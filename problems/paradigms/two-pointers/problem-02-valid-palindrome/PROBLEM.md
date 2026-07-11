# Valid Palindrome

**Difficulty:** Easy

**Source:** LeetCode 125 (Valid Palindrome)

## Description

A phrase is a **palindrome** if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads the
same forward and backward. Alphanumeric characters include letters and digits.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Examples

### Example 1

```
Input:  s = "A man, a plan, a canal: Panama"
Output: true
```

Explanation: After lowercasing and dropping non-alphanumeric characters, the
string becomes `"amanaplanacanalpanama"`, which reads the same both ways.

### Example 2

```
Input:  s = "race a car"
Output: false
```

Explanation: The cleaned string is `"raceacar"`, which is not a palindrome
(the first character `r` does not match the last character `r`'s counterpart —
comparing inward, `a` vs `c` fails).

### Example 3

```
Input:  s = " "
Output: true
```

Explanation: After removing non-alphanumeric characters the string is empty, and
an empty string is considered a palindrome.

## Hint

Use the **Two Pointers** technique: one pointer starts at the left, one at the
right, and they move toward each other. Skip characters that are not
alphanumeric and compare the rest case-insensitively.
