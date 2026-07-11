# Cyclical Quest

**Difficulty:** Hard

**Source:** Codeforces 235C "Cyclical Quest".

## Description

You are given a text string `s` and several query strings. Two strings are called
**cyclically isomorphic** if one can be obtained from the other by a cyclic shift
(rotation). For example, `"abc"`, `"bca"`, and `"cab"` are all cyclically
isomorphic.

For each query string `x`, count the number of substrings of `s` that are
cyclically isomorphic to `x`. Equivalently: over all *distinct* cyclic rotations
of `x`, sum the number of occurrences (with overlap, counted by position) of each
rotation inside `s`.

Distinct rotations matter: if `x` has period structure that makes some rotations
equal (e.g. `x = "aa"` has only one distinct rotation `"aa"`), count that
rotation only once.

## Constraints

- `1 <= len(s) <= 10^6`
- `1 <= number of queries <= 10^5`
- `1 <= len(x) <= 10^6` for each query, and the total length of all queries is at
  most `10^6`.
- All strings consist of lowercase English letters.

## Examples

### Example 1
```
Input:
  s = "baabaabaaa"
  queries = ["a", "ba", "baa", "aaba"]
Output: [7, 5, 7, 5]
Explanation:
  "a"    -> only rotation "a"; it occurs 7 times in s.
  "ba"   -> distinct rotations {"ba","ab"}; occurrences 3 + 2 = 5.
  "baa"  -> distinct rotations {"baa","aab","aba"}; occurrences 3 + 2 + 2 = 7.
  "aaba" -> distinct rotations {"aaba","abaa","baaa","aaab"};
            occurrences 2 + 2 + 1 + 0 = 5.
```

### Example 2
```
Input:
  s = "aabbaa"
  queries = ["aa", "ab", "abba"]
Output: [2, 2, 3]
Explanation:
  "aa"   -> only distinct rotation {"aa"}; "aa" occurs at indices 0 and 4 -> 2.
  "ab"   -> distinct rotations {"ab","ba"}; "ab" occurs once (index 1), "ba"
            occurs once (index 3) -> 1 + 1 = 2.
  "abba" -> distinct rotations {"abba","bbaa","baab","aabb"};
            occurrences "abba"(1) + "bbaa"(1) + "baab"(0) + "aabb"(1) = 3.
```

## Hint

Build a **Suffix Automaton** of `s` with `endpos` sizes (occurrence counts).
For a query `x`, feed the doubled string `x + x` through the automaton like a
sliding window of length `|x|` (following suffix links when the match gets too
long), and at each starting offset that achieves a full length-`|x|` match, add
the current state's occurrence count — while marking each visited state so every
distinct rotation is counted exactly once.
