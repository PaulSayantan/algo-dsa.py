# Longest Happy Prefix

**Difficulty:** Hard

**Source:** LeetCode 1392 — "Longest Happy Prefix"

## Description

A string is called a **happy prefix** if it is a **non-empty prefix** which is
also a **suffix** (excluding the whole string itself).

Given a string `s`, return the **longest happy prefix** of `s`. Return an empty
string `""` if no such prefix exists.

In other words, find the longest proper prefix of `s` that equals a suffix of
`s`. This is exactly the "longest border" of the string. Rabin–Karp solves it by
comparing the hash of the length-`L` prefix against the hash of the length-`L`
suffix for decreasing `L`, using precomputed prefix hashes so every comparison
is `O(1)`.

## Constraints

- `1 <= s.length <= 10^5`
- `s` contains only lowercase English letters.

## Examples

### Example 1

```
Input:  s = "level"
Output: "l"
Explanation:
  The proper prefixes are "l", "le", "lev", "leve".
  The proper suffixes are "l", "el", "vel", "evel".
  The longest string that is both a prefix and a suffix is "l".
```

### Example 2

```
Input:  s = "ababab"
Output: "abab"
Explanation:
  "abab" is a prefix (first 4 characters) and also a suffix (last 4 characters).
  No longer proper prefix/suffix match exists, so the answer is "abab".
```

### Example 3

```
Input:  s = "abcdef"
Output: ""
Explanation:
  No proper prefix equals a suffix, so the longest happy prefix is empty.
```

## Hint

Precompute **prefix hashes** of `s` so the hash of any substring is available in
`O(1)`. Then, for lengths `L` from `n-1` down to `1`, use **Rabin–Karp** to
compare `hash(prefix of length L)` with `hash(suffix of length L)` and return
the first match.
