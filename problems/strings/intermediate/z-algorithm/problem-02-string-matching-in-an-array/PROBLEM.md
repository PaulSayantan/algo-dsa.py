# String Matching in an Array

**Difficulty:** Easy

**Source:** LeetCode 1408 — "String Matching in an Array".

## Description

Given an array of strings `words`, return **all strings in `words` that are a
substring of another word in `words`**. You may return the answer in any order.

A string `a` is a substring of string `b` if and only if `a` occurs as a
contiguous block of characters inside `b`. A word never counts as a substring of
itself; it must appear inside some **different** word in the array.

Although the arrays here are small, the intended learning goal is to answer each
"is `a` inside `b`?" query in linear time with the Z-Algorithm (build
`a + separator + b` and check whether any Z-value equals `len(a)`), rather than
relying on the language's built-in substring operator.

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 30`
- `words[i]` consists of lowercase English letters.
- All the strings of `words` are **unique**.

## Examples

### Example 1

```
Input:  words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is a substring of "mass" and "hero" is a substring of
"superhero". ["hero","as"] is also a valid answer.
```

### Example 2

```
Input:  words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et" and "code" are both substrings of "leetcode".
```

### Example 3

```
Input:  words = ["blue","green","bu"]
Output: []
Explanation: No word is a substring of another word, so the answer is empty.
```

## Hint

For each candidate word, test membership in the other words using the
**Z-Algorithm**: run Z on `candidate + '#' + other` and look for a Z-value equal
to `len(candidate)`.
