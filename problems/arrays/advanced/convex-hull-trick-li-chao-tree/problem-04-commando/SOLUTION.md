# Commando — Solution

## Brute Force

Prefix-sum the strengths, then run the maximization partition DP:

```
dp[0] = 0
for i in 1 .. N:
    for j in 0 .. i-1:
        x = S[i] - S[j]
        dp[i] = max(dp[i], dp[j] + a*x*x + b*x + c)
answer = dp[N]
```

- **Time:** `O(N^2)`.
- **Space:** `O(N)`.

With `N` up to `10^6`, `O(N^2)` (up to `10^12` operations) is hopeless.

## Optimal Approach — Maximization Convex Hull Trick

### Expand into a maximum over lines

Let `S[i]` be prefix sums (`S[0] = 0`). Expand `a*(S_i - S_j)^2`:

```
dp[i] = max_j ( dp[j] + a*(S_i^2 - 2 S_i S_j + S_j^2) + b*(S_i - S_j) + c )
      = (a*S_i^2 + b*S_i + c) + max_j ( (-2a*S_j) * S_i + (a*S_j^2 - b*S_j + dp[j]) )
```

So each earlier index `j` is a line

```
line_j(x) = m_j * x + b_j,   m_j = -2a*S_j,   b_j = a*S_j^2 - b*S_j + dp[j]
```

queried at `x = S_i`, and `dp[i] = (a*S_i^2 + b*S_i + c) + max_j line_j(S_i)`.

### Why the hull is monotonic (and which hull)

We take a **maximum**, so only lines on the **upper hull** can ever be optimal.

- `a < 0` implies `-2a > 0`. Since `w[i] > 0`, prefix sums `S_j` strictly increase,
  so **slopes `m_j = -2a*S_j` are strictly increasing** — new lines append to the back.
- **Query points `x = S_i` are strictly increasing** — the optimal-line pointer only
  advances.

Both operations are amortized `O(1)`, so the whole DP is `O(N)`.

### Clean trick: reduce maximization to the min-CHT you already have

Maximizing `m*x + b` over a set of lines is the same as minimizing `(-m)*x + (-b)`
and negating the result. Using the *minimization* hull from Problems 1-3 avoids
writing a second hull with flipped comparisons. To keep the min-hull's requirement
"slopes inserted in decreasing order", note that after negation the inserted slopes
`-m_j = 2a*S_j` are strictly *decreasing* (since `a < 0`), exactly as the min-hull
wants.

### Reference implementation

```python
from typing import List

def max_effectiveness(w: List[int], a: int, b: int, c: int) -> int:
    n = len(w)
    S = [0] * (n + 1)
    for i in range(n):
        S[i + 1] = S[i] + w[i]

    # Minimization hull: slopes must be inserted in DECREASING order,
    # queries answered for NON-DECREASING x.
    slopes: List[int] = []
    intercepts: List[int] = []
    ptr = 0

    def bad(m1, b1, m2, b2, m3, b3) -> bool:
        return (b3 - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m3)

    def add_line(m: int, bb: int) -> None:
        while len(slopes) >= 2 and bad(slopes[-2], intercepts[-2],
                                       slopes[-1], intercepts[-1], m, bb):
            slopes.pop(); intercepts.pop()
        slopes.append(m); intercepts.append(bb)

    def query_min(x: int) -> int:
        nonlocal ptr
        if ptr >= len(slopes):
            ptr = len(slopes) - 1
        while ptr + 1 < len(slopes) and \
              slopes[ptr + 1] * x + intercepts[ptr + 1] <= slopes[ptr] * x + intercepts[ptr]:
            ptr += 1
        return slopes[ptr] * x + intercepts[ptr]

    dp = [0] * (n + 1)

    def push(j: int) -> None:
        m = -2 * a * S[j]                 # true (max) slope
        bj = a * S[j] * S[j] - b * S[j] + dp[j]
        add_line(-m, -bj)                 # negate -> min hull

    push(0)
    for i in range(1, n + 1):
        best = -query_min(S[i])           # negate back to recover the max
        dp[i] = a * S[i] * S[i] + b * S[i] + c + best
        push(i)
    return dp[n]
```

- **Time:** `O(N)`.
- **Space:** `O(N)`.

## Key Insights & Edge Cases

- **Maximization = minimization of negated lines.** Negating both slope and
  intercept, minimizing, then negating the answer reuses one hull implementation and
  eliminates a whole class of "flip every comparison" bugs.
- **`a < 0` is essential** — it makes the negated slopes monotone in the direction
  the min-hull expects, and it makes non-trivial partitions worthwhile in the first
  place.
- **`a*S_i^2 + b*S_i + c` is `i`-only** and is added after the max, not baked into
  lines.
- **`N = 1`:** the single squad answer is `f(w[0]) = a*w0^2 + b*w0 + c`, produced by
  the one query against the `j = 0` line.
- **Overflow:** `S_i` up to `10^8`, so `a*S_i^2` reaches `~5*10^16` — fits in signed
  64-bit; use `long long` in C++/Java.
- If `w[i]` could be zero, equal prefix sums (equal slopes) are still handled by the
  `<=` tie-breaks; strictly positive `w` here guarantees strict monotonicity.
