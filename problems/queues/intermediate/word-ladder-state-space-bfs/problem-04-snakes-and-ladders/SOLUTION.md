# Snakes and Ladders — Solution

## Optimal Approach

Each board square `1..n*n` is a state and a die roll is an unweighted edge to
`s+1 .. s+6`, so BFS yields the fewest rolls. The only subtlety is mapping a square
number back to a `(row, col)` in the boustrophedon layout: rows fill from the bottom
up, and every other row runs right-to-left. After landing, if the cell holds a value
other than `-1` we jump to that square (a single snake or ladder per move). A
`visited` set keyed by square number prevents revisits.

### Reference implementation

```python
class Solution:
    def snakesAndLadders(self, board):
        n = len(board)

        def cell(s):
            s -= 1
            row, col = divmod(s, n)
            if row % 2 == 1:
                col = n - 1 - col
            return n - 1 - row, col

        target = n * n
        q = deque([(1, 0)])
        seen = {1}
        while q:
            s, moves = q.popleft()
            if s == target:
                return moves
            for d in range(1, 7):
                nxt = s + d
                if nxt > target:
                    break
                r, c = cell(nxt)
                if board[r][c] != -1:
                    nxt = board[r][c]
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, moves + 1))
        return -1
```
