# Jump Game IV — Solution

## Optimal Approach

Treat each array index as a node. Node `i` is adjacent to `i - 1`, `i + 1`, and every
other index holding the same value. Because adjacency is symmetric, BFS can run from both
index `0` and the last index simultaneously, expanding whichever frontier is smaller each
round (this is what roughly square-roots the states explored). When a generated neighbor
already sits in the opposite frontier, the two searches meet and the accumulated step count
is the answer.

Two details keep it efficient and correct:

- Group indices by value up front (`groups[value] -> [indices]`). The first time a frontier
  expands any index with a given value, splice in the whole group, then mark that value as
  used so the (potentially large) group is never rescanned — otherwise a run of equal values
  makes the search quadratic. Each direction tracks its own used-value set, since the
  frontiers are swapped as they trade places.
- Track a visited set per direction so we never re-add an index to our own frontier.

`arr` of length 1 is already at the goal, so the answer is `0`.

### Reference implementation

```python
class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0
        groups = defaultdict(list)
        for i, x in enumerate(arr):
            groups[x].append(i)
        front, back = {0}, {n - 1}
        visited_f, visited_b = {0}, {n - 1}
        used_f, used_b = set(), set()
        steps = 0
        while front and back:
            if len(front) > len(back):
                front, back = back, front
                visited_f, visited_b = visited_b, visited_f
                used_f, used_b = used_b, used_f
            steps += 1
            nxt = set()
            for i in front:
                neighbors = []
                if i + 1 < n:
                    neighbors.append(i + 1)
                if i - 1 >= 0:
                    neighbors.append(i - 1)
                v = arr[i]
                if v not in used_f:
                    used_f.add(v)
                    neighbors.extend(groups[v])
                for nb in neighbors:
                    if nb in back:
                        return steps
                    if nb not in visited_f:
                        visited_f.add(nb)
                        nxt.add(nb)
            front = nxt
        return -1
```
