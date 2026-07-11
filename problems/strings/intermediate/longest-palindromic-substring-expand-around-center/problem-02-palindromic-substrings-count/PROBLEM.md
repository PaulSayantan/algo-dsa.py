# Palindromic Substrings

**Difficulty:** Medium

**Source:** LeetCode 647 — Palindromic Substrings

## Description

Given a string `s`, return *the number of palindromic substrings in it*.

A **substring** is a contiguous, non-empty sequence of characters within a
string. Two substrings are counted **separately** if they start or end at
different indices, even when they consist of the same characters. In other
words, count occurrences by position, not by distinct content.

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Examples

**Example 1**

```
Input:  s = "abc"
Output: 3
Explanation: Three palindromic substrings: "a", "b", "c".
```

**Example 2**

```
Input:  s = "aaa"
Output: 6
Explanation: Six palindromic substrings: "a", "a", "a", "aa", "aa", "aaa".
             Note the three single "a"s and the two "aa"s are counted by
             position, so they are all distinct occurrences.
```

**Example 3**

```
Input:  s = "aba"
Output: 4
Explanation: "a", "b", "a", and "aba" — four palindromic substrings.
```

## Hint

Every palindromic substring is anchored at one of the `2n - 1` centers. Use the
**Longest Palindromic Substring (expand around center)** technique, but instead
of tracking the longest, increment a counter by one for *each successful
expansion step* — every time the mirrored characters still match, you have found
one more palindrome centered there.
