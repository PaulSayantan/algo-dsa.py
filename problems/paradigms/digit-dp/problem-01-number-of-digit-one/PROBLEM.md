# Number of Digit One

**Difficulty:** Medium

**Source:** LeetCode 233 — Number of Digit One (classic "count occurrences of a digit up to N")

## Description

Given an integer `n`, count the **total number of times the digit `1` appears**
in the decimal representations of all non-negative integers less than or equal
to `n`.

Note that this counts *occurrences*, not the number of integers that contain a
`1`. For example, the number `11` contributes **two** to the total because it
has two `1` digits.

## Constraints

- `0 <= n <= 10^9`

## Examples

### Example 1

```
Input:  n = 13
Output: 6
Explanation: The digit 1 appears in the numbers 1, 10, 11, 12, and 13.
             1 -> one '1'
             10 -> one '1'
             11 -> two '1'
             12 -> one '1'
             13 -> one '1'
             Total occurrences = 1 + 1 + 2 + 1 + 1 = 6.
```

### Example 2

```
Input:  n = 0
Output: 0
Explanation: The only number considered is 0, which contains no digit 1.
```

### Example 3

```
Input:  n = 20
Output: 12
Explanation: Occurrences of '1' in 1,10,11,12,13,14,15,16,17,18,19 give
             1 + (1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1) = 12
             (the number 20 itself contributes no '1').
```

## Hint

This is a counting-over-a-range problem where the quantity depends only on the
digits of the numbers involved, so it is naturally solved with **Digit DP**:
walk the digits of `n` from most significant to least significant while carrying
a *tight* flag (whether the prefix so far equals the prefix of `n`) and
accumulate how many `1`s have been placed.
