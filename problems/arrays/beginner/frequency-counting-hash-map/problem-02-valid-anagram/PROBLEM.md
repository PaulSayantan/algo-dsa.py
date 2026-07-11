# Valid Anagram

**Difficulty:** Easy

**Source:** LeetCode 242 (https://leetcode.com/problems/valid-anagram/)

## Description

Given two strings `s` and `t`, return `true` if `t` is an **anagram** of `s`,
and `false` otherwise.

An anagram is a word or phrase formed by rearranging the letters of another,
using all the original letters exactly once. In other words, `s` and `t` are
anagrams if and only if they contain the same characters with the same
multiplicities (counts), regardless of order.

This problem is a natural fit for frequency counting: two strings are anagrams
precisely when their character-frequency tables are identical.

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "anagram", t = "nagaram"
Output: true
Explanation: Both strings contain a:3, n:1, g:1, r:1, m:1, so t is a
rearrangement of s.
```

### Example 2

```
Input:  s = "rat", t = "car"
Output: false
Explanation: s has a 't' and no 'c', while t has a 'c' and no 't', so the
frequency tables differ.
```

### Example 3

```
Input:  s = "ab", t = "a"
Output: false
Explanation: The strings have different lengths, so they cannot contain the
same multiset of characters.
```

## Hint

Use **Frequency Counting with a Hash Map**: build a character count for `s`,
then verify `t` consumes exactly those counts (or compare the two count tables).
