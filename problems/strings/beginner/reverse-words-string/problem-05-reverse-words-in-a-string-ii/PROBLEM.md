# Reverse Words in a String II

**Difficulty:** Medium

**Source:** LeetCode 186 — Reverse Words in a String II

## Description

Given a character array `s`, reverse the **order of the words** in place.

A word is a maximal sequence of non-space characters. The words in `s` are
separated by a **single** space, and there are **no** leading or trailing
spaces. You must reverse the word order using `O(1)` extra space (a constant
number of scalar variables); you may not allocate another array proportional to
the input size.

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is an English letter (upper or lower case), digit, or the space `' '`.
- `s` has exactly one space between adjacent words and no leading/trailing space.
- There is at least one word in `s`.

## Examples

### Example 1

```
Input:  s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Explanation: The words are "the", "sky", "is", "blue". Reversing their order
gives "blue is sky the". Because the total length and the number of spaces are
unchanged, this fits back into the same array.
```

### Example 2

```
Input:  s = ["a"]
Output: ["a"]
Explanation: A single one-letter word reversed in order is itself. Nothing
moves.
```

## Hint

Use the **Reverse Words / String** technique: reverse the whole array first,
then reverse each word segment back in place. Two applications of the same
two-pointer swap give you `O(1)` extra space.
