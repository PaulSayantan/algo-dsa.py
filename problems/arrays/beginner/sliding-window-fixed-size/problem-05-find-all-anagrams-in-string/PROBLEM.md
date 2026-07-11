# Find All Anagrams in a String

**Difficulty:** Medium

**Source:** LeetCode 438 — "Find All Anagrams in a String"

## Description

Given two strings `s` and `p`, return a list of the **start indices** of all of `p`'s
**anagrams** in `s`. You may return the answer in any order.

An **anagram** is a rearrangement of all the letters of a word using each letter exactly
once. So you are looking for every substring of `s` of length `len(p)` that has the
**same multiset of characters** as `p`.

## Constraints

- `1 <= s.length, p.length <= 3 * 10^4`
- `s` and `p` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "cbaebabacd", p = "abc"
Output: [0, 6]
```

**Explanation:** The substring starting at index 0 is `"cba"`, an anagram of `"abc"`.
The substring starting at index 6 is `"bac"`, also an anagram of `"abc"`. No other
length-3 window matches.

### Example 2

```
Input:  s = "abab", p = "ab"
Output: [0, 1, 2]
```

**Explanation:** The length-2 windows are `"ab"` (index 0), `"ba"` (index 1), and
`"ab"` (index 2) — all three are anagrams of `"ab"`.

### Example 3

```
Input:  s = "aa", p = "bb"
Output: []
```

**Explanation:** No window of `s` contains the letters of `"bb"`, so there are no
matches and the result is empty.

## Hint

Use a **Sliding Window (fixed size)** of width `len(p)`. Keep a character-count table
for the current window and compare it to `p`'s count table. As the window slides,
increment the entering character's count and decrement the leaving one, so each check
stays cheap instead of re-counting the whole window.
