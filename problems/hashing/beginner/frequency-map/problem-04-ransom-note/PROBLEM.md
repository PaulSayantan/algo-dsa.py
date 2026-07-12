# Ransom Note

**Difficulty:** Easy

**Source:** LeetCode 383 — Ransom Note

## Description

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed using the letters of `magazine`. Each letter in `magazine` may be used at most once.

## Examples

### Example 1

```
Input:  ransomNote = "aa", magazine = "ab"
Output: false
```

### Example 2

```
Input:  ransomNote = "aa", magazine = "aab"
Output: true
```

## Hint

Count the magazine's letters; the note is constructible iff every needed letter has enough supply.
