# Max Value of Equation — Solution

## Brute Force

Try every pair `(i, j)` with `i < j`, skip those violating `x_j - x_i <= k`, and
track the maximum of `y_i + y_j + (x_j - x_i)`.

```python
def brute(points, k):
    best = float("-inf")
    n = len(points)
    for i in range(n):
        xi, yi = points[i]
        for j in range(i + 1, n):
            xj, yj = points[j]
            if xj - xi > k:
                break            # points sorted by x -> no further j works
            best = max(best, yi + yj + (xj - xi))
    return best
```

- **Time:** `O(n^2)` in the worst case (large `k`).
- **Space:** `O(1)`.

## Optimal Approach (Monotonic Deque)

Since the points are sorted by x and `i < j`, `x_i < x_j`, so
`|x_i - x_j| = x_j - x_i`. Rewrite the objective:

```
y_i + y_j + (x_j - x_i) = (y_j + x_j) + (y_i - x_i)
```

For a **fixed right point `j`**, `(y_j + x_j)` is a constant. We only need the
maximum of `(y_i - x_i)` over earlier points `i` whose x is within the window
`x_i >= x_j - k`. That is a sliding-window maximum keyed by x-distance.

Maintain a deque of points (store `(x_i, y_i - x_i)`, or indices) so the stored
`y_i - x_i` values are **decreasing** front to back:

1. **Front-expiry.** While the deque front has `x_j - x_front > k`, it is out of
   range — `popleft`.
2. **Answer.** If the deque is non-empty, candidate value is
   `(y_j + x_j) + (front's y_i - x_i)`; update the best.
3. **Push.** Pop from the back while `dq[-1].(y - x) <= (y_j - x_j)`, then append
   the current point (it becomes a future `i`).

```python
from collections import deque

def optimal(points, k):
    dq = deque()          # (x, y - x), with (y - x) decreasing front -> back
    best = float("-inf")
    for x, y in points:
        while dq and x - dq[0][0] > k:      # front out of the x-window
            dq.popleft()
        if dq:
            best = max(best, x + y + dq[0][1])
        while dq and dq[-1][1] <= y - x:    # current point dominates the back
            dq.pop()
        dq.append((x, y - x))
    return best
```

### Why it is correct

Processing points left to right, when we reach point `j` every point already in
the deque has a smaller x (so it is a legal left endpoint `i` as long as it is
within `k`). Front-expiry removes points too far to the left. The deque keeps the
stored `y_i - x_i` decreasing, so its front is the best partner for `j`. A point
whose `y - x` is `<=` the newcomer's is dominated — the newcomer has a larger (or
equal) `y - x` **and** a larger x (closer to future right points, so it stays in
range longer) — hence it can be discarded from the back.

### Step-by-step on `points = [[1,3],[2,0],[5,10],[6,-10]], k = 1`

Store `(x, y - x)`.

| point   | x | y   | y - x | front-expiry (x - front.x > 1) | answer update             | dq after            |
|---------|---|-----|-------|--------------------------------|---------------------------|---------------------|
| [1, 3]  | 1 | 3   | 2     | deque empty                    | none (empty)              | [(1, 2)]            |
| [2, 0]  | 2 | 0   | -2    | 2 - 1 = 1 > 1? no              | 2 + 0 + 2 = 4 -> best 4   | [(1,2),(2,-2)]      |
| [5, 10] | 5 | 10  | 5     | 5 - 1 = 4 > 1? pop (1,2); 5 - 2 = 3 > 1? pop (2,-2) | deque empty -> none | [(5, 5)]  |
| [6,-10] | 6 | -10 | -16   | 6 - 5 = 1 > 1? no              | 6 + (-10) + 5 = 1         | [(5,5),(6,-16)]     |

The best value seen is `4`, matching Example 1.

- **Time:** `O(n)` — each point enters and leaves the deque at most once.
- **Space:** `O(n)` worst case for the deque.

## Key Insights & Edge Cases

- The key algebraic move is splitting the objective into a `j`-only part
  (`y_j + x_j`) and an `i`-only part (`y_i - x_i`) so the deque can maximize the
  latter over the x-window.
- **Expire the front by x-distance**, not by index count — the window is defined
  by `x_j - x_i <= k`, and x-gaps between consecutive points vary.
- The problem guarantees at least one valid pair, so `best` is always updated;
  still, guard the answer step with a non-empty deque check (the first point has
  no earlier partner).
- Only read the deque front *after* expiry so you never pair with an out-of-range
  point.
- Coordinates reach `10^8` and `k` up to `2 * 10^8`; sums fit in 64-bit integers
  (and Python ints are unbounded).
