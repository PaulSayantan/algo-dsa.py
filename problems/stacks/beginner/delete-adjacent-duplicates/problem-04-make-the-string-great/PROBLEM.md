# Make The String Great

**Difficulty:** Easy

**Source:** LeetCode 1544 — Make The String Great

## Description

Given a string `s` of lowercase and uppercase English letters, make it *good* by repeatedly removing two adjacent characters that are the same letter in different cases (e.g. `'a'` next to `'A'`, or `'A'` next to `'a'`). Keep removing until no such adjacent pair remains and return the resulting good string. The answer is unique; it may be empty.

## Examples

### Example 1

```
Input:  s = "leEeetcode"
Output: "leetcode"
```

**Explanation:** `'eE'` is a bad pair, so remove it: `"leetcode"` — now good.

## Hint

Same adjacent-collapse as removing equal duplicates: push each char, but if it and the stack top are the same letter in opposite cases, pop instead.
