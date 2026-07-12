# Remove All Adjacent Duplicates In String

**Difficulty:** Easy

**Source:** LeetCode 1047 — Remove All Adjacent Duplicates In String

## Description

Given a string `s` of lowercase letters, repeatedly remove two adjacent equal letters. Keep doing this until no adjacent duplicates remain, and return the final string (the result is unique).

## Examples

### Example 1

```
Input:  s = "abbaca"
Output: "ca"
```

**Explanation:** Remove 'bb' -> 'aaca', remove 'aa' -> 'ca'.

## Hint

Push each char; if it equals the stack top, pop instead of pushing.
