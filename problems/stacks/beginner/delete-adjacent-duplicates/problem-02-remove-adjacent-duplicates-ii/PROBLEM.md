# Remove All Adjacent Duplicates in String II

**Difficulty:** Medium

**Source:** LeetCode 1209 — Remove All Adjacent Duplicates in String II

## Description

Given a string `s` and an integer `k`, repeatedly remove `k` adjacent equal letters until no such group remains, and return the final string. The answer is unique.

## Examples

### Example 1

```
Input:  s = "deeedbbcccbdaa", k = 3
Output: "aa"
```

## Hint

Stack of [char, count]; increment on match, pop when count hits k.
