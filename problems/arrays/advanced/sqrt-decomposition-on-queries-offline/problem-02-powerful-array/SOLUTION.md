# Solution — Powerful Array

## Brute Force

For each query, count occurrences in `a[l..r]` and evaluate `Σ Ks²·s`.

```python
from collections import Counter

def brute(a, queries):
    out = []
    for l, r in queries:                 # l, r are 1-indexed inclusive
        c = Counter(a[l - 1:r])
        out.append(sum(k * k * s for s, k in c.items()))
    return out
```

- **Time:** `O(q * n)` — up to `4*10^10` operations for the max constraints.
  Far too slow.
- **Space:** `O(n)` per query for the counter.

The statistic mixes squared frequencies with the value itself, so no prefix
sum or standard segment tree captures it directly. But it has a clean
incremental delta — perfect for Mo's.

## Optimal Approach — Mo's Algorithm (offline sqrt decomposition)

### Incremental delta

Keep `freq[v]` and a running `power`. Suppose value `v` currently occurs `k`
times inside the window.

- **Add one `v`** (`k → k+1`): its contribution grows from `k²·v` to `(k+1)²·v`,
  so `power += ((k+1)² − k²)·v = (2k + 1)·v`. Then set `freq[v] = k+1`.
- **Remove one `v`** (`k → k−1`): contribution shrinks to `(k−1)²·v`, so
  `power += ((k−1)² − k²)·v = −(2k − 1)·v`. Then set `freq[v] = k−1`.

A tidy way to code removal is: decrement `freq[v]` first, then subtract
`(2·freq[v] + 1)·v`, which equals `(2(k−1) + 1)·v = (2k − 1)·v`.

Each update is `O(1)`, so `f = O(1)` and the whole algorithm runs in
**`O((n + q) · sqrt(n))`**.

### Why it is correct

`power` is maintained as the exact value of `Σ_v freq[v]²·v` over the current
window `[curL, curR]`. Each single-element `add`/`remove` applies precisely the
change in that sum. Because we always step the pointers one index at a time to
reach a query's bounds, when `[curL, curR] == [l−1, r−1]` (0-indexed) the value
of `power` is the answer, and it is stored at the query's original index.

### Reference implementation

```python
from typing import List, Tuple


def powerful_array(a: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    n = len(a)
    q = len(queries)
    if q == 0:
        return []
    block = max(1, int(n / (q ** 0.5)))

    # convert to 0-indexed inclusive bounds
    qs = [(l - 1, r - 1) for (l, r) in queries]
    order = sorted(
        range(q),
        key=lambda k: (qs[k][0] // block,
                       qs[k][1] if (qs[k][0] // block) % 2 == 0 else -qs[k][1]),
    )

    max_val = max(a) if a else 0
    freq = [0] * (max_val + 1)
    power = 0
    ans = [0] * q
    cur_l, cur_r = 0, -1

    def add(i: int) -> None:
        nonlocal power
        v = a[i]
        power += (2 * freq[v] + 1) * v
        freq[v] += 1

    def remove(i: int) -> None:
        nonlocal power
        v = a[i]
        freq[v] -= 1
        power -= (2 * freq[v] + 1) * v

    for k in order:
        l, r = qs[k]
        while cur_r < r:
            cur_r += 1
            add(cur_r)
        while cur_l > l:
            cur_l -= 1
            add(cur_l)
        while cur_r > r:
            remove(cur_r)
            cur_r -= 1
        while cur_l < l:
            remove(cur_l)
            cur_l += 1
        ans[k] = power
    return ans
```

## Key Insights & Edge Cases

- **64-bit overflow:** With `n = 2*10^5` all-equal values up to `10^6`, the power
  reaches `(2*10^5)² * 10^6 ≈ 4*10^16`, which overflows 32-bit but fits in 64-bit.
  In C++ use `long long`; Python integers are arbitrary precision so no action
  needed there.
- **Add/remove symmetry:** the "increment-then-add" vs "decrement-then-subtract"
  ordering keeps `freq[v]` non-negative at every step and makes the delta formula
  identical (`(2·freq + 1)·v`) in both directions.
- **Expand-before-shrink** ordering of the four `while` loops prevents transient
  negative-width windows.
- **Block size tuning:** `B = n / sqrt(q)` slightly beats a fixed `sqrt(n)` when
  `q` is much larger or smaller than `n`; both are asymptotically optimal.
