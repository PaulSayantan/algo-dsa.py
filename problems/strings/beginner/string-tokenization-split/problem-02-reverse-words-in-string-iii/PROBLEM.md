# Reverse Words in a String III

**Difficulty:** Easy

**Source:** LeetCode 557 — Reverse Words in a String III

## Description

Given a string `s`, reverse the order of characters in each word **within** a
sentence while still preserving whitespace and the original **word order**.

In other words, split the sentence into words separated by single spaces, reverse
the letters of each individual word in place, and keep the words in the same
positions.

## Constraints

- `1 <= s.length <= 5 * 10^4`
- `s` contains printable ASCII characters.
- `s` does **not** contain any leading or trailing spaces.
- There is **exactly one** space between each pair of adjacent words.
- `s` contains at least one word.

## Examples

**Example 1**

```
Input:  s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Explanation: Each word is reversed on its own; the words stay in the same order
and are still separated by single spaces.
```

**Example 2**

```
Input:  s = "Mr Ding"
Output: "rM gniD"
Explanation: "Mr" -> "rM" and "Ding" -> "gniD"; word order is preserved.
```

**Example 3**

```
Input:  s = "hello"
Output: "olleh"
Explanation: A single word is simply reversed.
```

## Hint

Use **String Tokenization / Split**: split on spaces to get the words, reverse
each token, then join them back together with single spaces.
