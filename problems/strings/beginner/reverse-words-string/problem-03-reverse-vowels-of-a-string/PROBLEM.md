# Reverse Vowels of a String

**Difficulty:** Easy

**Source:** LeetCode 345 — Reverse Vowels of a String

## Description

Given a string `s`, reverse only the **vowels** of the string and return the
result. The vowels are `'a'`, `'e'`, `'i'`, `'o'`, `'u'`, and they can appear in
**both lower and upper case**. Every non-vowel character must stay in its
original position.

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s` consists of printable ASCII characters.

## Examples

### Example 1

```
Input:  s = "IceCreAm"
Output: "AceCreIm"
Explanation: The vowels in order are I, e, e, A (at indices 0, 2, 5, 6).
Reversed, that sequence becomes A, e, e, I. Re-inserting them into the same
vowel slots and leaving consonants (c, C, r, m) fixed gives "AceCreIm".
```

### Example 2

```
Input:  s = "leetcode"
Output: "leotcede"
Explanation: The vowels are e, e, o, e (indices 1, 2, 5, 7). Reversed they are
e, o, e, e. Placing them back into indices 1, 2, 5, 7 yields "leotcede"; the
consonants l, t, c, d never move.
```

## Hint

Use the **Reverse Words / String** technique restricted to a subset: run two
pointers inward from both ends, but only swap when *both* pointers currently sit
on a vowel.
