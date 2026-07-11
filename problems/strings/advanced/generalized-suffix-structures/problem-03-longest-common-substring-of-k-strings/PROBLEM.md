# Longest Common Substring of K Strings

**Difficulty:** Hard

**Source:** SPOJ LCS2 — "Longest Common Substring II" (generalization of the
two-string longest-common-substring problem to many strings).

## Description

You are given `k` strings. Find the length of the **longest string that is a
contiguous substring of every one of them**.

This is the longest common *substring* (contiguous), not subsequence, and it must
be common to **all** `k` inputs simultaneously. If no non-empty string is common
to all of them (they do not all share even a single character), the answer is
`0`.

Return the **length** of this longest common substring.

## Constraints

- `2 <= k <= 10` strings.
- Each string has length up to `10^5`.
- The total length `L = sum of lengths` is up to `10^6`.
- All strings consist of lowercase English letters.

## Examples

### Example 1
```
Input:  ["alsdfkjfjkdsal", "fdjskalajfkdsla", "aaaajfaaaa"]
Output: 2
Explanation: "jf" is a substring of all three: alsdfk|jf|jkdsal,
             fdjskala|jf|kdsla, and aaaa|jf|aaaa. No length-3 block appears in all
             three strings, so the longest common substring has length 2.
```

### Example 2
```
Input:  ["abab", "baba", "aabb"]
Output: 2
Explanation: "ab" is a substring of all three ("ab"ab, b"ab"a, a"ab"b), length 2.
             "ba" is also common. No length-3 block appears in all three.
```

### Example 3
```
Input:  ["abc", "def", "xyz"]
Output: 0
Explanation: The three strings share no common character, so the longest
             common substring is empty, length 0.
```

## Hint

Build a **Generalized Suffix Structure** over all `k` strings. Give each state a
`k`-bit mask recording which source strings occur there and propagate the masks
up the suffix-link tree. The answer is the largest `len[v]` among states whose
mask has **all `k` bits set**.
