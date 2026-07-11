# Kalila and Dimna in the Forest — Solution

## Brute Force

Evaluate the recurrence directly:

```
dp[0] = 0
for i in 1 .. N-1:
    dp[i] = min over j < i of ( dp[j] + b[j] * a[i] )
answer = dp[N-1]
```

- **Time:** `O(N^2)`.
- **Space:** `O(N)`.

With `N` up to `10^5`, `O(N^2)` is `10^10` operations — too slow.

## Optimal Approach — Monotonic Convex Hull Trick

### The transition is already a line

No expansion is needed here. Read

```
dp[j] + b[j] * a[i]
```

as a line

```
line_j(x) = m_j * x + b_j_intercept,   m_j = b[j],   b_j_intercept = dp[j]
```

evaluated at the query point `x = a[i]`. Then

```
dp[i] = min_j line_j(a[i]).
```

Because we minimize, only lines on the **lower hull** matter.

### Why the hull is monotonic

The problem guarantees two orderings:

- **Slopes `m_j = b[j]` are non-increasing** (`b` is given non-increasing), so each
  new line is appended to the back of the hull.
- **Query points `a[i]` are strictly increasing**, so the optimal-line pointer only
  advances.

That is the monotonic CHT regime — amortized `O(1)` per insert and per query, so the
whole DP is `O(N)`.

### Reference implementation

```python
from typing import List

def min_total_cost(a: List[int], b: List[int]) -> int:
    n = len(a)
    slopes: List[int] = []
    intercepts: List[int] = []
    ptr = 0

    def bad(m1, b1, m2, b2, m3, b3) -> bool:
        # middle line (m2,b2) redundant given neighbours 1 and 3
        return (b3 - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m3)

    def add_line(m: int, c: int) -> None:
        while len(slopes) >= 2 and bad(slopes[-2], intercepts[-2],
                                       slopes[-1], intercepts[-1], m, c):
            slopes.pop(); intercepts.pop()
        slopes.append(m); intercepts.append(c)

    def query(x: int) -> int:
        nonlocal ptr
        if ptr >= len(slopes):
            ptr = len(slopes) - 1
        while ptr + 1 < len(slopes) and \
              slopes[ptr + 1] * x + intercepts[ptr + 1] <= slopes[ptr] * x + intercepts[ptr]:
            ptr += 1
        return slopes[ptr] * x + intercepts[ptr]

    dp = [0] * n
    add_line(b[0], dp[0])            # line for j = 0
    for i in range(1, n):
        dp[i] = query(a[i])
        add_line(b[i], dp[i])
    return dp[n - 1]
```

- **Time:** `O(N)`.
- **Space:** `O(N)`.

## Key Insights & Edge Cases

- **Not every CHT problem needs algebra.** When the transition is literally
  `dp[j] + (slope depending on j) * (value depending on i)`, the lines are handed to
  you directly. This is the cleanest CHT template.
- **Equal slopes** (repeated `b` values) are safe: the redundancy test's `<=` keeps
  only the lower intercept among equal-slope lines.
- **`N = 1`:** no tree to cut after the first, `dp[0] = 0` is the answer.
- **64-bit values:** `b[j] * a[i]` can reach `10^9 * 10^9 = 10^18`, still within
  signed 64-bit range; Python integers are unbounded, but in C++/Java use `long long`.
- **Monotonicity is provided by the statement.** If either ordering failed you would
  need binary-search CHT (arbitrary queries) or a Li Chao Tree (arbitrary slopes).
