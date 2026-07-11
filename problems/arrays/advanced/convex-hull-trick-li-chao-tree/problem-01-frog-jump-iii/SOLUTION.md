# Frog Jump III — Solution

## Brute Force

Compute the recurrence directly:

```
dp[0] = 0
for j in 1 .. N-1:
    dp[j] = min over i < j of ( dp[i] + (h[i] - h[j])^2 + C )
answer = dp[N-1]
```

- **Time:** `O(N^2)` — for each of `N` stones we scan all earlier stones.
- **Space:** `O(N)` for the `dp` array.

With `N` up to `2 * 10^5` this is about `4 * 10^10` operations — far too slow.

## Optimal Approach — Monotonic Convex Hull Trick

### Rewrite the transition as a minimum over lines

Expand the square:

```
dp[j] = min_i ( dp[i] + h[i]^2 - 2 h[i] h[j] + h[j]^2 + C )
      = h[j]^2 + C + min_i ( (-2 h[i]) * h[j] + (dp[i] + h[i]^2) )
```

The `i`-only quantities are the coefficients of a line

```
line_i(x) = m_i * x + b_i,   where m_i = -2 h[i],   b_i = dp[i] + h[i]^2
```

and we evaluate it at the query point `x = h[j]`. So

```
dp[j] = h[j]^2 + C + min_i line_i(h[j]).
```

We add stones left to right: before computing `dp[j]` all lines for `i < j` already
exist, which is exactly the set we minimize over.

### Why a monotonic hull works here

Only lines lying on the **lower envelope** (lower hull) can ever be the minimum at
some `x`. Two special monotonicities make this cheap:

1. **Slopes are strictly decreasing.** `m_i = -2 h[i]` and `h` is strictly
   increasing, so each new slope is smaller than the previous one. New lines can be
   appended to the back of a deque, popping lines that become redundant.
2. **Query points are strictly increasing.** We query at `x = h[j]` with `h`
   increasing. The index of the optimal line only moves forward, so a single pointer
   sweeps across the hull; it never needs to move back.

Both operations are amortized `O(1)`, giving an `O(N)` algorithm.

### Removing a redundant line

Keep lines `L1, L2, L3` on the hull (in insertion order). `L2` is redundant — never
minimal for any `x` — when the intersection of `L1` and `L3` lies at or to the left
of the intersection of `L1` and `L2`. Using integer cross-multiplication to avoid
floating point (with `L = (m, b)`):

```
bad(L1, L2, L3):
    return (b3 - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m3)
```

Pop `L2` while `bad` holds, then push the new line.

### Reference implementation

```python
from typing import List

def min_total_cost(heights: List[int], c: int) -> int:
    slopes: List[int] = []      # m values on the hull, decreasing
    intercepts: List[int] = []  # matching b values
    ptr = 0                     # moving pointer for increasing queries

    def bad(m1, b1, m2, b2, m3, b3) -> bool:
        # is the middle line (m2,b2) redundant given neighbours 1 and 3?
        return (b3 - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m3)

    def add_line(m: int, b: int) -> None:
        while len(slopes) >= 2 and bad(slopes[-2], intercepts[-2],
                                       slopes[-1], intercepts[-1], m, b):
            slopes.pop(); intercepts.pop()
        slopes.append(m); intercepts.append(b)

    def query(x: int) -> int:
        nonlocal ptr
        if ptr >= len(slopes):
            ptr = len(slopes) - 1
        while ptr + 1 < len(slopes) and \
              slopes[ptr + 1] * x + intercepts[ptr + 1] <= slopes[ptr] * x + intercepts[ptr]:
            ptr += 1
        return slopes[ptr] * x + intercepts[ptr]

    n = len(heights)
    dp = [0] * n
    add_line(-2 * heights[0], dp[0] + heights[0] ** 2)
    for j in range(1, n):
        dp[j] = query(heights[j]) + heights[j] ** 2 + c
        add_line(-2 * heights[j], dp[j] + heights[j] ** 2)
    return dp[n - 1]
```

- **Time:** `O(N)` — each line is pushed and popped at most once, and the query
  pointer only advances.
- **Space:** `O(N)` for the hull and `dp` array.

## Key Insights & Edge Cases

- **The algebra is the whole trick.** Any cost with a `-2 h[i] h[j]` cross term
  splits into an `i`-line evaluated at an `i`-independent query point.
- **Integers only.** Comparing intercept intersections with cross-multiplication
  (never division) avoids floating-point error; values stay well within 64-bit.
- **Strictly increasing heights are what guarantee monotone slopes.** If heights
  were not sorted, slopes would not be monotone and you would need the binary-search
  CHT or a Li Chao Tree (see Problem 5).
- **`N = 2`:** the loop runs once, the answer is the single jump
  `(h[0] - h[1])^2 + C` — handled naturally.
- **The `+C` toll and `h[j]^2` are `i`-independent**, so they are added *after* the
  minimization, not inside the lines.
