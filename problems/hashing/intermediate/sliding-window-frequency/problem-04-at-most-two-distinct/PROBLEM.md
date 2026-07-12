# Longest Substring with At Most Two Distinct Characters

**Difficulty:** Medium

**Source:** LeetCode 159 — Longest Substring with At Most Two Distinct Characters

## Description

Given a string `s`, return the length of the longest substring that contains at most two distinct characters. Grow a window and shrink it from the left whenever the frequency map holds more than two keys.

## Examples

### Example 1

```
Input:  s = "eceba"
Output: 3
```

**Explanation:** "ece" has two distinct characters and length 3.

### Example 2

```
Input:  s = "ccaabbb"
Output: 5
```

**Explanation:** "aabbb" has two distinct characters and length 5.

## Hint

defaultdict counts; while len(count) > 2, decrement/evict the left char and advance left.
