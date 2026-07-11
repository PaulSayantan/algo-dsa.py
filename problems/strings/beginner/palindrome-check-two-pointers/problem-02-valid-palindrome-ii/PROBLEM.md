# Valid Palindrome II

**Difficulty:** Easy (borderline Medium)

**Source:** LeetCode 680 — Valid Palindrome II

## Description

Given a string `s`, return `True` if `s` can become a palindrome after
deleting **at most one** character from it. Deleting zero characters is
allowed, so any string that is already a palindrome qualifies.

The string consists of lowercase English letters only.

## Constraints

- `1 <= len(s) <= 10^5`
- `s` consists of lowercase English letters.

## Examples

### Example 1
```
Input:  s = "aba"
Output: True
Explanation: "aba" is already a palindrome, so no deletion is needed.
```

### Example 2
```
Input:  s = "abca"
Output: True
Explanation: The ends 'a' and 'a' match. Inside, 'b' vs 'c' mismatch.
             Delete 'c' to get "aba" (or delete 'b' to get "aca"), which
             is a palindrome. One deletion suffices.
```

### Example 3
```
Input:  s = "abc"
Output: False
Explanation: 'a' vs 'c' mismatch. Deleting either leaves "bc" or "ab",
             neither of which is a palindrome. No single deletion works.
```

## Hint

Use the **Palindrome Check (two pointers)** technique. Scan inward normally;
at the first mismatch you have exactly two candidates to try — skip the left
character or skip the right character — and check whether either remaining
substring is a plain palindrome.
