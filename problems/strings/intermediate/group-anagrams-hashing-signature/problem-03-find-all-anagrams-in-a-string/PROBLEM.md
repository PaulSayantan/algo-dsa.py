# Find All Anagrams in a String

**Difficulty:** Medium

**Source:** LeetCode 438 — Find All Anagrams in a String

## Description

Given two strings `s` and `p`, return an array of all the **start indices** of
`p`'s anagrams in `s`. You may return the answer in any order.

Concretely, for every window of length `len(p)` inside `s`, that window is an
anagram of `p` when it contains exactly the same characters with the same
frequencies as `p`. Report the starting index of every such window.

This applies the **hashing signature** idea to a *sliding window*: `p` has a
fixed count signature, and you slide a window of width `len(p)` across `s`,
maintaining the window's count signature incrementally and reporting each index
where the two signatures match.

## Constraints

- `1 <= s.length, p.length <= 3 * 10^4`
- `s` and `p` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation: The window "cba" starting at index 0 is an anagram of "abc"; the
window "bac" starting at index 6 is an anagram of "abc". No other length-3
window matches p's signature.
```

### Example 2

```
Input:  s = "abab", p = "ab"
Output: [0, 1, 2]
Explanation: The windows "ab" (index 0), "ba" (index 1), and "ab" (index 2) are
all anagrams of "ab".
```

### Example 3

```
Input:  s = "aa", p = "bb"
Output: []
Explanation: No length-2 window of s has the signature {b:2}, so there are no
matches.
```

## Hint

Keep a running **Group Anagrams (hashing signature)** (a length-26 count array)
for a window of width `len(p)`; slide it one character at a time and record every
index where the window's signature equals `p`'s signature.
