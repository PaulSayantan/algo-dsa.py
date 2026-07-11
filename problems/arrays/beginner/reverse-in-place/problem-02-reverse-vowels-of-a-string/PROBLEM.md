# Reverse Vowels of a String

**Difficulty:** Easy

**Source:** LeetCode 345 — Reverse Vowels of a String

## Description

Given a string `s`, reverse only all the vowels in the string and return the resulting
string.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both
lower and upper cases. Every non-vowel character must stay in its original position;
only the vowels are rearranged, and they end up in reversed relative order.

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s` consists of printable ASCII characters.

## Examples

### Example 1

```
Input:  s = "IceCreAm"
Output: "AceCreIm"
```

Explanation: The vowels in `"IceCreAm"` are `['I', 'e', 'e', 'A']` (reading left to
right). Reversed, that sequence is `['A', 'e', 'e', 'I']`. Dropping them back into the
same vowel slots gives `"AceCreIm"`; the consonants `c`, `C`, `r`, `m` never move.

### Example 2

```
Input:  s = "leetcode"
Output: "leotcede"
```

Explanation: The vowels are `['e', 'e', 'o', 'e']`. Reversed they become
`['e', 'o', 'e', 'e']`, so the string becomes `"leotcede"`. The consonants
`l`, `t`, `c`, `d` remain fixed.

## Hint

Use **Reverse In-Place**: run two pointers inward, but only swap when *both* pointers
are sitting on a vowel; otherwise advance whichever pointer is on a consonant.
