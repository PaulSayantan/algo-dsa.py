# Valid Anagram

**Difficulty:** Easy

**Source:** LeetCode 242 — Valid Anagram

## Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and
`false` otherwise.

An **anagram** is a word or phrase formed by rearranging the letters of a
different word or phrase, using all the original letters exactly once. In other
words, `t` is an anagram of `s` if and only if both strings have exactly the same
characters with exactly the same counts (order does not matter).

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "anagram", t = "nagaram"
Output: true
Explanation: Both strings use the letters a x3, n x1, g x1, r x1, m x1. The counts
             match exactly, so t is a rearrangement of s.
```

### Example 2

```
Input:  s = "rat", t = "car"
Output: false
Explanation: s has an 'a' and 't' while t has a 'c' and 'r'. The letter multisets
             differ ('t' vs 'c'), so t is not an anagram of s.
```

### Example 3

```
Input:  s = "a", t = "ab"
Output: false
Explanation: The strings have different lengths (1 vs 2), so they cannot contain
             the same multiset of characters.
```

## Hint

Two strings are anagrams exactly when they have identical character counts. Use a
**Character Frequency Count** over the 26 lowercase letters: tally one string,
then check the other against that tally.
