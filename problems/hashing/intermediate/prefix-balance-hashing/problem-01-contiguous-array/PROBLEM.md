# Contiguous Array

**Difficulty:** Medium

**Source:** LeetCode 525 — Contiguous Array

## Description

Given a binary array `nums`, return the length of the longest contiguous subarray with an equal number of `0`s and `1`s. Map `0` to `-1` and `1` to `+1`; the running balance repeats at the two ends of every balanced window, so track the earliest index of each balance value.

## Examples

### Example 1

```
Input:  nums = [0,1]
Output: 2
```

**Explanation:** [0,1] has one 0 and one 1.

### Example 2

```
Input:  nums = [0,1,0]
Output: 2
```

**Explanation:** [0,1] or [1,0] is the longest balanced window.

## Hint

Seed first = {0: -1}; record each balance only the first time so the window is as long as possible.
