# Perfect Squares (BFS) — Solution

## Brute Force

Try every partition recursively (`numSquares(n) = 1 + min(numSquares(n - sq))` over
all squares `sq <= n`). Without memoization this is exponential and recomputes the
same subproblems repeatedly.

## Optimal Approach

Model it as an unweighted shortest-path problem. A state is a remaining amount; from
`rem` you can move to `rem - sq` for each perfect square `sq <= rem`, and each such
move costs one term. BFS layer by layer from `n`: the first time we reach `0`, the
current depth is the minimum count of perfect squares. A `visited` set over remaining
amounts prevents re-exploring the same value, keeping the search polynomial.

### Reference implementation

```python
class Solution:
    def numSquares(self, n):
        if n <= 0:
            return 0
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        q = deque([(n, 0)])
        seen = {n}
        while q:
            rem, steps = q.popleft()
            if rem == 0:
                return steps
            for sq in squares:
                if sq > rem:
                    break
                nxt = rem - sq
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, steps + 1))
        return -1
```
