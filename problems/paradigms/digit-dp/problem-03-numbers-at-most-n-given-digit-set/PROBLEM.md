# Numbers At Most N Given Digit Set

**Difficulty:** Medium

**Source:** LeetCode 902 — Numbers At Most N Given Digit Set

## Description

You are given an array of `digits`, which is **sorted in non-decreasing order**.
Each `digits[i]` is a single decimal digit character from `'1'` to `'9'` (note:
`'0'` is **not** in the set), and all entries are distinct.

You may write numbers using **only** these digits, and you may use each digit
**as many times as you want**. For example, if `digits = ['1', '3', '5']`, then
you can write numbers such as `'13'`, `'551'`, and `'1351315'`.

Return the count of **positive integers** that can be written this way and are
**less than or equal to** a given integer `n`.

## Constraints

- `1 <= digits.length <= 9`
- `digits[i]` is a character in the range `'1'` to `'9'`.
- All the values in `digits` are **unique**.
- `digits` is sorted in non-decreasing order.
- `1 <= n <= 10^9`

## Examples

### Example 1

```
Input:  digits = ["1","3","5","7"], n = 100
Output: 20
Explanation:
  The 20 numbers that can be written are:
  1-digit: 1, 3, 5, 7                      (4 numbers)
  2-digit: 11, 13, 15, 17, 31, 33, 35, 37,
           51, 53, 55, 57, 71, 73, 75, 77  (16 numbers)
  Total = 4 + 16 = 20. (No 3-digit number formed from {1,3,5,7} is <= 100.)
```

### Example 2

```
Input:  digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation:
  We can write numbers with 1, 2, 3, ..., 9 digits using the three allowed
  digits, and every such number is <= 10^9. The count is
  3 + 3^2 + 3^3 + ... + 3^9 = 29523.
```

### Example 3

```
Input:  digits = ["7"], n = 8
Output: 1
Explanation: The only writable number <= 8 is 7 itself.
```

## Hint

The allowed digits form a restricted alphabet, and you must count writable
numbers `<= n`. This is a **Digit DP** where numbers of length shorter than `n`
are all free, and numbers of the same length as `n` require the usual *tight*
bound tracking so you never exceed `n`.
