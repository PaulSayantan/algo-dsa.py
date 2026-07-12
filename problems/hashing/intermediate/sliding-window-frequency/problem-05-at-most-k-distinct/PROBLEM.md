# Longest Substring with At Most K Distinct Characters

**Difficulty:** Medium

**Source:** LeetCode 340 — Longest Substring with At Most K Distinct Characters

## Description

Given a string `s` and an integer `k`, return the length of the longest substring that contains at most `k` distinct characters. This generalises the two-distinct case; `k = 0` yields `0`.

## Examples

### Example 1

```
Input:  s = "eceba", k = 2
Output: 3
```

**Explanation:** "ece" has 2 distinct characters and length 3.

## Hint

Same window, invariant len(count) <= k; evict left chars until the map has <= k keys.
