# Snakes and Ladders — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def snakesAndLadders(self, board):
        n = len(board)

        def cell(sq):
            r, c = divmod(sq - 1, n)
            row = n - 1 - r
            col = c if r % 2 == 0 else n - 1 - c
            return row, col

        target = n * n
        seen = {1}
        q = deque([(1, 0)])
        while q:
            sq, moves = q.popleft()
            if sq == target:
                return moves
            for nxt in range(sq + 1, min(sq + 6, target) + 1):
                r, c = cell(nxt)
                dest = board[r][c] if board[r][c] != -1 else nxt
                if dest not in seen:
                    seen.add(dest)
                    q.append((dest, moves + 1))
        return -1
```
