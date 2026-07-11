# Rotate String

**Difficulty:** Easy

**Source:** LeetCode 796 — Rotate String

## Description

Given two strings `s` and `goal`, return `True` if and only if `s` can become `goal`
after some number of **shifts** on `s`.

A shift on `s` consists of moving the leftmost character of `s` to the rightmost
position. For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

## Constraints

- `1 <= s.length, goal.length <= 100`
- `s` and `goal` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "abcde", goal = "cdeab"
Output: true
```

**Explanation:** Shifting `"abcde"` twice gives `"abcde" -> "bcdea" -> "cdeab"`, which
equals `goal`. Equivalently, `"cdeab"` appears inside `"abcdeabcde"`.

### Example 2

```
Input:  s = "abcde", goal = "abced"
Output: false
```

**Explanation:** No sequence of shifts of `"abcde"` produces `"abced"` (the characters
`d` and `e` are swapped, which rotation can never do), so the answer is `false`.

### Example 3

```
Input:  s = "aa", goal = "aa"
Output: true
```

**Explanation:** Zero shifts already make `s` equal to `goal`.

## Hint

A string `goal` is a rotation of `s` if and only if `goal` is a **substring** of
`s + s` (and they are the same length). Search for `goal` inside the doubled string
using **Naive Pattern Matching**.
