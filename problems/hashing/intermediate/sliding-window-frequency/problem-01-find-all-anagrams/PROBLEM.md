# Find All Anagrams in a String

**Difficulty:** Medium

**Source:** LeetCode 438 — Find All Anagrams in a String

## Description

Given strings `s` and `p`, return the start indices of every substring of `s` that is an anagram of `p`. A substring is an anagram of `p` iff it has the exact same multiset of characters. Return the indices in ascending order (they arise naturally in left-to-right scan order).

## Examples

### Example 1

```
Input:  s = "cbaebabacd", p = "abc"
Output: [0, 6]
```

**Explanation:** The substrings "cba" (index 0) and "bac" (index 6) are anagrams of "abc".

### Example 2

```
Input:  s = "abab", p = "ab"
Output: [0, 1, 2]
```

## Hint

Slide a window of length len(p); keep its Counter equal-checked against Counter(p).
