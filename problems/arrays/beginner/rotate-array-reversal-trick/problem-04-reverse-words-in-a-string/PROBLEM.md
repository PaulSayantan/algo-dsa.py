# Reverse Words in a String

**Difficulty:** Medium

**Source:** LeetCode 151 — Reverse Words in a String

## Description

Given an input string `s`, reverse the order of the **words**.

A word is a sequence of non-space characters. The words in `s` are separated by
one or more spaces. Return a string of the words in reverse order concatenated
by a **single** space.

Note that `s` may contain leading or trailing spaces, or multiple consecutive
spaces between words. The returned string should have words separated by a
single space and should **not** contain any leading or trailing spaces.

Because Python strings are immutable you will return a new string, but the
intended technique is the same reversal trick used for the in-place char-array
version — reverse the whole thing, then reverse each word — combined with
whitespace normalization.

## Constraints

- `1 <= s.length <= 10^4`
- `s` contains English letters (upper- and lower-case), digits, and spaces `' '`.
- There is **at least one** word in `s`.

## Examples

### Example 1

```
Input:  s = "the sky is blue"
Output: "blue is sky the"
```

Explanation: The four words are reversed in order; single spaces are preserved.

### Example 2

```
Input:  s = "  hello world  "
Output: "hello world"
```

Explanation: The leading and trailing spaces are removed, and the two words are
reversed in order.

### Example 3

```
Input:  s = "a good   example"
Output: "example good a"
```

Explanation: The multiple spaces between "good" and "example" are reduced to a
single space, and the word order is reversed.

## Hint

Use the **Rotate Array (reversal trick)**: after trimming and collapsing spaces,
reverse the whole character sequence and then reverse each individual word (or
equivalently reverse each word first, then the whole sequence).
