# Valid Palindrome (Alphanumeric Only)

**Difficulty:** Easy

**Source:** LeetCode 125 — Valid Palindrome

## Description

Given a string `s`, consider only its alphanumeric characters and ignore case; return whether that filtered sequence is a palindrome. Build a deque of the lowercased alphanumeric characters, then compare from both ends. An empty filtered string counts as a palindrome.

## Examples

### Example 1

```
Input:  s = "A man, a plan, a canal: Panama"
Output: true
```

**Explanation:** "amanaplanacanalpanama" is a palindrome.

### Example 2

```
Input:  s = "0P"
Output: false
```

**Explanation:** '0' vs 'p' differ.

## Hint

Filter to c.lower() for alphanumeric c, load a deque, then compare popleft() vs pop().
