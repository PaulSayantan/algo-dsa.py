# Longest Happy Prefix

**Difficulty:** Medium (LeetCode labels it Hard)

**Source:** LeetCode 1392 — Longest Happy Prefix

## Description

A string is called a **happy prefix** if it is a **non-empty** prefix that is
also a **suffix** (excluding the whole string itself).

Given a string `s`, return the **longest happy prefix** of `s`. Return an empty
string `""` if no such prefix exists.

The classic solution is the KMP failure function, but this problem is a perfect
drill for **prefix hashing**: precompute prefix hashes so the hash of any prefix
`s[0..L-1]` and any suffix `s[n-L..n-1]` can be read in `O(1)`, then find the
largest length `L < n` for which those two hashes are equal. Use two moduli so
a hash match reliably means the prefix and suffix are truly identical.

## Constraints

- `1 <= s.length <= 10^5`
- `s` contains only lowercase English letters.

## Examples

**Example 1**

```
Input:  s = "level"
Output: "l"
Explanation: The prefixes are "l","le","lev","leve". The suffixes are
"l","el","vel","evel". The largest string that is both a prefix and a suffix
(and not the whole string) is "l".
```

**Example 2**

```
Input:  s = "ababab"
Output: "abab"
Explanation: "abab" is the longest prefix that is also a suffix. They can
overlap in the original string.
```

**Example 3**

```
Input:  s = "abcdef"
Output: ""
Explanation: No non-empty prefix equals a suffix, so the answer is "".
```

## Hint

Use **Double Hashing / Anti-Hash**: build prefix hashes of `s`, then for
lengths `L` from `n-1` down to `1` compare `hash(prefix of length L)` with
`hash(suffix of length L)`; the first (longest) match under two moduli is the
answer.
