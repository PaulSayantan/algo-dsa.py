# Permutation in String

**Difficulty:** Medium

**Source:** LeetCode 567 — Permutation in String

## Description

Given two strings `s1` and `s2`, return `True` if `s2` contains a **permutation
of `s1`** as a substring, and `False` otherwise.

In other words, return `True` if some contiguous substring of `s2` uses exactly
the same characters as `s1` with exactly the same multiplicities (an anagram of
`s1`). Since a permutation of `s1` always has length `len(s1)`, you are looking
for a length-`len(s1)` window of `s2` whose character counts match `s1`'s.

## Constraints

- `1 <= len(s1), len(s2) <= 10^4`
- `s1` and `s2` consist of lowercase English letters.

## Examples

### Example 1
```
Input:  s1 = "ab", s2 = "eidbaooo"
Output: True
Explanation: s2 contains the substring "ba" (indices 3..4), which is a
             permutation of "ab".
```

### Example 2
```
Input:  s1 = "ab", s2 = "eidboaoo"
Output: False
Explanation: No length-2 window of s2 equals a permutation of "ab". The 'a'
             and 'b' in s2 are separated by 'o', so they never sit adjacent.
```

### Example 3
```
Input:  s1 = "adc", s2 = "dcda"
Output: True
Explanation: The window "dcd" is not a match, but "cda" (indices 1..3) uses
             the same letters as "adc", so it is a permutation.
```

## Hint

Use the **Sliding Window on Strings** technique with a **fixed-size** window of
length `len(s1)`: maintain character counts for the window, slide it one step
at a time (add the entering character, remove the leaving one), and report
success whenever the window's counts equal `s1`'s counts.
