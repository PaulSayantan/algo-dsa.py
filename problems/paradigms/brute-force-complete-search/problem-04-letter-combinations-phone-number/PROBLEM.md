# Letter Combinations of a Phone Number

**Difficulty:** Medium

**Source:** LeetCode 17 (Letter Combinations of a Phone Number)

## Description

Given a string `digits` containing digits from `2`-`9` inclusive, return *all
the letter combinations* that the number could spell. Return the answer in any
order.

A mapping of digits to letters (like the buttons on a classic telephone keypad)
is given below. Note that `1` does **not** map to any letters.

```
2 -> "abc"     3 -> "def"     4 -> "ghi"
5 -> "jkl"     6 -> "mno"     7 -> "pqrs"
8 -> "tuv"     9 -> "wxyz"
```

Each digit contributes one letter to a combination, chosen independently from
that digit's letter set. The full answer is the **Cartesian product** of the
per-digit letter sets, which brute force / complete search enumerates directly.

## Constraints

- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.

## Examples

### Example 1

```
Input:  digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Explanation: Digit '2' maps to "abc" and '3' maps to "def". Pairing each of the
3 letters of '2' with each of the 3 letters of '3' gives 3 * 3 = 9 combinations.
(Any ordering of these 9 strings is accepted.)
```

### Example 2

```
Input:  digits = ""
Output: []
Explanation: There are no digits, so there are no letter combinations. The empty
string yields an empty list (NOT a list containing the empty string).
```

### Example 3

```
Input:  digits = "2"
Output: ["a","b","c"]
Explanation: A single digit '2' maps directly to its three letters.
```

## Hint

Use **Brute Force / Complete Search**: build the Cartesian product of the letter
sets, extending every partial combination by every letter of the next digit
(iteratively or via recursion).
