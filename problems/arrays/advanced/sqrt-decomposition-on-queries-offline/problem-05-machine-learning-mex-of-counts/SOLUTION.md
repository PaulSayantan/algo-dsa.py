# Solution — Machine Learning (Mex of Occurrence Counts)

## Brute Force

Process ops in order; for a type-1 query, count occurrences in `a[l..r]`, collect
the set of occurrence counts, and scan upward for the mex.

```python
from collections import Counter

def brute(n, a, ops):
    arr = a[:]                      # 0-indexed copy
    out = []
    for op in ops:
        if op[0] == 1:
            _, l, r = op
            counts = set(Counter(arr[l - 1:r]).values())
            m = 1
            while m in counts:
                m += 1
            out.append(m)
        else:
            _, p, x = op
            arr[p - 1] = x
    return out
```

- **Time:** `O(q * n)` for the scans (plus small mex loop) — `~10^10`. Too slow.
- **Space:** `O(n)`.

Point updates block plain Mo's and prefix structures alike; we extend Mo's with a
*time* axis.

## Optimal Approach — Mo's Algorithm with Point Updates (3D Mo's)

### Data maintained

- `cnt[value]` — occurrences of each (compressed) value in the current window.
- `occ[t]` — number of *distinct values* whose occurrence count is exactly `t`.

`add`/`remove` of one element updates both:

```
add(v):    occ[cnt[v]] -= 1; cnt[v] += 1; occ[cnt[v]] += 1
remove(v): occ[cnt[v]] -= 1; cnt[v] -= 1; occ[cnt[v]] += 1
```

Answering a type-1 query: scan `t = 1, 2, 3, ...` and return the first `t` with
`occ[t] == 0`. By the `M(M-1)/2 <= len` bound, this loop is `O(sqrt(len))`.

### Adding the time dimension

Number the type-1 queries with the count of updates that precede them
(`time`). Each type-2 update is stored as `(pos, new_val, old_val)`. The current
state of the array is defined by "how many updates have been applied", tracked by
a pointer `cur_t`.

- **Apply update `u`** (move time forward): if `pos[u]` is inside the current
  `[curL, curR]`, `remove(old_val)` then `add(new_val)`. Then set the array at
  `pos[u]` to `new_val`. (Swap `old`/`new` stored so the reverse works.)
- **Undo update `u`** (move time backward): symmetric — restore `old_val`.

A clean trick: keep the update as a pair and, on each application, *swap* its two
values so the same routine both applies and undoes.

### Sorting and block size

Use block size `B ≈ n^(2/3)`. Sort type-1 queries by
`(l // B, r // B, time)`. This balances three kinds of pointer travel:

- left pointer within a block: `O(B)` per query,
- right pointer within an (l-block, r-block) bucket: monotone in `time`,
- time pointer swept per bucket.

The classic analysis gives **`O(n^(2/3) · q)`** total operations (times the
`O(sqrt(len))` mex scan, which is dominated / folded into constants in practice).

### Why it is correct

At any moment the pair `(window [curL,curR], applied-update-count cur_t)`
uniquely determines the *actual* array contents of that window at that query's
point in time. `cnt` and `occ` are exact invariants for that state. We move all
three pointers (`curL`, `curR`, `cur_t`) one step at a time to match each query's
`(l, r, time)`; when they match, the array window equals what the query would see
in the online problem, so the mex computed from `occ` is correct. Answers are
recorded at each query's original position.

### Reference implementation (sketch)

```python
from typing import List, Tuple


def mex_of_counts(n, a, ops):
    # 1. gather values for compression
    vals = list(a)
    updates = []      # (pos0, new_val_raw)
    queries = []      # (l0, r0, time, qid)
    time = 0
    for op in ops:
        if op[0] == 2:
            _, p, x = op
            vals.append(x)
            updates.append((p - 1, x))
        else:
            _, l, r = op
            queries.append((l - 1, r - 1, len(updates), len(queries)))
    comp = {v: i for i, v in enumerate(sorted(set(vals)))}
    arr = [comp[v] for v in a]
    updates = [(pos, comp[x]) for (pos, x) in updates]

    B = max(1, int(round(n ** (2 / 3))))
    queries.sort(key=lambda t: (t[0] // B, t[1] // B, t[2]))

    max_id = len(comp)
    cnt = [0] * (max_id + 1)
    occ = [0] * (n + 2)                 # occ[t] over t = 0..n
    ans = [0] * len(queries)

    cur_l, cur_r, cur_t = 0, -1, 0

    def add(pos):
        v = arr[pos]
        occ[cnt[v]] -= 1
        cnt[v] += 1
        occ[cnt[v]] += 1

    def remove(pos):
        v = arr[pos]
        occ[cnt[v]] -= 1
        cnt[v] -= 1
        occ[cnt[v]] += 1

    def apply_update(i):
        pos, newv = updates[i]
        if cur_l <= pos <= cur_r:
            remove(pos)
            arr[pos] = newv
            add(pos)
        else:
            arr[pos] = newv
        # store previous value so we can undo
        updates[i] = (pos, arr_prev)  # see note below

    # In practice keep an explicit old-value array; the swap-in-place idiom
    # is shown for brevity. A robust version stores (pos, val) and swaps.

    for l, r, t, qid in queries:
        while cur_t < t:
            _roll_forward(cur_t); cur_t += 1
        while cur_t > t:
            cur_t -= 1; _roll_back(cur_t)
        while cur_r < r:
            cur_r += 1; add(cur_r)
        while cur_l > l:
            cur_l -= 1; add(cur_l)
        while cur_r > r:
            remove(cur_r); cur_r -= 1
        while cur_l < l:
            remove(cur_l); cur_l += 1
        m = 1
        while occ[m] > 0:
            m += 1
        ans[qid] = m
    return ans
```

A fully robust roll-forward/back keeps an explicit `old_val` per update and swaps
`arr[pos]` with the stored value (guarded by the in-window check) so applying and
undoing share one routine. The sketch above shows structure; production code
should store both endpoints of each update to make `_roll_forward` / `_roll_back`
exact inverses.

## Key Insights & Edge Cases

- **Mex is small:** the `M(M-1)/2 <= len` bound is what makes the linear scan for
  the mex cheap (`O(sqrt(len))`), and it is why the answer never exceeds
  ~`sqrt(n)`.
- **Block size `n^(2/3)`, not `sqrt(n)`:** with an update dimension, `n^(2/3)`
  balances the three pointer costs and yields `O(n^(2/3) q)`; using `sqrt(n)`
  degrades to `O(q * n)` from time-pointer thrashing.
- **In-window guard on updates:** only touch `cnt`/`occ` when the updated
  position currently lies in `[curL, curR]`; otherwise just change the stored
  array value. Forgetting the guard corrupts the histogram.
- **Compress update values too:** the new values `x` from type-2 ops must be part
  of the coordinate compression, or the value table misses them.
- **Move the time pointer consistently** relative to the window pointers; a
  common, safe convention is to settle `cur_t` first, then expand the window,
  then shrink — as long as apply/undo respect the current window bounds it is
  correct either way.
- **Ordering of `occ` updates** in add/remove (`occ[old]--`, adjust `cnt`,
  `occ[new]++`) must bracket the `cnt` change, mirroring the `atLeast` discipline
  from the tree problem.
