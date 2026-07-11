# One Edit Distance

**Difficulty:** Easy/Medium

**Source:** LeetCode 161 — One Edit Distance

## Description

Given two strings `s` and `t`, return `true` if they are **exactly one edit
distance apart**, otherwise return `false`.

A string `s` is said to be one edit distance apart from a string `t` if you can
convert `s` into `t` (or `t` into `s`) with exactly **one** of the following
single-character operations:

- **Insert** exactly one character into `s`.
- **Delete** exactly one character from `s`.
- **Replace** exactly one character of `s` with a different character.

Note that "exactly one" is strict: two identical strings are **zero** edits
apart, so the answer for equal strings is `false`.

## Constraints

- `0 <= s.length, t.length <= 10^4`
- `s` and `t` consist of lowercase letters, uppercase letters, and/or digits.

## Examples

### Example 1

```
Input:  s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t. That is exactly one insertion.
```

### Example 2

```
Input:  s = "cab", t = "ad"
Output: false
Explanation: The strings differ by more than one edit. Turning "cab" into "ad"
requires at least two operations, so they are not one edit apart.
```

### Example 3

```
Input:  s = "1203", t = "1213"
Output: true
Explanation: Replacing the '0' in s with '1' yields t. That is exactly one
replacement.
```

### Example 4

```
Input:  s = "abc", t = "abc"
Output: false
Explanation: The strings are identical, so they are zero edits apart, not one.
```

## Hint

This is a constrained form of **Edit Distance (Levenshtein)**: instead of
computing the full distance, you only need to verify it equals exactly 1. Think
about how the lengths of `s` and `t` limit which single operation is even
possible, then scan for the first mismatch.
