# Check if a String is a Lyndon Word

**Difficulty:** Easy

**Source:** Classic string / competitive-programming warm-up (definition from the Chen–Fox–Lyndon theorem)

## Description

A **Lyndon word** is a non-empty string that is *strictly* smaller than every one of
its proper (non-empty) suffixes when compared lexicographically. Equivalently, it is
strictly smaller than all of its non-trivial rotations, and it cannot be written as a
power `t^m` of a shorter string with `m >= 2`.

Given a string `s`, determine whether `s` is a Lyndon word. Return `True` if it is and
`False` otherwise.

Examples of Lyndon words: `"a"`, `"ab"`, `"aab"`, `"abc"`, `"aabb"`.
Examples that are **not** Lyndon words: `"aa"` (equal to a rotation), `"ba"` (suffix
`"a"` is smaller), `"abab"` (a square), `"aba"` (suffix `"a"` is smaller).

## Constraints

- `1 <= len(s) <= 10^5`
- `s` consists of lowercase English letters.

## Examples

### Example 1
```
Input:  s = "aab"
Output: True
Explanation: The proper suffixes are "ab" and "b". Both "ab" > "aab" and "b" > "aab",
             so "aab" is strictly smaller than every proper suffix -> it is a Lyndon word.
```

### Example 2
```
Input:  s = "abab"
Output: False
Explanation: "abab" = ("ab")^2 is a square, and its suffix "ab" is a prefix (hence
             "ab" < "abab" is false in the strict-suffix sense; "abab" is not strictly
             smaller than all rotations). It is not a Lyndon word.
```

### Example 3
```
Input:  s = "b"
Output: True
Explanation: A single character has no proper suffix, so it is vacuously a Lyndon word.
```

## Hint

Run **Lyndon Factorization (Duval's algorithm)** on `s`: the string is a Lyndon word
exactly when Duval produces a single factor equal to the whole string.
