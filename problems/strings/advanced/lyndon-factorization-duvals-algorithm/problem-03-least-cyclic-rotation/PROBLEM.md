# Lexicographically Smallest Rotation

**Difficulty:** Medium

**Source:** SPOJ MINMOVE / "Booking" / classic necklace-canonicalization problem

## Description

A **rotation** (cyclic shift) of a string `s` of length `n` by `d` positions is
`s[d:] + s[:d]`. There are `n` rotations (for `d = 0, 1, ..., n-1`).

Given a string `s`, return its **lexicographically smallest** rotation.

For example, the rotations of `"baca"` are `"baca"`, `"acab"`, `"caba"`, `"abac"`; the
smallest is `"abac"`.

## Constraints

- `1 <= len(s) <= 10^6`
- `s` consists of lowercase English letters.

## Examples

### Example 1
```
Input:  s = "bca"
Output: "abc"
Explanation: Rotations are "bca", "cab", "abc". The smallest is "abc" (shift by 2).
```

### Example 2
```
Input:  s = "baabaa"
Output: "aabaab"
Explanation: Among the 6 rotations, "aabaab" (shift by 2, using the second 'a' region)
             is the lexicographically smallest.
```

### Example 3
```
Input:  s = "dcba"
Output: "adcb"
Explanation: Rotations are "dcba", "cbad", "badc", "adcb". The smallest is "adcb"
             (shift by 3).
```

## Hint

Run **Lyndon Factorization (Duval's algorithm)** on the doubled string `s + s` and stop
early: the start of the Lyndon factor that crosses index `n - 1` marks the beginning of
the minimal rotation. Runs in `O(n)`.
