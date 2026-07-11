# Valid Palindrome

**Difficulty:** Easy

**Source:** LeetCode 125 — Valid Palindrome

## Description

A phrase is a **palindrome** if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads the
same forward and backward. Alphanumeric characters include letters (`a`–`z`,
`A`–`Z`) and digits (`0`–`9`).

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Examples

### Example 1
- **Input:** `s = "A man, a plan, a canal: Panama"`
- **Output:** `true`
- **Explanation:** After lowercasing and dropping non-alphanumeric characters we
  get `"amanaplanacanalpanama"`, which reads the same in both directions.

### Example 2
- **Input:** `s = "race a car"`
- **Output:** `false`
- **Explanation:** The filtered string is `"raceacar"`, which is **not** a
  palindrome (`r...r`, then `a...a`, then `c` vs `e` mismatch).

### Example 3
- **Input:** `s = " "`
- **Output:** `true`
- **Explanation:** After removing non-alphanumeric characters the string is
  empty. An empty string reads the same forward and backward, so it is a
  palindrome.

## Hint

Use **Two Pointers (opposite ends)**: start one index at the front and one at
the back, skip over any character that is not alphanumeric, and compare the two
(case-insensitively) as the pointers move toward each other.
