# Count Distinct Common Substrings

**Difficulty:** Hard

**Source:** Classic generalized suffix automaton problem (substring-set
intersection counting; appears on various competitive-programming judges).

## Description

You are given a list of `k` strings. Consider every string `t` that is a
substring of **all** `k` inputs simultaneously. Count how many **distinct** such
common substrings exist.

Equivalently, let `S_i` be the set of substrings of string `i`. Return
`|S_1 ∩ S_2 ∩ ... ∩ S_k|` (excluding the empty string).

Note the difference from "longest common substring": here you must count the
*number of distinct* common substrings, not just find the longest one.

## Constraints

- `1 <= k <= 10` strings.
- Each string has length up to `10^5`.
- Total length `L = sum of lengths` up to `10^6`.
- All strings consist of lowercase English letters.

## Examples

### Example 1
```
Input:  ["ab", "ab"]
Output: 3
Explanation: Both strings are "ab", whose substrings are {"a", "b", "ab"}.
             The intersection is all 3 of them.
```

### Example 2
```
Input:  ["aaa", "aa"]
Output: 2
Explanation: Substrings of "aaa": {"a","aa","aaa"}; of "aa": {"a","aa"}.
             Intersection = {"a","aa"} -> 2 distinct common substrings.
             ("aaa" is not a substring of "aa".)
```

### Example 3
```
Input:  ["abab", "baba"]
Output: 6
Explanation: Common substrings are {"a","b","ab","ba","aba","bab"} -> 6 distinct.
             (No length-4 substring is shared: "abab" != "baba".)
```

## Hint

Build a **Generalized Suffix Structure** over all `k` strings and mark each state
with the set of source strings occurring there (propagate up the suffix-link
tree). A state whose mask is all-ones contributes `len[v] - len[link[v]]` distinct
substrings that are common to everyone; sum that over all all-ones states.
