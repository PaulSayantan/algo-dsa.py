# Count Special Integers

**Difficulty:** Hard

**Source:** LeetCode 2376 — Count Special Integers

## Description

We call a positive integer **special** if **all of its digits are distinct**
(no digit repeats). For example, `123` and `1024` are special, but `112` and
`900` are not.

Given a positive integer `n`, return the number of **special integers** that
belong to the inclusive range `[1, n]`.

## Constraints

- `1 <= n <= 2 * 10^9`

## Examples

### Example 1

```
Input:  n = 20
Output: 19
Explanation: All integers from 1 to 20, except 11, are special (11 repeats the
             digit 1). So there are 20 - 1 = 19 special integers.
```

### Example 2

```
Input:  n = 5
Output: 5
Explanation: Every one of 1, 2, 3, 4, 5 is a single-digit number, so all of them
             have distinct digits. Count = 5.
```

### Example 3

```
Input:  n = 135
Output: 110
Explanation: There are 110 integers in [1, 135] whose digits are all distinct.
             The remaining 25 numbers in [1, 135] contain a repeated digit
             (for example 11, 22, ..., 99, 100, 101, 110, 112, 113, ...),
             so 135 - 25 = 110 are special.
```

## Hint

"All digits distinct" means you must remember **which digits have already been
used** as you build the number left to right — a natural fit for a **Digit DP**
whose state includes a 10-bit *bitmask* of used digits, plus a *tight* flag and
a leading-zero flag so that leading zeros are not mistakenly treated as the used
digit `0`.
