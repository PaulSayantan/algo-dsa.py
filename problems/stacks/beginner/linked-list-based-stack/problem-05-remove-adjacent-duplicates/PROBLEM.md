# Remove All Adjacent Duplicates In String

**Difficulty:** Easy

**Source:** LeetCode 1047 — Remove All Adjacent Duplicates In String

## Description

Given a string `s` of lowercase English letters, repeatedly remove any two **adjacent and equal** letters. Keep removing until no such adjacent pair remains, then return the final string. The answer is unique.

Constraints: `1 <= len(s) <= 10^5`; `s` consists of lowercase English letters only.

## Examples

### Example 1

```
Input:  s = "abbaca"
Output: 'ca'
```

**Explanation:** Remove the adjacent `"bb"` to get `"aaca"`, then remove the adjacent `"aa"` to get `"ca"`, which has no adjacent duplicates.

### Example 2

```
Input:  s = "azxxzy"
Output: 'ay'
```

**Explanation:** Remove `"xx"` -> `"azzy"`, then `"zz"` -> `"ay"`.

## Hint

Push each character onto a linked-list stack; if the incoming character equals the head, pop instead of pushing. The stack, read bottom-to-top, is the answer.
