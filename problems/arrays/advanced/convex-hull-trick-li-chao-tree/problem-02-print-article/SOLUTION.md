# Print Article — Solution

## Brute Force

Build prefix sums `S`, then run the partition DP directly:

```
dp[0] = 0
for i in 1 .. N:
    for j in 0 .. i-1:
        dp[i] = min(dp[i], dp[j] + (S[i] - S[j])^2 + M)
answer = dp[N]
```

- **Time:** `O(N^2)`.
- **Space:** `O(N)`.

With `N` up to `5 * 10^5`, `O(N^2)` is about `2.5 * 10^11` operations — far too slow.

## Optimal Approach — Monotonic Convex Hull Trick

### Turn the transition into a minimum over lines

Let `S[i]` be the prefix sum of the first `i` costs (`S[0] = 0`). Expand:

```
dp[i] = min_j ( dp[j] + S[i]^2 - 2 S[i] S[j] + S[j]^2 + M )
      = S[i]^2 + M + min_j ( (-2 S[j]) * S[i] + (dp[j] + S[j]^2) )
```

Each earlier index `j` contributes a line

```
line_j(x) = m_j * x + b_j,   m_j = -2 S[j],   b_j = dp[j] + S[j]^2
```

queried at `x = S[i]`. So `dp[i] = S[i]^2 + M + min_j line_j(S[i])`. The `S[i]^2 + M`
part is independent of `j` and added after the minimization.

### Why the hull is monotonic

Costs are non-negative, so prefix sums `S` are **non-decreasing**. Therefore:

- **Slopes `m_j = -2 S[j]` are non-increasing** as `j` grows — new lines append to
  the back of the hull.
- **Query points `x = S[i]` are non-decreasing** — the optimal-line pointer only
  moves forward.

That is precisely the monotonic CHT regime: amortized `O(1)` per insert and per
query, giving an overall `O(N)` algorithm.

> Duplicate / equal slopes (when a cost is `0`, so `S[j] = S[j-1]`) are handled by
> the `<=` in the redundancy test and the `<=` in the pointer advance: among equal
> slopes only the one with the smaller intercept survives, which is correct for
> minimization.

### Reference implementation

```python
from typing import List

def min_print_cost(cost: List[int], m: int) -> int:
    n = len(cost)
    S = [0] * (n + 1)
    for i in range(n):
        S[i + 1] = S[i] + cost[i]

    slopes: List[int] = []
    intercepts: List[int] = []
    ptr = 0

    def bad(m1, b1, m2, b2, m3, b3) -> bool:
        return (b3 - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m3)

    def add_line(a: int, b: int) -> None:
        while len(slopes) >= 2 and bad(slopes[-2], intercepts[-2],
                                       slopes[-1], intercepts[-1], a, b):
            slopes.pop(); intercepts.pop()
        slopes.append(a); intercepts.append(b)

    def query(x: int) -> int:
        nonlocal ptr
        if ptr >= len(slopes):
            ptr = len(slopes) - 1
        while ptr + 1 < len(slopes) and \
              slopes[ptr + 1] * x + intercepts[ptr + 1] <= slopes[ptr] * x + intercepts[ptr]:
            ptr += 1
        return slopes[ptr] * x + intercepts[ptr]

    dp = [0] * (n + 1)
    add_line(-2 * S[0], dp[0] + S[0] ** 2)   # line for j = 0
    for i in range(1, n + 1):
        dp[i] = S[i] ** 2 + m + query(S[i])
        add_line(-2 * S[i], dp[i] + S[i] ** 2)
    return dp[n]
```

- **Time:** `O(N)`.
- **Space:** `O(N)` for prefix sums, hull, and `dp`.

## Key Insights & Edge Cases

- **Prefix sums are the query axis.** Whenever a segment cost depends on a segment
  *sum*, prefix sums turn `(S_i - S_j)^2` into a clean line-versus-query form.
- **Non-negative costs are what buy you the O(N) monotonic hull.** If costs could be
  negative, prefix sums would not be monotone and you would fall back to
  binary-search CHT or a Li Chao Tree.
- **Add `S[i]^2 + M` after the min**, never inside the lines — it depends only on `i`.
- **`N = 1`:** the single batch answer is `cost[0]^2 + M`, produced by one query
  against the `j = 0` line.
- **Integer cross-multiplication** keeps everything exact; values fit in 64 bits
  (`S[i] <= 5*10^7`, so `S[i]^2 <= 2.5*10^15`).
