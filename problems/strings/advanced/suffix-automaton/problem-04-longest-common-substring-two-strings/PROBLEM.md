# Longest Common Substring of Two Strings

**Difficulty:** Hard

**Source:** Classic string problem (SPOJ LCS "Longest Common Substring"; also the
substring — not subsequence — variant of LeetCode 1143's cousin).

## Description

Given two strings `s` and `t`, find the length of their **longest common
substring** — the longest contiguous block of characters that appears in both
`s` and `t`.

Note this is a *substring* (contiguous), not a *subsequence*. If the two strings
share no character at all, the answer is `0`.

Return the **length** of the longest common substring.

## Constraints

- `1 <= len(s), len(t) <= 2.5 * 10^5`
- Both strings consist of lowercase English letters (or, more generally, a fixed
  alphabet).
- The two strings may have very different lengths.

## Examples

### Example 1
```
Input:  s = "abcde", t = "cdefg"
Output: 3
Explanation: The longest substring present in both is "cde" (length 3).
             "cd" and "de" are also common but shorter.
```

### Example 2
```
Input:  s = "banana", t = "ananas"
Output: 5
Explanation: "anana" (length 5) is a substring of both "banana" and "ananas".
             No length-6 substring is common.
```

### Example 3
```
Input:  s = "abc", t = "xyz"
Output: 0
Explanation: The strings share no common substring (not even a single letter),
             so the answer is 0.
```

## Hint

Build a **Suffix Automaton** of one string (say `s`), then feed `t` through the
automaton character by character, maintaining a current state and a current match
length. When a transition is missing, follow suffix links to shorten the match.
Track the maximum match length seen.
