# Valid Palindrome

**Difficulty:** Easy

**Source:** LeetCode 125 — Valid Palindrome

## Description

A phrase is a **palindrome** if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads the
same forward and backward. Alphanumeric characters include letters and
digits.

Given a string `s`, return `True` if it is a palindrome, or `False`
otherwise.

## Constraints

- `1 <= len(s) <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Examples

### Example 1
```
Input:  s = "A man, a plan, a canal: Panama"
Output: True
Explanation: After lowercasing and dropping non-alphanumeric characters,
             the string becomes "amanaplanacanalpanama", which reads the
             same forwards and backwards.
```

### Example 2
```
Input:  s = "race a car"
Output: False
Explanation: Cleaned, the string is "raceacar", which is not a palindrome
             ('r' at the front vs 'r' at the back matches, but 'a' vs 'a',
             then 'c' vs 'c', then 'e' vs 'a' fails).
```

### Example 3
```
Input:  s = " "
Output: True
Explanation: After removing non-alphanumeric characters the string is empty
             "". An empty string reads the same forwards and backwards, so
             it is a palindrome.
```

## Hint

Use the **Palindrome Check (two pointers)** technique: keep a pointer at each
end, skip over characters that are not alphanumeric, and compare the
lowercased characters as the pointers move inward.
