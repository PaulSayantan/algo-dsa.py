# Perfect Squares — Solution

## Optimal Approach

Treat every attainable running total in `0..n` as a node, with an edge from `t`
to `t + s` for each perfect square `s <= n - t`. Every edge has weight one, so
the minimum number of squares that sum to `n` is the shortest-path length from
`0` to `n` — exactly what BFS computes. Process the queue level by level: each
level corresponds to using one more square, so the first level at which `n`
appears is the answer. A `visited` set keeps each total from being expanded more
than once, giving O(n·√n) time.

### Reference implementation

```python
class Solution:
    def numSquares(self, n):
        if n == 0:
            return 0
        squares = [i * i for i in range(1, math.isqrt(n) + 1)]
        visited = {0}
        q = deque([0])
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for s in squares:
                    nxt = cur + s
                    if nxt == n:
                        return level
                    if nxt < n and nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
        return level
```
