# Palindrome Check with a Deque

**Difficulty:** Easy

**Source:** Classic — palindrome test via a double-ended queue

## Description

Given a string `s`, return `True` if it reads the same forwards and backwards, otherwise `False`. Solve it with a **deque**: load every character, then repeatedly compare the front and back characters, popping both, until one or zero characters remain.

Compare characters exactly as given (case- and space-sensitive). An empty string and a single character are palindromes.

## Examples

### Example 1

```
Input:  s = "racecar"
Output: true
```

**Explanation:** Popping ends in pairs — (r,r), (a,a), (c,c) — leaves the middle `e`; every pair matched, so it is a palindrome.

### Example 2

```
Input:  s = "hello"
Output: false
```

**Explanation:** The first front/back comparison is `h` vs `o`, which differ, so it returns `False` immediately.

## Hint

Push every character into a doubly-linked-list deque, then `popFront()` and `popBack()` together and compare — a mismatch means "not a palindrome".
