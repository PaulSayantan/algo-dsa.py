# Sum of the Longest Consecutive Run

**Difficulty:** Medium

**Source:** Classic — sum over the longest band of consecutive numbers

## Description

Given an integer array `nums`, find the longest run of consecutive integers (smallest start on ties) and return the sum of that run's values. Return `0` for empty input.

## Examples

### Example 1

```
Input:  nums = [100,4,200,1,3,2]
Output: 10
```

**Explanation:** Longest run [1,2,3,4] sums to 10.

### Example 2

```
Input:  nums = [5,6,1,2,3]
Output: 6
```

**Explanation:** {1,2,3} (length 3) is longer than {5,6}, and sums to 6.

## Hint

Same run-start scan; when a strictly longer run is found, record the sum of its range.
