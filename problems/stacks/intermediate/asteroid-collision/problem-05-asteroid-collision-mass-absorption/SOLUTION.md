# Asteroid Collision with Mass Absorption — Solution

## Optimal Approach

Keep a stack of surviving asteroids, exactly like standard asteroid collision.
Only a negative (left-moving) asteroid can collide, and only with a positive
(right-moving) asteroid on top of the stack.

For each incoming asteroid `a`, while it is left-moving and the stack top is
right-moving, resolve the head-on collision:

- **top < -a** — the incoming left-mover is bigger. Pop the top, add its mass to
  `a` (`a -= top`, which grows `a`'s magnitude while it stays negative), and keep
  fighting the next survivor.
- **top == -a** — equal magnitudes. Pop the top and destroy `a` too; nobody
  survives this pair.
- **top > -a** — the right-mover on top is bigger. It survives and absorbs the
  incoming mass, so its magnitude grows by `-a`; the incoming asteroid dies.

If the asteroid is still alive after the loop (it never met an opposing asteroid,
or it out-massed everything it hit), push it. Mass is conserved: the total
absolute magnitude of survivors equals the input total minus any equal-magnitude
pairs that mutually annihilated. Runs in O(n) time and O(n) space.

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
                    a -= top            # left-mover survives and absorbs the mass
                    continue
                elif top == -a:
                    stack.pop()         # equal magnitudes: both explode
                    alive = False
                else:
                    stack[-1] = top - a  # right-mover survives, absorbs (-a > 0)
                    alive = False
            if alive:
                stack.append(a)
        return stack
```
