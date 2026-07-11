# Reverse Words in a String II

**Difficulty:** Medium

**Source:** LeetCode 186 — Reverse Words in a String II

## Description

Given a character array `s` that represents a sentence, reverse the **order of
the words** in place.

A word is a maximal sequence of non-space characters. The words in `s` are
separated by a single space, and there are no leading or trailing spaces.

You must reverse the word order using **O(1) extra space** — mutate the array
directly rather than splitting into a list of words and re-joining.

This is the string-level twin of rotating an array: the reversal trick reverses
the whole array and then "fixes up" each block (here, each word) with a second
reversal.

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is an English letter (uppercase or lowercase), digit, or space `' '`.
- There is at least one word in `s`.
- Words are separated by a single space; no leading or trailing spaces.

## Examples

### Example 1

```
Input:  s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
```

Explanation: The sentence is `"the sky is blue"`. Reversing the word order gives
`"blue is sky the"`. Note the letters inside each word keep their original
order.

### Example 2

```
Input:  s = ["a"," ","b"]
Output: ["b"," ","a"]
```

Explanation: The sentence `"a b"` has two single-letter words; swapping their
order yields `"b a"`.

## Hint

Use the **Rotate Array (reversal trick)**: reverse the entire array first, which
puts the words in the right order but spelled backwards, then reverse each
individual word to restore its letters.
