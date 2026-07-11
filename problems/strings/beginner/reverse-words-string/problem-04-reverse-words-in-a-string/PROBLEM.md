# Reverse Words in a String

**Difficulty:** Medium

**Source:** LeetCode 151 — Reverse Words in a String

## Description

Given an input string `s`, reverse the **order of the words**.

A word is a maximal sequence of non-space characters. The words in `s` are
separated by at least one space. Return a string of the words in reverse order
joined by a **single** space.

Note that `s` may contain leading or trailing spaces or multiple spaces between
two words. The returned string should have words separated by a single space and
should not contain any extra spaces.

## Constraints

- `1 <= s.length <= 10^4`
- `s` contains English letters (upper and lower case), digits, and spaces `' '`.
- There is at least one word in `s`.

## Examples

### Example 1

```
Input:  s = "the sky is blue"
Output: "blue is sky the"
Explanation: The words are ["the", "sky", "is", "blue"]. Reversing their order
gives ["blue", "is", "sky", "the"], joined by single spaces.
```

### Example 2

```
Input:  s = "  hello world  "
Output: "world hello"
Explanation: Leading and trailing spaces are stripped, so the words are
["hello", "world"]. Reversed and joined by a single space, the result is
"world hello" with no surrounding or duplicated spaces.
```

## Hint

Use the **Reverse Words / String** technique: either split on whitespace and
reverse the token list, or (for `O(1)` extra space on a mutable buffer) reverse
the entire string and then reverse each word back — remembering to normalize the
extra spaces.
