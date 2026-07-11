# Palindromic Substrings

**Difficulty:** Medium

**Source:** LeetCode 647 — Palindromic Substrings

## Description

Given a string `s`, return the **number of palindromic substrings** in it.

A substring is a contiguous sequence of characters within the string. Two
substrings are counted separately if they start or end at different indices, even
if they consist of the same characters. Every single character counts as a
palindrome of length 1.

The straightforward "expand around each center" approach is O(n^2). Manacher's
Algorithm computes the palindrome radius at every center in O(n), and each center
with radius `p` (measured in the transformed string) contributes exactly
`(p + 1) // 2` palindromes in the original string — summing these gives the total
count in linear time.

## Constraints

- `1 <= s.length <= 1000` (aim for a solution that also scales to `10^5+`)
- `s` consists of lowercase English letters.

## Examples

### Example 1
```
Input:  s = "abc"
Output: 3
Explanation: Three single-character palindromes: "a", "b", "c". No longer
palindromic substring exists.
```

### Example 2
```
Input:  s = "aaa"
Output: 6
Explanation: The palindromic substrings are "a", "a", "a", "aa", "aa", "aaa".
That is 3 single characters + 2 "aa" + 1 "aaa" = 6.
```

### Example 3
```
Input:  s = "abba"
Output: 6
Explanation: "a", "b", "b", "a" (4 singles), "bb", and "abba" -> 4 + 1 + 1 = 6.
```

## Hint

Compute the palindrome radius at every center with **Manacher's Algorithm**; a
center whose transformed radius is `p` accounts for `(p + 1) // 2` distinct
palindromic substrings. Sum over all centers.
