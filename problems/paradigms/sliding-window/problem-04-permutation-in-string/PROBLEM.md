# Permutation in String

**Difficulty:** Medium

**Source:** LeetCode 567 — Permutation in String

## Description

Given two strings `s1` and `s2`, return `true` if `s2` contains a **permutation** of
`s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations appears as a
**contiguous substring** of `s2`.

A permutation rearranges all the characters of `s1`; every character (with its
multiplicity) must be used exactly once.

## Constraints

- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains the substring "ba" (indices 3..4), which is a permutation
             of "ab".
```

### Example 2

```
Input:  s1 = "ab", s2 = "eidboaoo"
Output: false
Explanation: No contiguous length-2 window of s2 is a rearrangement of "ab"; the
             'a' and 'b' are never adjacent.
```

### Example 3

```
Input:  s1 = "adc", s2 = "dcda"
Output: true
Explanation: The window "dcd" is not a match, but "dca" (indices 1..3, letters
             d, c, a) is a permutation of "adc", so the answer is true.
```

## Hint

Use the **Sliding Window** technique with a fixed window size equal to `len(s1)`:
slide a window over `s2` and check whether its character frequencies match those of
`s1`, updating the counts incrementally rather than recounting each window.
