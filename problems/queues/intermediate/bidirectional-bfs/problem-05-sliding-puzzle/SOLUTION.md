# Sliding Puzzle — Solution

## Optimal Approach

Represent a board as a flat 6-tuple indexed `0..5`; the empty square is the value `0`.
Precompute, for each index, which indices are orthogonally adjacent on the 2x3 grid — those
are the tiles `0` can swap with. Run BFS from both the start state and the solved goal
`(1, 2, 3, 4, 5, 0)`, always expanding the smaller frontier (swapping the visited sets with
the frontiers). When a generated neighbor already sits in the opposite frontier the two
searches meet and the accumulated step count is the answer; if the frontiers drain without
meeting, the puzzle is unsolvable, so return `-1`.

### Reference implementation

```python
class Solution:
    def slidingPuzzle(self, board):
        start = tuple(board[0] + board[1])
        goal = (1, 2, 3, 4, 5, 0)
        if start == goal:
            return 0
        adj = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5),
               3: (0, 4), 4: (1, 3, 5), 5: (2, 4)}

        def neighbors(state):
            z = state.index(0)
            res = []
            for n in adj[z]:
                lst = list(state)
                lst[z], lst[n] = lst[n], lst[z]
                res.append(tuple(lst))
            return res

        front, back = {start}, {goal}
        visited_f, visited_b = {start}, {goal}
        steps = 0
        while front and back:
            if len(front) > len(back):
                front, back = back, front
                visited_f, visited_b = visited_b, visited_f
            steps += 1
            nxt = set()
            for state in front:
                for nb in neighbors(state):
                    if nb in back:
                        return steps
                    if nb not in visited_f:
                        visited_f.add(nb)
                        nxt.add(nb)
            front = nxt
        return -1
```
