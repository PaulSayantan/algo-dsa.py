# Reverse Words in a String

**Difficulty:** Medium

**Source:** LeetCode 151 — Reverse Words in a String

## Description

Given an input string `s`, reverse the **order of the words**.

A **word** is defined as a sequence of non-space characters. The words in `s`
will be separated by at least one space.

Return a string of the words in **reverse order** concatenated by a **single
space**.

Note that `s` may contain leading or trailing spaces or multiple spaces between
two words. The returned string should have only a single space separating the
words. Do **not** include any extra spaces.

## Constraints

- `1 <= s.length <= 10^4`
- `s` contains English letters (upper and lower case), digits, and spaces `' '`.
- There is **at least one** word in `s`.

## Examples

**Example 1**

```
Input:  s = "the sky is blue"
Output: "blue is sky the"
Explanation: The four words reversed in order.
```

**Example 2**

```
Input:  s = "  hello world  "
Output: "world hello"
Explanation: The reversed string should not contain leading or trailing spaces.
```

**Example 3**

```
Input:  s = "a good   example"
Output: "example good a"
Explanation: Multiple spaces between words are reduced to a single space in the
reversed string.
```

## Hint

Use **String Tokenization / Split**: split on runs of whitespace to get clean
words, reverse the list of tokens, and join with single spaces.
