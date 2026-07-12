# Asteroid Collision — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for a in asteroids:
            alive = True
            while alive and a < 0 and stack and stack[-1] > 0:
                top = stack[-1]
                if top < -a:
                    stack.pop()
                    continue
                elif top == -a:
                    stack.pop()
                alive = False
            if alive:
                stack.append(a)
        return stack
```
