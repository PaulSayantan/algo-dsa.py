# Asteroid Collision

**Difficulty:** Medium

**Source:** LeetCode 735 — Asteroid Collision

## Description

Given `asteroids` (each a non-zero integer: magnitude = absolute value, sign = direction, `+` right and `-` left), simulate their collisions and return the state after all collisions. Two asteroids moving toward each other: the smaller explodes; equal magnitudes both explode; same direction never collide.

## Examples

### Example 1

```
Input:  asteroids = [5,10,-5]
Output: [5,10]
```

## Hint

Stack of survivors; a negative asteroid pops smaller positives, cancels equal, or dies.
