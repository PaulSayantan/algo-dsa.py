# Detect a Tandem Repeat

**Difficulty:** Easy

Source: Classic string / competitive-programming warm-up (a.k.a. "square-free string test").

## Description

A **tandem repeat** (or **square**) is a non-empty substring of the form `XX`,
where `X` is some non-empty string immediately followed by an identical copy of
itself. For example, `"abab"` is a square (`X = "ab"`), and `"aa"` is a square
(`X = "a"`). A string that contains no square anywhere is called **square-free**.

Given a string `s`, return `True` if `s` contains at least one tandem repeat as a
(contiguous) substring, and `False` otherwise.

This is the entry point to the Main–Lorentz world: before locating or counting
squares, you first learn to detect their existence efficiently.

## Constraints

- `1 <= len(s) <= 200_000`
- `s` consists of lowercase English letters.
- A single character alone is **not** a square (a square has length at least 2).

## Examples

### Example 1
```
Input:  s = "abab"
Output: True
Explanation: The whole string "abab" is a square with X = "ab".
```

### Example 2
```
Input:  s = "abcde"
Output: False
Explanation: No substring repeats itself back-to-back, so the string is square-free.
```

### Example 3
```
Input:  s = "abcabcabc"
Output: True
Explanation: The substring "abcabc" (positions 0..5) is a square with X = "abc".
             (There are several other squares too, e.g. starting at index 1, 2, 3.)
```

## Hint

Splitting the string in half and asking "does a square cross the middle?" lets you
recurse on each half in O(n log n) overall — this is the **Main–Lorentz Algorithm**.
Detecting existence only needs to know whether *any* crossing range is non-empty.
