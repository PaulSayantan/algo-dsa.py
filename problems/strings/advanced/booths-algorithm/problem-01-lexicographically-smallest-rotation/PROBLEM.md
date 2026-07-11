# Lexicographically Smallest Rotation

**Difficulty:** Easy

**Source:** Classic string problem (equivalent to GeeksforGeeks "Lexicographically smallest rotation of a string"; the linear-time solution is Booth's Algorithm, JGL Booth 1980).

## Description

A **rotation** of a string `s` of length `n` is obtained by moving some prefix of `s`
to its end. Formally, rotation `i` (for `0 <= i < n`) is:

```
rot(s, i) = s[i:] + s[:i]
```

For example, the rotations of `"cba"` are `"cba"`, `"bac"`, and `"acb"`.

Given a string `s`, return the rotation of `s` that is **lexicographically smallest**
(the one that would come first in a dictionary). Comparison is the standard character
ordering (for lowercase letters, ordinary alphabetical order).

You must return the smallest rotation as an actual string. A brute-force scan over all
`n` rotations is `O(n^2)`; you are expected to do it in **linear time**.

## Constraints

- `1 <= len(s) <= 10^6`
- `s` consists of characters from a fixed, totally ordered alphabet (e.g. lowercase
  English letters `a`–`z`).
- If several rotations are tied for smallest (possible when `s` has periodicity, e.g.
  `"abab"`), returning any one of them is fine — they are identical strings anyway.

## Examples

### Example 1

```
Input:  s = "cba"
Output: "acb"
Explanation: The rotations are "cba", "bac", "acb". In dictionary order
             "acb" < "bac" < "cba", so the smallest is "acb".
```

### Example 2

```
Input:  s = "bbaaccaadd"
Output: "aaccaaddbb"
Explanation: The smallest rotation starts at index 2 ("aaccaaddbb").
             Any rotation starting with 'a' beats one starting with 'b';
             among the two 'a'-starting rotations, "aaccaaddbb" (index 2)
             is smaller than "aaddbbaacc" (index 6) because at the third
             character 'c' < 'd'.
```

### Example 3

```
Input:  s = "abab"
Output: "abab"
Explanation: The distinct rotations are "abab" and "baba"; "abab" is already
             the smallest, so the answer is the original string.
```

## Hint

Concatenate `s` with itself and run **Booth's Algorithm** — a modified KMP
failure-function scan — to locate the start index of the least rotation in `O(n)`.
