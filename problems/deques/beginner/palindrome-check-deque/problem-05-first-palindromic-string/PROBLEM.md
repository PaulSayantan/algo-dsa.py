# First Palindromic String in the Array

**Difficulty:** Easy

**Source:** LeetCode 2108 — Find First Palindromic String in the Array

## Description

Given a list of strings `words`, return the first string in `words` that is a palindrome. If there is no palindromic string, return the empty string `""`. Test each word by loading it into a deque and comparing `popleft()` against `pop()` from both ends; return the first word that passes.

## Examples

### Example 1

```
Input:  words = ["abc", "car", "ada", "racecar", "cool"]
Output: "ada"
```

**Explanation:** `"ada"` is the first word that reads the same forwards and backwards.

### Example 2

```
Input:  words = ["notapalindrome", "racecar"]
Output: "racecar"
```

**Explanation:** The first word is not a palindrome, so `"racecar"` is returned.

## Hint

Scan left to right; for each word run the deque `popleft()` vs `pop()` check and return the first palindrome, else `""`.
