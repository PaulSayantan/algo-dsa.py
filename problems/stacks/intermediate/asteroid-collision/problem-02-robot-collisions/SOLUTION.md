# Robot Collisions — Solution

## Optimal Approach

Process robots left-to-right by position. Right-moving robots wait on a stack.
A left-moving robot fights the survivors on the stack one at a time — identical
to a negative asteroid annihilating smaller positive asteroids — losing 1 health
per weaker opponent it destroys, dying against a stronger one, and mutually
destroying an equal one. Answers are re-ordered back to the original indices.

### Reference implementation

```python
class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        order = sorted(range(n), key=lambda i: positions[i])
        health = list(healths)
        stack = []  # indices of surviving right-moving robots
        for i in order:
            if directions[i] == 'R':
                stack.append(i)
                continue
            while stack and health[i] > 0:
                j = stack[-1]
                if health[j] < health[i]:
                    health[j] = 0
                    stack.pop()
                    health[i] -= 1
                elif health[j] > health[i]:
                    health[j] -= 1
                    health[i] = 0
                else:
                    health[j] = 0
                    health[i] = 0
                    stack.pop()
        return [h for h in (health[i] for i in range(n)) if h > 0]
```
