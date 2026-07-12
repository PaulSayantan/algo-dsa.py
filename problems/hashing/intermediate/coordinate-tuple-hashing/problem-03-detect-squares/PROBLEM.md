# Detect Squares

**Difficulty:** Medium

**Source:** LeetCode 2013 — Detect Squares (design)

## Description

Design a data structure that accepts a stream of points and can count axis-aligned squares formed with a query point. `add(point)` adds a point (duplicates allowed); `count(point)` returns the number of squares with positive area having `point` as one corner and three previously added points as the others.

## Examples

### Example 1

```
Input:  add [3,10],[11,2],[3,2]; count [11,10]
Output: 1
```

## Hint

For each stored diagonal corner (equal |dx|=|dy|), multiply counts of the two other corners.
