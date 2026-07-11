# Reverse Words in a String III

**Difficulty:** Easy

**Source:** LeetCode 557 — Reverse Words in a String III

## Description

Given a string `s`, reverse the order of characters in each word within the
sentence while still **preserving whitespace and the original word order**.

A "word" is a maximal sequence of non-space characters. Words are separated by
single spaces, and the string has no leading or trailing spaces.

## Constraints

- `1 <= s.length <= 5 * 10^4`
- `s` contains printable ASCII characters.
- There is exactly one space between adjacent words.
- `s` does not contain any leading or trailing spaces.

## Examples

### Example 1

```
Input:  s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Explanation: Each word is reversed independently. "Let's" -> "s'teL",
"take" -> "ekat", "LeetCode" -> "edoCteeL", "contest" -> "tsetnoc".
The words stay in their original left-to-right order and the spaces are kept.
```

### Example 2

```
Input:  s = "Mr Ding"
Output: "rM gniD"
Explanation: "Mr" -> "rM" and "Ding" -> "gniD". Word order is unchanged, so
the space between them stays exactly where it was.
```

## Hint

Use the **Reverse Words / String** technique: identify each word's boundaries,
then apply the two-pointer reversal to that word's span. Leave the word ordering
alone — only the letters within each word flip.
