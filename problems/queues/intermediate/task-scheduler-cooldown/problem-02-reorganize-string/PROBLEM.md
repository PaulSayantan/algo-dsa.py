# Reorganize String

**Difficulty:** Medium

**Source:** LeetCode 767 — Reorganize String

## Description

Given a string `s`, rearrange its characters so that no two adjacent characters are the same. Return any valid rearrangement, or `""` if it is impossible.

Constraints: `1 <= len(s) <= 500`, `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "aab"
Output: "aba"
```

**Explanation:** Placing the most frequent character (`a`) into alternating slots keeps equal characters apart.

### Example 2

```
Input:  s = "aaab"
Output: ""
```

**Explanation:** `a` appears 3 times in a length-4 string, exceeding `(4 + 1) // 2 = 2`, so no valid arrangement exists.

## Hint

This is cooldown with `n = 1`: always emit the most frequent available character, then hold it back one slot (a one-step cooldown) before it may be used again.
