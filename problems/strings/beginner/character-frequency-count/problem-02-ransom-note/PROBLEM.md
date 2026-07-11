# Ransom Note

**Difficulty:** Easy

**Source:** LeetCode 383 — Ransom Note

## Description

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can
be constructed by using the letters from `magazine`, and `false` otherwise.

Each letter in `magazine` can only be used **once** in `ransomNote`. In other
words, for every distinct character, `ransomNote` must not require more copies of
that character than `magazine` actually provides.

## Constraints

- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  ransomNote = "a", magazine = "b"
Output: false
Explanation: The note needs one 'a', but the magazine only supplies a 'b'. The
             required letter is unavailable.
```

### Example 2

```
Input:  ransomNote = "aa", magazine = "ab"
Output: false
Explanation: The note needs two 'a's, but the magazine has only one 'a'. There are
             not enough copies.
```

### Example 3

```
Input:  ransomNote = "aa", magazine = "aab"
Output: true
Explanation: The magazine has 'a' x2 and 'b' x1. The note needs 'a' x2, which is
             covered with a spare 'b' left over.
```

## Hint

This is a "does the supply cover the demand?" question. Build a **Character
Frequency Count** of the magazine, then check that it has at least as many of each
letter as the ransom note requires.
