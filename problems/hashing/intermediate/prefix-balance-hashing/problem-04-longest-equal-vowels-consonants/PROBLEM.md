# Longest Substring With Equal Vowels and Consonants

**Difficulty:** Medium

**Source:** Classic — equal vowels and consonants (balance hashing)

## Description

Given a lowercase string `s`, return the length of the longest substring containing an equal number of vowels (`a e i o u`) and consonants. Map each vowel to `+1` and each consonant to `-1`; the balance repeats at the two ends of any equal-count window, so store the earliest index of each balance value.

## Examples

### Example 1

```
Input:  s = "leetcode"
Output: 8
```

**Explanation:** The whole word has 4 vowels (e,e,o,e) and 4 consonants (l,t,c,d).

### Example 2

```
Input:  s = "abcde"
Output: 2
```

**Explanation:** "ab" has one vowel and one consonant.

## Hint

vowel -> +1, consonant -> -1; seed first = {0: -1} and keep the earliest index of each balance.
