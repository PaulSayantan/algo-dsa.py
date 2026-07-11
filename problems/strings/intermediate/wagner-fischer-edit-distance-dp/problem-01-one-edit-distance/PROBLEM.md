# One Edit Distance

**Difficulty:** Medium

**Source:** LeetCode 161 — One Edit Distance

## Description

Given two strings `s` and `t`, return `true` if they are **exactly one edit distance**
apart, otherwise return `false`.

A string `s` is said to be one edit distance apart from a string `t` if you can turn
`s` into `t` using **exactly one** of the following operations:

- **Insert** exactly one character into `s` to get `t`.
- **Delete** exactly one character from `s` to get `t`.
- **Replace** exactly one character of `s` with a **different** character to get `t`.

Note the word *exactly*: if `s` and `t` are already equal (edit distance `0`), or if they
differ by two or more edits, the answer is `false`.

## Constraints

- `0 <= s.length, t.length <= 10^4`
- `s` and `t` consist of lowercase letters, uppercase letters, and digits.

## Examples

**Example 1**

```
Input:  s = "ab", t = "acb"
Output: true
Explanation: Insert 'c' into s between 'a' and 'b' to obtain t. That is a single insertion,
             so the edit distance is exactly 1.
```

**Example 2**

```
Input:  s = "cab", t = "ad"
Output: false
Explanation: The lengths differ by 1, so the only candidate is deleting one character from s.
             Deleting a single character from "cab" yields "ab", "cb", or "ca" — none equal "ad".
             The edit distance is greater than 1.
```

**Example 3**

```
Input:  s = "", t = ""
Output: false
Explanation: The strings are identical, so their edit distance is 0, not 1.
```

## Hint

This is a *bounded* edit-distance question. Reason about it with the **Wagner–Fischer
(Edit Distance DP)** recurrence: because you only need to know whether the distance is
exactly 1, the general table collapses to a narrow band you can check in a single pass.
