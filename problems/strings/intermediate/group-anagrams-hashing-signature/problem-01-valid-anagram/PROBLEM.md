# Valid Anagram

**Difficulty:** Easy

**Source:** LeetCode 242 — Valid Anagram

## Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and
`false` otherwise.

An **anagram** is a word or phrase formed by rearranging the letters of a
different word or phrase, using all the original letters exactly once. In other
words, `t` is an anagram of `s` if and only if the two strings contain the exact
same multiset of characters (same characters with the same counts), regardless
of order.

This is the simplest use of a **hashing signature**: instead of grouping many
strings, you just build the character-count signature of each string and check
whether the two signatures are identical.

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "anagram", t = "nagaram"
Output: true
Explanation: Both strings use the letters a:3, n:1, g:1, r:1, m:1, so their
count signatures are identical.
```

### Example 2

```
Input:  s = "rat", t = "car"
Output: false
Explanation: s has {r:1, a:1, t:1} while t has {c:1, a:1, r:1}. The 't' vs 'c'
mismatch means the signatures differ, so they are not anagrams.
```

### Example 3

```
Input:  s = "a", t = "ab"
Output: false
Explanation: Different lengths cannot share the same character multiset, so the
answer is false.
```

## Hint

Reduce each string to a canonical **Group Anagrams (hashing signature)** — either
a sorted string or a length-26 character-count tuple — and compare the two
signatures for equality.
