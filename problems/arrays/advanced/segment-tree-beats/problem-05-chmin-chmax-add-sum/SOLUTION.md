# Solution — Full Segment Tree Beats (chmin / chmax / add / sum)

## Brute Force

Keep the array. Each of chmin, chmax, add loops over `[l, r)`; each sum query
loops and adds.

- **Time:** `O(q * n)` — every update can touch the whole array. With
  `n, q = 2 * 10^5` this is `4 * 10^10`, far too slow.
- **Space:** `O(n)`.

Neither chmin nor chmax is a uniform lazy tag (each touches only the elements on
one side of `x`), so an ordinary lazy segment tree cannot do this either. The
full Segment Tree Beats maintains enough per-node statistics to decide, in `O(1)`,
whether a chmin/chmax is uniform on a node.

## Optimal Approach (Full Segment Tree Beats)

Each node stores, over its sub-range:

- `sum`               — the sum of values,
- `mx, mx2, mxc`      — maximum, **strict** second maximum, count of the maximum,
- `mn, mn2, mnc`      — minimum, **strict** second minimum, count of the minimum,
- `add`               — a lazy pending "add to all" tag.

The three primitive node updates:

```
apply_add(node, v):                 # add v to every element
    node.sum += v * node.len
    node.mx += v;  if node.mx2 != -INF: node.mx2 += v
    node.mn += v;  if node.mn2 != +INF: node.mn2 += v
    node.add += v

apply_chmin(node, x):               # precondition: node.mx2 < x < node.mx
    node.sum -= (node.mx - x) * node.mxc
    if node.mn  == node.mx:  node.mn  = x     # single distinct value
    if node.mn2 == node.mx:  node.mn2 = x     # x becomes a second-min boundary
    node.mx = x

apply_chmax(node, x):               # precondition: node.mn2 > x > node.mn
    node.sum += (x - node.mn) * node.mnc
    if node.mx  == node.mn:  node.mx  = x
    if node.mx2 == node.mn:  node.mx2 = x
    node.mn = x
```

**chmin update on `[l, r)` with `x`** (chmax is the mirror image):

```python
def chmin(k, lo, hi, l, r, x):
    if r <= lo or hi <= l or mx[k] <= x:      # disjoint OR no element exceeds x
        return                                # -> break, nothing to do
    if l <= lo and hi <= r and mx2[k] < x:    # covered AND uniform-on-max
        apply_chmin(k, x)                     # -> O(1) tag, break
        return
    push_down(k)                              # "beaten": recurse
    mid = (lo + hi) // 2
    chmin(2*k, lo, mid, l, r, x)
    chmin(2*k+1, mid+1, hi, l, r, x)
    pull_up(k)
```

**Merge (pull up)** combines two children by merging their max-side and min-side
statistics independently:

```python
def merge_max(mxL, mx2L, mxcL, mxR, mx2R, mxcR):
    if mxL == mxR:  return mxL, max(mx2L, mx2R), mxcL + mxcR
    if mxL >  mxR:  return mxL, max(mx2L, mxR),  mxcL
    return               mxR, max(mx2R, mxL),  mxcR
# symmetric merge_min uses min(...) and the smaller second-min
```

`push_down` first pushes the `add` tag to both children (via `apply_add`), then
clamps each child with the parent's `mx` (chmin) and `mn` (chmax) using
`apply_chmin` / `apply_chmax` **only if** the child's extreme exceeds/undershoots
the parent's bound. Sum query is the standard range-sum over `sum`.

Reference core (0-indexed, half-open handled by the caller):

```python
INF = float("inf")

class Beats:
    def __init__(self, a):
        self.n = len(a)
        s = 4 * self.n
        self.sum = [0] * s
        self.mx  = [-INF] * s; self.mx2 = [-INF] * s; self.mxc = [0] * s
        self.mn  = [ INF] * s; self.mn2 = [ INF] * s; self.mnc = [0] * s
        self.add = [0] * s
        self.len = [0] * s
        self._build(1, 0, self.n - 1, a)

    def _pull(self, k):
        l, r = 2 * k, 2 * k + 1
        self.sum[k] = self.sum[l] + self.sum[r]
        # max side
        if self.mx[l] == self.mx[r]:
            self.mx[k] = self.mx[l]; self.mxc[k] = self.mxc[l] + self.mxc[r]
            self.mx2[k] = max(self.mx2[l], self.mx2[r])
        elif self.mx[l] > self.mx[r]:
            self.mx[k] = self.mx[l]; self.mxc[k] = self.mxc[l]
            self.mx2[k] = max(self.mx2[l], self.mx[r])
        else:
            self.mx[k] = self.mx[r]; self.mxc[k] = self.mxc[r]
            self.mx2[k] = max(self.mx2[r], self.mx[l])
        # min side (mirror)
        if self.mn[l] == self.mn[r]:
            self.mn[k] = self.mn[l]; self.mnc[k] = self.mnc[l] + self.mnc[r]
            self.mn2[k] = min(self.mn2[l], self.mn2[r])
        elif self.mn[l] < self.mn[r]:
            self.mn[k] = self.mn[l]; self.mnc[k] = self.mnc[l]
            self.mn2[k] = min(self.mn2[l], self.mn[r])
        else:
            self.mn[k] = self.mn[r]; self.mnc[k] = self.mnc[r]
            self.mn2[k] = min(self.mn2[r], self.mn[l])

    def _apply_add(self, k, v):
        self.sum[k] += v * self.len[k]
        self.mx[k] += v
        if self.mx2[k] != -INF: self.mx2[k] += v
        self.mn[k] += v
        if self.mn2[k] !=  INF: self.mn2[k] += v
        self.add[k] += v

    def _apply_min(self, k, x):     # x < mx[k], x > mx2[k]
        if x >= self.mx[k]:
            return
        self.sum[k] -= (self.mx[k] - x) * self.mxc[k]
        if self.mn[k]  == self.mx[k]: self.mn[k]  = x
        if self.mn2[k] == self.mx[k]: self.mn2[k] = x
        self.mx[k] = x

    def _apply_max(self, k, x):     # x > mn[k], x < mn2[k]
        if x <= self.mn[k]:
            return
        self.sum[k] += (x - self.mn[k]) * self.mnc[k]
        if self.mx[k]  == self.mn[k]: self.mx[k]  = x
        if self.mx2[k] == self.mn[k]: self.mx2[k] = x
        self.mn[k] = x

    def _push(self, k):
        for c in (2 * k, 2 * k + 1):
            if self.add[k]:
                self._apply_add(c, self.add[k])
            self._apply_min(c, self.mx[k])
            self._apply_max(c, self.mn[k])
        self.add[k] = 0
```

The public `chmin`, `chmax`, `range_add`, and `range_sum` follow the standard
decompose/recurse structure, calling `_push` before recursing and `_pull` after,
with the break/tag conditions shown above (`mx <= x` break, `mx2 < x` tag for
chmin; the mirror for chmax).

**Correctness.** For chmin, if `mx <= x` nothing exceeds `x` (identity); if
`mx2 < x < mx` the only elements above `x` are exactly the `mxc` copies of the
max, so lowering them to `x` is exact and the second-max/count are preserved; if
`x <= mx2`, two distinct values exceed `x` and one tag cannot express the result,
so we recurse. chmax is symmetric. The `add` tag shifts all six extreme
statistics uniformly, so it composes cleanly with the clamp tags as long as add
is pushed first during `push_down`.

**Why it is fast (potential argument).** As in the chmin-only tree, a recursion
("beat") occurs only when a clamp target lands between an extreme and its second
extreme, which strictly reduces the number of distinct extreme values in the
affected subtrees. With both chmin and chmax present, and range-add reshuffling
the extremes, the tightest proven bound is `O((n + q) log^2 n)` amortized (the
chmin-only or chmax-only case is `O((n + q) log n)`).

- **Time:** `O((n + q) log^2 n)` amortized.
- **Space:** `O(n)`.

## Key Insights & Edge Cases

- **Second-extremes must be STRICT.** `mx2` is the largest value strictly below
  `mx`; `mn2` is the smallest value strictly above `mn`. The tag conditions
  (`mx2 < x`, `x < mn2`) depend on this; a non-strict second extreme breaks both
  correctness and termination.
- **The two sides interact.** When a chmin lowers `mx` and the node had
  `mn == mx` (all equal) or `mn2 == mx`, the min-side statistics must be updated
  too — see the `if node.mn == node.mx` / `if node.mn2 == node.mx` lines. Forget
  these and the min side silently desyncs. The same applies mirrored for chmax.
- **Push order in `push_down`: add first, then clamps.** The stored `mx`/`mn`
  bounds are already post-add for this node, so children must receive the add
  before being clamped by them.
- **Sentinels.** Use `-INF` for "no second max" and `+INF` for "no second min",
  and guard against shifting a sentinel during `apply_add`.
- **Redundant/degenerate updates.** chmin with `x >= mx`, chmax with `x <= mn`,
  and add with `x == 0` are all no-ops caught by the break conditions.
- **Half-open ranges.** This problem uses `[l, r)`; convert to inclusive
  `[l, r-1]` (and skip empty ranges) before recursing, or thread the half-open
  convention through consistently.
- **This is the ceiling of the technique.** Every earlier problem in this folder
  is a special case: square-root and modulo use only a max + break condition;
  Gorgeous Sequence uses the max/second-max/count for chmin; Naive Operations
  prunes on a min countdown. The full tree simply carries both extremes plus an
  add tag at once.
