# Maximum Number of Non-overlapping Palindrome Substrings

**Difficulty:** Hard

**Source:** LeetCode 2472 — Maximum Number of Non-overlapping Palindrome
Substrings

## Description

You are given a string `s` and a positive integer `k`.

Select a set of **non-overlapping** substrings of `s` such that:

- The length of each substring is **at least** `k`.
- Each substring is a **palindrome**.

Return the **maximum** number of substrings you can select.

A **substring** is a contiguous, non-empty sequence of characters within a
string. Non-overlapping means no two chosen substrings share a character
position.

## Constraints

- `1 <= k <= s.length <= 2000`
- `s` consists of lowercase English letters.

## Examples

**Example 1**

```
Input:  s = "abaccdbbd", k = 3
Output: 2
Explanation: Choose "aba" (indices 0-2) and "dbbd" (indices 5-8). Both are
             palindromes of length >= 3 and they do not overlap. No selection
             yields more than 2.
```

**Example 2**

```
Input:  s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome of length >= 2 in the string, so nothing
             can be selected.
```

**Example 3**

```
Input:  s = "aabbaa", k = 2
Output: 3
Explanation: Choose "aa" (0-1), "bb" (2-3), and "aa" (4-5) — three
             non-overlapping palindromes each of length >= 2.
```

## Hint

Sweep the `2n - 1` centers left to right using the **Longest Palindromic
Substring (expand around center)** technique. As soon as an expansion produces a
palindrome of length `>= k` (bounded so it does not overlap what you already
took), greedily select it, jump your left boundary past its end, and continue.
The shortest qualifying palindrome at the earliest position is always safe to
take.
