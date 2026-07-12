# Rearrange String k Distance Apart

**Difficulty:** Medium

**Source:** LeetCode 358 — Rearrange String k Distance Apart

## Description

Given a string `s` and an integer `k`, rearrange the characters so that any two equal characters are at least `k` apart. Return any valid rearrangement, or `""` if none exists. When `k == 0` there is no separation requirement, so `s` itself is valid.

Constraints: `1 <= len(s) <= 3 * 10^5`, `0 <= k <= len(s)`, `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "aabbcc", k = 3
Output: "abcabc"
```

**Explanation:** Each repeated character is exactly 3 positions apart.

### Example 2

```
Input:  s = "aaabc", k = 3
Output: ""
```

**Explanation:** Three `a`s cannot all be kept 3 apart within a length-5 string.

## Hint

Generalized cooldown of length `k`: greedily emit the most frequent available character and push it into a FIFO cooldown queue; a character only becomes eligible again once `k` characters have been placed after it.
