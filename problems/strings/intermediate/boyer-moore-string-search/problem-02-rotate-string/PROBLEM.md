# Rotate String

**Difficulty:** Easy

**Source:** LeetCode 796 — "Rotate String"

## Description

Given two strings `s` and `goal`, return `true` if and only if `s` can become
`goal` after some number of **shifts** on `s`.

A shift on `s` moves the leftmost character of `s` to the rightmost position.
For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

The classic trick: `goal` is a rotation of `s` if and only if `goal` is a
**substring of `s + s`** (and the two strings have equal length). That reduces
the whole problem to a single substring search — an ideal fit for a fast
single-pattern matcher.

## Constraints

- `1 <= s.length, goal.length <= 100`
- `s` and `goal` consist of lowercase English letters.

## Examples

### Example 1
```
Input:  s = "abcde", goal = "cdeab"
Output: true
Explanation: "abcde" -> "bcdea" -> "cdeab" reaches goal after 2 shifts.
             Equivalently, "cdeab" is a substring of "abcdeabcde".
```

### Example 2
```
Input:  s = "abcde", goal = "abced"
Output: false
Explanation: No sequence of shifts of "abcde" produces "abced"; "abced" is not
             a substring of "abcdeabcde".
```

### Example 3
```
Input:  s = "aa", goal = "a"
Output: false
Explanation: The lengths differ, so no rotation can match.
```

## Hint

Concatenate `s + s` and check whether `goal` appears inside it (only when
lengths match). Perform that substring check with **Boyer–Moore (string
search)** rather than a naive scan.
