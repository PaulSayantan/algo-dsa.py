# Palindrome Number

**Difficulty:** Easy

**Source:** LeetCode 9 — Palindrome Number

## Description

Given an integer `x`, return whether `x` reads the same backward as forward. Any negative number is not a palindrome because the leading `-` would have to become a trailing `-`. For non-negative `x`, load its decimal digits into a deque and compare `popleft()` against `pop()` from both ends until at most one digit remains.

## Examples

### Example 1

```
Input:  x = 121
Output: true
```

**Explanation:** `121` reversed is still `121`.

### Example 2

```
Input:  x = -121
Output: false
```

**Explanation:** Reversed it reads `121-`, which is not a valid number, so negatives are never palindromes.

## Hint

Reject negatives up front, then load `str(x)` into a deque and compare `popleft()` vs `pop()`.
