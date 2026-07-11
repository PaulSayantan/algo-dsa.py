# Total Length of All Distinct Substrings

**Difficulty:** Medium

**Source:** Classic string-processing exercise (a natural extension of counting
distinct substrings; appears in various competitive-programming sets and
university course problems).

## Description

Given a string `s`, compute the **sum of the lengths of all distinct non-empty
substrings** of `s`.

Formally, let `D` be the set of distinct substrings of `s`. Return
`sum(len(w) for w in D)`. As with counting distinct substrings, each distinct
string contributes its length **once**, no matter how many times it occurs.

## Constraints

- `1 <= len(s) <= 10^5`
- `s` consists of lowercase English letters.
- The answer can be as large as roughly `n^3 / 6`, so use a 64-bit integer type
  (Python ints are unbounded).

## Examples

### Example 1
```
Input:  s = "abc"
Output: 10
Explanation: Distinct substrings: "a","b","c" (len 1 each = 3),
             "ab","bc" (len 2 each = 4), "abc" (len 3 = 3). Total = 3+4+3 = 10.
```

### Example 2
```
Input:  s = "aaa"
Output: 6
Explanation: Distinct substrings: "a" (1), "aa" (2), "aaa" (3). Total = 1+2+3 = 6.
```

### Example 3
```
Input:  s = "abab"
Output: 16
Explanation: The 7 distinct substrings and their lengths are
             "a"(1), "b"(1), "ab"(2), "ba"(2), "aba"(3), "bab"(3), "abab"(4).
             Total = 1+1+2+2+3+3+4 = 16.
```

## Hint

Build a **Suffix Automaton**. A state `v` represents every substring whose length
lies in `(len[link[v]], len[v]]`; the sum of those integers is an arithmetic
series you can add per state in `O(1)`.
