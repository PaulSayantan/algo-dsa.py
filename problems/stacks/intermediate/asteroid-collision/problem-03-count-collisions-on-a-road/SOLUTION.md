# Count Collisions on a Road — Solution

## Optimal Approach

Run an asteroid-collision stack over the cars. A right-mover (`R`) is pushed as a
"live" car. When an `S` arrives, every `R` currently on top crashes into it
(each is one collision) and then the position becomes stationary. When an `L`
arrives, if the top is an `R` they meet head-on for `2` collisions, and the `L`
becomes stationary and continues to consume any further `R`s behind it (each `1`
more); an `L` against empty space or a leading run of `L`s simply drives off and
never collides. This mirrors a negative asteroid annihilating the positive pile,
tallying the destroyed cars.

### Reference implementation

```python
class Solution:
    def countCollisions(self, directions):
        stack = []
        collisions = 0
        for c in directions:
            if c == 'R':
                stack.append('R')
            elif c == 'S':
                while stack and stack[-1] == 'R':
                    stack.pop()
                    collisions += 1
                stack.append('S')
            else:  # 'L'
                if not stack or stack[-1] == 'L':
                    stack.append('L')
                elif stack[-1] == 'S':
                    collisions += 1
                    stack.append('S')
                else:  # top is 'R': head-on meeting
                    collisions += 2
                    stack.pop()
                    while stack and stack[-1] == 'R':
                        stack.pop()
                        collisions += 1
                    stack.append('S')
        return collisions
```
