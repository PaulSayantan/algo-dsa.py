# Rotated Digits

**Difficulty:** Medium

**Source:** LeetCode 788 — Rotated Digits

## Description

An integer `x` is a **good number** if after rotating each of its digits
individually by 180 degrees, we get a **valid** number that is **different**
from `x`. Each digit must be rotated — we cannot choose to leave a digit
unrotated.

A number is valid after rotation if **every** one of its digits maps to a valid
digit:

- `0`, `1`, `8` rotate to themselves (`0`, `1`, `8`).
- `2` and `5` rotate to each other (`2 -> 5`, `5 -> 2`).
- `6` and `9` rotate to each other (`6 -> 9`, `9 -> 6`).
- `3`, `4`, `7` are **invalid** — a number containing any of these can never be
  rotated into a valid number.

So `x` is **good** if and only if all its digits are in `{0,1,2,5,6,8,9}` **and**
at least one of its digits is in `{2,5,6,9}` (a digit that actually changes under
rotation, guaranteeing the rotated number differs from `x`).

Given a positive integer `n`, return the count of good numbers in the range
`[1, n]`.

## Constraints

- `1 <= n <= 10^4`

## Examples

### Example 1

```
Input:  n = 10
Output: 4
Explanation: The good numbers in [1, 10] are 2, 5, 6, and 9.
             Note that 1 and 10 are valid after rotation but map to themselves
             (1 -> 1, 10 -> 10), so they are NOT good.
```

### Example 2

```
Input:  n = 20
Output: 9
Explanation: The good numbers in [1, 20] are 2, 5, 6, 9, 12, 15, 16, 19, 20.
             Each contains at least one rotation-changing digit (2,5,6,9) and no
             invalid digit (3,4,7). Numbers like 18 (1->1, 8->8) rotate to
             themselves, so they are NOT good.
```

### Example 3

```
Input:  n = 1
Output: 0
Explanation: Only the number 1 is considered. It rotates to 1 (unchanged), so it
             is not good. There are no good numbers in [1, 1].
```

## Hint

The "goodness" of a number depends only on the *set* of digits it contains
(must avoid `3,4,7`; must include at least one of `2,5,6,9`). Counting how many
numbers up to `n` satisfy such a per-digit condition is a textbook **Digit DP**:
carry a `tight` flag plus a boolean "have I already seen a rotation-changing
digit" flag.
