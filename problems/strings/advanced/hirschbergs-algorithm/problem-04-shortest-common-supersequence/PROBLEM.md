# Shortest Common Supersequence

**Difficulty:** Hard

**Source:** LeetCode 1092 "Shortest Common Supersequence" (linear-space variant)

## Description

Given two strings `str1` and `str2`, return the **shortest string** that has **both**
`str1` and `str2` as subsequences. If more than one such shortest string exists, return
any one of them.

A string `s` is a *supersequence* of `t` if `t` can be obtained from `s` by deleting zero
or more characters. The shortest common supersequence (SCS) has length
`len(str1) + len(str2) - LCS(str1, str2)`: you write out both strings but merge the
characters they share (their longest common subsequence) exactly once.

To keep this in the Hirschberg family, you must produce the SCS while computing the
underlying LCS in only **`O(min(len(str1), len(str2)))` extra space** — no full
`O(n·m)` table.

## Constraints

- `1 <= len(str1), len(str2) <= 1000`
- `str1` and `str2` consist of lowercase English letters.
- The LCS used to build the answer must be found in `O(min(n, m))` extra space.
- Any shortest supersequence is accepted.

## Examples

### Example 1
```
Input:  str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: "cabac" has length 5. str1 = "abac" is a subsequence (c-ABAC), and
str2 = "cab" is a subsequence (CAB-ac). The LCS of the two is "ab" (length 2), so the
SCS length is 4 + 3 - 2 = 5.
```

### Example 2
```
Input:  str1 = "geek", str2 = "eke"
Output: "geeke"
Explanation: Length 5. "geek" is a subsequence (GEEK-e) and "eke" is a subsequence
(g-EKE... e). LCS is "ek" (length 2), so SCS length is 4 + 3 - 2 = 5.
```

### Example 3
```
Input:  str1 = "abc", str2 = "def"
Output: "abcdef"
Explanation: The strings share nothing (LCS length 0), so the shortest supersequence
just concatenates them: length 3 + 3 - 0 = 6. "adbecf" would also be valid.
```

## Hint

Merge the two strings along their longest common subsequence — shared characters are
written once, private stretches are written in order. Recover that LCS in linear space
with **Hirschberg's Algorithm**, then interleave.
