# First Unique Character in a String

**Difficulty:** Easy

**Source:** LeetCode 387 — First Unique Character in a String

## Description

Given a string `s`, return the index of the first character that appears exactly once. If no such character exists, return `-1`.

## Examples

### Example 1

```
Input:  s = "leetcode"
Output: 0
```

**Explanation:** 'l' is the first character that appears only once.

### Example 2

```
Input:  s = "loveleetcode"
Output: 2
```

**Explanation:** 'v' at index 2 is the first unique character.

## Hint

Count all characters first, then scan left-to-right for the first with count 1.
