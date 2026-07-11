# Find All Anagrams in a String

**Difficulty:** Medium

Source: LeetCode 438 — Find All Anagrams in a String

## Description

Given two strings `s` and `p`, return an array of **all the start indices** of `p`'s
anagrams in `s`. You may return the answer in any order.

In other words, find every index `i` such that the substring `s[i : i + len(p)]` is a
permutation (anagram) of `p` — it uses exactly the same characters with the same
frequencies as `p`.

## Constraints

- `1 <= s.length, p.length <= 3 * 10^4`
- `s` and `p` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation:
  - The substring starting at index 0 is "cba", which is an anagram of "abc".
  - The substring starting at index 6 is "bac", which is an anagram of "abc".
```

### Example 2

```
Input:  s = "abab", p = "ab"
Output: [0, 1, 2]
Explanation:
  - index 0 -> "ab" (anagram of "ab")
  - index 1 -> "ba" (anagram of "ab")
  - index 2 -> "ab" (anagram of "ab")
```

### Example 3

```
Input:  s = "aa", p = "bb"
Output: []
Explanation: No substring of "aa" of length 2 uses the letters of "bb", so there are
no matching start indices.
```

## Hint

Use an **Anagram Check (sort or count)** on a *sliding window*: maintain a running
frequency table for the current window of length `len(p)` and compare it against `p`'s
table as the window slides one character at a time.
