# Removing Stars From a String

**Difficulty:** Medium

**Source:** LeetCode 2390 — Removing Stars From a String

## Description

You are given a string `s` of lowercase letters and `'*'` characters. In one operation you pick a `*` and remove it together with the **closest non-star character to its left**. Repeat until no `*` remains. The result is guaranteed to be unique.

Return the resulting string after all stars have been removed. It is guaranteed the operation can always be performed (there is always a character to the left of each `*`).

## Examples

### Example 1

```
Input:  s = "leet**cod*e"
Output: 'lecoe'
```

**Explanation:** The first `*` removes the second `t`, the second `*` removes the first `t`, and the third `*` removes the `d`, leaving `lecoe`.

## Hint

A `*` behaves like a left-moving asteroid that annihilates the letter on top of the stack; push letters and pop one per star.
