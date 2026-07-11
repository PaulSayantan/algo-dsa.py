# Excel Sheet Column Number

**Difficulty:** Easy

**Source:** LeetCode 171 (Excel Sheet Column Number)

## Description

Spreadsheets label columns with letters: the first column is `"A"`, then `"B"`,
..., `"Z"`, then `"AA"`, `"AB"`, ..., `"AZ"`, `"BA"`, and so on. Given such a
column title as a string `columnTitle`, return its corresponding column **number**
(a 1-based integer).

This is essentially reading a number in base 26, where the "digits" are letters.
Each letter contributes a value of `ord(c) - ord('A') + 1` (so `'A'` is 1, `'B'`
is 2, ..., `'Z'` is 26). Processing the title left to right, you multiply the
accumulated result by 26 and add the current letter's value — exactly how you would
parse a decimal number one digit at a time, but with base 26 and 1-indexed digits.

## Constraints

- `1 <= columnTitle.length <= 7`
- `columnTitle` consists only of uppercase English letters.
- `columnTitle` is in the range `["A", "FXSHRXW"]`.

## Examples

### Example 1

```
Input:  columnTitle = "A"
Output: 1
Explanation: 'A' maps to ord('A') - ord('A') + 1 = 1.
```

### Example 2

```
Input:  columnTitle = "AB"
Output: 28
Explanation: 'A' contributes 1, then result = 1*26 + 2 = 28 (the value of 'B').
```

### Example 3

```
Input:  columnTitle = "ZY"
Output: 701
Explanation: 'Z' contributes 26, then result = 26*26 + 25 = 676 + 25 = 701.
```

## Hint

Use **Case Conversion & ASCII Arithmetic**: map each letter to a 1-based digit with
`ord(c) - ord('A') + 1` and accumulate the value as a base-26 number.
