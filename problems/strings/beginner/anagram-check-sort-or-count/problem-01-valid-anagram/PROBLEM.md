# Valid Anagram

**Difficulty:** Easy

Source: LeetCode 242 — Valid Anagram

## Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and
`false` otherwise.

An **anagram** is a word or phrase formed by rearranging the letters of a different
word or phrase, using all the original letters exactly once. In other words, `t` is
an anagram of `s` when both strings have the same length and contain exactly the same
characters with the same multiplicities.

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

Follow-up: What if the inputs contain Unicode characters? How would you adapt your
solution?

## Examples

### Example 1

```
Input:  s = "anagram", t = "nagaram"
Output: true
Explanation: Both strings use the letters a×3, n×1, g×1, r×1, m×1, so one is a
rearrangement of the other.
```

### Example 2

```
Input:  s = "rat", t = "car"
Output: false
Explanation: The strings have the same length but different letters ('t' vs 'c'),
so t cannot be a rearrangement of s.
```

### Example 3

```
Input:  s = "a", t = "ab"
Output: false
Explanation: The lengths differ (1 vs 2), so t cannot be an anagram of s.
```

## Hint

Use an **Anagram Check (sort or count)**: either sort both strings and compare, or
build a per-character frequency table for each string and check that the tables match.
