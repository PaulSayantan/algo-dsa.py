# Asteroid Collision with Mass Absorption

**Difficulty:** Medium

**Source:** Classic — Asteroid Collision, mass-absorption variant (of LeetCode 735)

## Description

Given `asteroids` (each a non-zero integer: magnitude = absolute value, sign = direction, `+` right and `-` left), simulate their collisions moving left to right and return the state after everything settles.

Collisions differ from the standard problem: mass is conserved. When two asteroids move toward each other (a right-mover to the left of a left-mover),

- if their magnitudes are **equal**, both explode and neither survives;
- otherwise the **larger** one survives but **absorbs the mass** of the one it destroys, so its magnitude grows by the destroyed asteroid's magnitude (its direction is unchanged).

Two asteroids moving the same way never collide. A left-moving asteroid that survives keeps plowing leftward, absorbing every smaller right-mover it overtakes.

## Examples

### Example 1

```
Input:  asteroids = [5,10,-5]
Output: [5, 15]
```

**Explanation:** The `-5` meets the `10`. Since `10 > 5`, the right-mover survives and absorbs the left-mover's mass, growing to `15`. The `5` at the bottom never gets hit.

### Example 2

```
Input:  asteroids = [4,-1,-2,-8]
Output: [-15]
```

**Explanation:** The `4` absorbs the `-1` (grows to `5`), then absorbs the `-2` (grows to `7`). The `-8` is larger than `7`, so the left-mover survives and absorbs the `7`, becoming `-15`.

### Example 3

```
Input:  asteroids = [8,-8]
Output: []
```

**Explanation:** Equal magnitudes moving toward each other — both explode.

## Hint

Use a stack of survivors just like standard asteroid collision, but when the survivor is bigger, add the destroyed asteroid's magnitude to it instead of discarding it; when the left-mover wins, let its magnitude accumulate the masses it destroys as it keeps popping.
