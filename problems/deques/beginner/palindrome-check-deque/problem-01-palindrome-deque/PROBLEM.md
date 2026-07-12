# Palindrome Check with a Deque

**Difficulty:** Easy

**Source:** Classic — two-ended palindrome check

## Description

Given a string or list `s`, return whether it reads the same forwards and backwards. Load it into a deque and, while more than one element remains, compare `popleft()` against `pop()`; a mismatch means it is not a palindrome. Empty and single-element inputs are palindromes.

## Examples

### Example 1

```
Input:  s = "racecar"
Output: true
```

### Example 2

```
Input:  s = "abc"
Output: false
```

## Hint

while len(dq) > 1: if dq.popleft() != dq.pop(): return False. Otherwise True.
