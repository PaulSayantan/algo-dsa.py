# Count Distinct Substrings

**Difficulty:** Medium

**Source:** LeetCode 1698 — "Number of Distinct Substrings in a String"
(also a classic GeeksforGeeks / competitive-programming problem). Idiomatically
solved with polynomial hashing (or a suffix automaton / suffix array for the
optimal bound).

## Description

Given a string `s`, return the number of **distinct** non-empty substrings of
`s`.

A substring is a contiguous sequence of characters within the string. Two
substrings are considered the same if they contain the same characters in the
same order, regardless of where they occur; each distinct string is counted
exactly once.

The total number of `(start, end)` substring positions is `n·(n+1)/2`, but many
of them may be identical strings. You must count how many *unique* strings appear
among all of them.

The hashing approach: enumerate all `O(n^2)` substrings, but instead of storing
each substring (which costs `O(length)` to hash/compare), store its **polynomial
hash** in a set. Using precomputed prefix hashes, each substring's hash is
`O(1)`, so the whole enumeration is `O(n^2)` rather than `O(n^3)`.

## Constraints

- `1 <= len(s) <= 500`
- `s` consists of only lowercase English letters.

## Examples

### Example 1

```
Input:  s = "aba"
Output: 5
Explanation: The distinct substrings are: "a", "b", "ab", "ba", "aba".
             (Note "a" appears twice as a substring but is counted once.)
```

### Example 2

```
Input:  s = "aaa"
Output: 3
Explanation: The distinct substrings are: "a", "aa", "aaa".
             Positions give 6 substrings total, but only 3 are unique.
```

### Example 3

```
Input:  s = "abc"
Output: 6
Explanation: All substrings are distinct: "a", "b", "c", "ab", "bc", "abc".
```

## Hint

Precompute **polynomial prefix hashes** so every substring's hash is available in
`O(1)`. Drop each substring's hash into a hash set and return the set's size — no
substring is ever materialized or compared character-by-character. This is
**Rolling Hash / Polynomial Hashing**.
