# Reverse Words in a String

**Difficulty:** Medium

**Source:** LeetCode 151 — Reverse Words in a String

## Description

Given an input string `s`, reverse the order of the **words**.

A word is defined as a sequence of non-space characters. The words in `s` are separated
by one or more spaces. Return a string of the words in reverse order concatenated by a
single space.

Note that `s` may contain leading or trailing spaces, or multiple spaces between two
words. The returned string should have only a single space separating the words and no
leading or trailing spaces.

## Constraints

- `1 <= s.length <= 10^4`
- `s` contains English letters (upper and lower case), digits, and spaces `' '`.
- There is at least one word in `s`.

## Examples

### Example 1

```
Input:  s = "the sky is blue"
Output: "blue is sky the"
```

Explanation: The words in reading order are `["the", "sky", "is", "blue"]`. Reversing
their order gives `["blue", "is", "sky", "the"]`, joined by single spaces.

### Example 2

```
Input:  s = "  hello world  "
Output: "world hello"
```

Explanation: The leading and trailing spaces are stripped, leaving the two words
`["hello", "world"]`. Reversing their order gives `["world", "hello"]`, joined by a
single space as `"world hello"`.

### Example 3

```
Input:  s = "a good   example"
Output: "example good a"
```

Explanation: The multiple spaces between `good` and `example` collapse to one. The
words `["a", "good", "example"]` reversed are `["example", "good", "a"]`.

## Hint

Use **Reverse In-Place**: reverse the entire character array first, then reverse each
individual word back to its correct spelling (after trimming/collapsing spaces).
