# Number of Distinct Islands

**Difficulty:** Medium

**Source:** LeetCode 694 — Number of Distinct Islands

## Description

Given a binary `grid`, an island is a 4-directionally connected group of 1s. Two islands are the same if one can be translated (not rotated or reflected) to equal the other. Return the number of distinct island shapes.

## Examples

### Example 1

```
Input:  two identical 2x2 blocks
Output: 1
```

## Hint

Flood each island, record cells relative to its top-left, sort → a canonical shape tuple.
