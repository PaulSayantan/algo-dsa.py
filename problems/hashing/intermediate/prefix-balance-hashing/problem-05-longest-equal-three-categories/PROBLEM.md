# Longest Subarray With Equal Counts of Three Categories

**Difficulty:** Medium

**Source:** Classic — equal counts of three categories (difference-tuple hashing)

## Description

Given an array `nums` whose values are all `0`, `1`, or `2`, return the length of the longest contiguous subarray in which the three categories occur an equal number of times. A single scalar cannot capture 'all three equal', so key each prefix by the difference tuple `(c0 - c1, c1 - c2)` and store the earliest index of each tuple — two prefixes share the tuple exactly when the span between them is perfectly balanced.

## Examples

### Example 1

```
Input:  nums = [0,1,2,0,1,2]
Output: 6
```

**Explanation:** Two of each category across the whole array.

### Example 2

```
Input:  nums = [0,0,1,2]
Output: 3
```

**Explanation:** The window [0,1,2] has one of each category.

## Hint

Track counts of 0/1/2; hash the tuple (c0 - c1, c1 - c2) with earliest index, seeding {(0, 0): -1}.
