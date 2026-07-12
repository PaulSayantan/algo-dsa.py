# Count Maximal Consecutive Runs

**Difficulty:** Easy

**Source:** Classic — number of consecutive-sequence runs in a set

## Description

Given an integer array `nums`, return the number of maximal runs of consecutive integers among its distinct values. For example the distinct set `{1,2,3,10,11,20}` splits into the runs `{1,2,3}`, `{10,11}`, `{20}` — three runs.

## Examples

### Example 1

```
Input:  nums = [1,2,3,10,11,20]
Output: 3
```

**Explanation:** Runs: {1,2,3}, {10,11}, {20}.

## Hint

A run-start is any value x with x-1 absent; the number of run-starts equals the number of runs.
