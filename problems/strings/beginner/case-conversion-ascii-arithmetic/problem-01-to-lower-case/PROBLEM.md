# To Lower Case

**Difficulty:** Easy

**Source:** LeetCode 709 (To Lower Case)

## Description

Given a string `s`, return the string after replacing every uppercase letter with
the same letter in lowercase.

You are asked to implement this **without** calling a built-in case-conversion
helper (such as Python's `str.lower()`). Instead, convert each character by
reasoning about its ASCII code: uppercase letters `'A'..'Z'` occupy codes 65..90,
and each lowercase counterpart sits exactly 32 codes higher (`'a'` is 97). Every
character that is not an uppercase letter (digits, spaces, punctuation, or letters
that are already lowercase) must be left unchanged.

## Constraints

- `1 <= s.length <= 100`
- `s` consists of printable ASCII characters.

## Examples

### Example 1

```
Input:  s = "Hello"
Output: "hello"
Explanation: 'H' has code 72; adding 32 gives 104 which is 'h'. The remaining
letters 'e','l','l','o' are already lowercase and stay the same.
```

### Example 2

```
Input:  s = "here"
Output: "here"
Explanation: Every character is already lowercase, so nothing changes.
```

### Example 3

```
Input:  s = "LOVELY"
Output: "lovely"
Explanation: All six letters are uppercase; each has 32 added to its code to
produce its lowercase form.
```

## Hint

Use **Case Conversion & ASCII Arithmetic**: detect uppercase letters by their code
range and shift them by the fixed gap between the uppercase and lowercase blocks.
