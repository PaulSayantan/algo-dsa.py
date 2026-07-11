# Solution — Naive Operations

## Brute Force

Keep `a` as a plain array. A range increment `[0, l, r]` loops over `[l, r]`
doing `a[i] += 1`. A query `[1, l, r]` loops over `[l, r]` summing
`a[i] // b[i]`.

- **Time:** `O(q * n)` — both operations are `O(n)`. With `n, q = 10^5` this is
  `10^10`, too slow.
- **Space:** `O(n)`.

The waste: recomputing `a[i] // b[i]` from scratch every query, and incrementing
individual elements even though most increments do not change any quotient.

## Optimal Approach (Segment Tree Beats break condition on a countdown)

The quotient `a[i] // b[i]` rises by `1` exactly each time `a[i]` crosses a
multiple of `b[i]`. Track, per index, a **countdown**:

```
need[i] = b[i] - (a[i] mod b[i])   # increments remaining until the next tick
```

Initially `a[i] = 0`, so `need[i] = b[i]`. A range increment on `[l, r]` is a
**range `-1`** applied to `need` over `[l, r]`. Whenever a `need[i]` reaches `0`,
the quotient for index `i` has just increased by `1`: add `1` to that index's
stored answer and **reset** `need[i]` to `b[i]`.

Segment tree node stores:

- `mn`   — the minimum `need` in the sub-range,
- `add`  — a lazy pending decrement (to be subtracted from `mn` / pushed down),
- `sum`  — the sum of stored answers (`a[i] // b[i]`) over the sub-range.

**Range increment / decrement** `[l, r]`:

```python
def add_update(k, lo, hi, l, r):
    if r < lo or hi < l:
        return
    if l <= lo and hi <= r:
        mn[k] -= 1
        add[k] += 1
        if mn[k] > 0:          # BREAK CONDITION: nothing ticked here, stop
            return
        # some leaf hit 0 -> must descend to find & reset it
    if lo == hi:              # leaf reached 0 -> tick and reset
        sum[k] += 1
        mn[k] = b[lo]
        add[k] = 0
        return
    push_down(k)
    mid = (lo + hi) // 2
    add_update(2*k, lo, mid, l, r)
    add_update(2*k+1, mid+1, hi, l, r)
    pull_up(k)                # mn = min(children), sum = sum(children)
```

The essential Beats-style move is the **break condition** `if mn[k] > 0: return`
after fully covering a node: if the smallest countdown in the whole sub-range is
still positive, no quotient ticked, so we do not descend. We recurse only when
some countdown reached `0`, and only far enough to find and reset those leaves.

`push_down` propagates the lazy `-add` into the children's `mn` and `add`.
Query `[1, l, r]` is a standard range-sum over `sum`.

Reference core:

```python
class Beats:
    def __init__(self, b):
        self.n = len(b)
        self.b = b
        self.mn  = [0] * (4 * self.n)
        self.lz  = [0] * (4 * self.n)   # pending decrement
        self.sm  = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1)

    def _build(self, k, lo, hi):
        if lo == hi:
            self.mn[k] = self.b[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * k, lo, mid)
        self._build(2 * k + 1, mid + 1, hi)
        self.mn[k] = min(self.mn[2 * k], self.mn[2 * k + 1])

    def _apply(self, k, d):
        self.mn[k] -= d
        self.lz[k] += d

    def _push(self, k):
        if self.lz[k]:
            self._apply(2 * k, self.lz[k])
            self._apply(2 * k + 1, self.lz[k])
            self.lz[k] = 0

    def _pull(self, k):
        self.mn[k] = min(self.mn[2 * k], self.mn[2 * k + 1])
        self.sm[k] = self.sm[2 * k] + self.sm[2 * k + 1]

    def inc(self, k, lo, hi, l, r):
        if r < lo or hi < l:
            return
        if l <= lo and hi <= r and self.mn[k] - 1 > 0:
            self._apply(k, 1)          # BREAK: whole range stays positive
            return
        if lo == hi:                   # leaf hitting zero -> tick & reset
            self.sm[k] += 1
            self.mn[k] = self.b[lo]
            return
        self._push(k)
        mid = (lo + hi) // 2
        self.inc(2 * k, lo, mid, l, r)
        self.inc(2 * k + 1, mid + 1, hi, l, r)
        self._pull(k)

    def qsum(self, k, lo, hi, l, r):
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return self.sm[k]
        self._push(k)
        mid = (lo + hi) // 2
        return (self.qsum(2 * k, lo, mid, l, r)
                + self.qsum(2 * k + 1, mid + 1, hi, l, r))
```

Convert 1-indexed operations to 0-indexed before calling in.

**Why it is fast (amortized).** Over the whole run, index `i` can tick at most
`T_i / b[i]` times, where `T_i` is the total number of increments it receives.
Since `T_i <= q` and `b` is a permutation of `1..n`, the total number of ticks is
at most `sum over i of q / b[i] = q * (1 + 1/2 + ... + 1/n) = O(q log n)`. Each
tick costs one `O(log n)` descent to a leaf; each range increment costs
`O(log n)` for the covered nodes that stay positive. So the total is
`O((n + q) log n + (q log n) log n) = O((n + q) log^2 n)` in the worst case, and
much less in practice.

- **Time:** `O((n + q) log^2 n)` amortized (near-linear-logarithmic).
- **Space:** `O(n)`.

## Key Insights & Edge Cases

- **Do not store `a` explicitly.** Storing the countdown `need[i]` turns a range
  increment into a uniform range `-1`, which *is* a normal lazy tag — the Beats
  break condition then avoids touching stable regions.
- **Break condition on the post-decrement minimum.** Apply the `-1`, and if the
  node's minimum is still `> 0`, stop. Descend only when the minimum reaches `0`.
- **Reset must set `need` back to `b[i]`, not to `0`.** After a tick, the next
  tick is another `b[i]` increments away.
- **A single increment ticks at most one step per index**, so at a leaf reaching
  `0` you add exactly `1` and reset — you never need a `while` loop there.
- **`b` being a permutation** is what bounds the total ticks by the harmonic sum
  `O(q log n)`; if `b` could contain `1`s repeatedly, ticks would be more
  frequent, but the same structure still works.
- **Relation to Beats.** This is the "count down to an event and prune where the
  event cannot happen yet" flavor of Beats — structurally the same as the chmin
  tree, but the pruned quantity is a minimum countdown rather than a maximum.
