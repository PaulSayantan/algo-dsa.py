# Powerful Array — Solution

## Brute Force

For each query, build the frequency map of `a[l..r]` and sum `cnt[x]² · x` over the
distinct values.

- Time: `O(q * n)` — with `n = q = 2*10^5` that is `4*10^10`, hopeless.
- Space: `O(n)` per query.

`power` is a nonlinear function of the frequency histogram (`cnt²`), so it does not
decompose across sub-ranges — no prefix sums, no segment-tree merge. But it *does*
admit a clean incremental update when a single element enters or leaves, which is the
signal for Mo's Algorithm.

## Optimal Approach — Mo's Algorithm

Keep a sliding window `[curL, curR]` with:

- `cnt[x]` — occurrences of value `x` in the window,
- `cur` — the running value of `Σ cnt[x]² · x`.

### The incremental delta

If value `x` currently occurs `c` times, its contribution is `c² · x`. Adding one
occurrence makes it `(c+1)² · x`. The change is:

```
(c+1)² · x − c² · x = (2c + 1) · x
```

So on **add**, do `cur += (2 * cnt[x] + 1) * x` *then* `cnt[x] += 1`.
On **remove**, first `cnt[x] -= 1`, then note the term drops from `(c)²·x` to
`(c−1)²·x`, a change of `−(2(c−1)+1)·x = −(2·cnt[x] + 1)·x` after the decrement:

```
add(i):    x = a[i]
           cur += (2 * cnt[x] + 1) * x
           cnt[x] += 1

remove(i): x = a[i]
           cnt[x] -= 1
           cur -= (2 * cnt[x] + 1) * x
```

Both are `O(1)` and keep `cur` exactly equal to `Σ cnt[x]² · x`.

### Why it is correct

`cur` is maintained as a telescoping sum of exact per-step deltas. Each `add`/`remove`
adjusts exactly the term for the affected value `x` by the algebraic identity above,
leaving all other terms unchanged. Thus the invariant `cur == Σ_x cnt[x]² · x` holds
after every operation, and in particular when the window matches a query's `[l, r]`.
Because the array is static, reordering queries never alters an individual answer.

### Full procedure

1. `block = max(1, int(n / √q))`.
2. Sort query indices by `(l // block, r)` with the even/odd `r` trick.
3. `curL, curR, cur = 0, -1, 0`.
4. For each sorted query, expand/shrink the window with the grow-first order and
   record `ans[id] = cur`.

### Reference implementation

```python
from math import isqrt
from typing import List, Tuple


def powerful_array(a: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    n, q = len(a), len(queries)
    ans = [0] * q
    if n == 0 or q == 0:
        return ans

    block = max(1, int(n / max(1, isqrt(q))))
    order = sorted(
        range(q),
        key=lambda i: (
            queries[i][0] // block,
            queries[i][1] if (queries[i][0] // block) % 2 == 0 else -queries[i][1],
        ),
    )

    max_val = max(a) + 1
    cnt = [0] * max_val
    cur = 0
    curL, curR = 0, -1

    def add(i: int) -> None:
        nonlocal cur
        x = a[i]
        cur += (2 * cnt[x] + 1) * x
        cnt[x] += 1

    def remove(i: int) -> None:
        nonlocal cur
        x = a[i]
        cnt[x] -= 1
        cur -= (2 * cnt[x] + 1) * x

    for i in order:
        l, r = queries[i]
        while curR < r:
            curR += 1
            add(curR)
        while curL > l:
            curL -= 1
            add(curL)
        while curR > r:
            remove(curR)
            curR -= 1
        while curL < l:
            remove(curL)
            curL += 1
        ans[i] = cur
    return ans
```

### Complexity

- Sorting: `O(q log q)`.
- Pointer movement: `O((n + q) * √n)` `O(1)` steps.
- Overall: `O((n + q) * √n)`. Space: `O(n + q + V)`, `V = max value`.

## Key Insights & Edge Cases

- **Derive the delta once and reuse it symmetrically.** On add use `cnt` *before*
  incrementing; on remove decrement *first*, then subtract using the new `cnt`. Both
  refer to the same `(2·c + 1)·x` with `c` the *smaller* of the two counts.
- **64-bit / big integers.** With `cnt` up to `2·10^5` and `x` up to `10^6`,
  `cnt²·x` reaches ~`4·10^16`; summed over values it exceeds 32-bit range. Python
  handles this natively; in C++ use `long long`.
- **Large value domain** (`a[i]` up to `10^6`): a flat `cnt` array of that size is
  fine; otherwise compress.
- **Single element** window: `cur = x` (since `1²·x`). Matches example 2's `(0,0)`.
- **Empty window init** `cur = 0`, `curL = 0`, `curR = -1`.
- Offline & static only, like every plain Mo's problem.
