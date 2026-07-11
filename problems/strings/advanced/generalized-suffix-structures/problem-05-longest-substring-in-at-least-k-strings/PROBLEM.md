# Longest Substring in At Least K Strings

**Difficulty:** Hard

**Source:** Classic generalized suffix automaton problem (a.k.a. "longest
substring common to at least `k` of the given strings"; related to SPOJ PHRASES).

## Description

You are given `n` strings and an integer `k` with `1 <= k <= n`. Find the length
of the **longest substring that occurs in at least `k` of the `n` strings**.

A substring counts once per string regardless of how many times it appears inside
that string — what matters is *how many distinct strings* contain it. If no
non-empty substring appears in at least `k` strings (only possible when even
single characters are too rare), the answer is `0`.

Return the **length** of that longest substring.

## Constraints

- `1 <= k <= n <= 10`
- Each string has length up to `10^5`.
- Total length `L = sum of lengths` up to `10^6`.
- All strings consist of lowercase English letters.

## Examples

### Example 1
```
Input:  strings = ["abcd", "bcde", "cdef"], k = 2
Output: 3
Explanation: "bcd" occurs in "abcd" and "bcde" (2 strings) -> length 3.
             "cde" occurs in "bcde" and "cdef" (2 strings) -> length 3.
             No length-4 substring appears in 2 or more strings, so answer 3.
```

### Example 2
```
Input:  strings = ["abcd", "bcde", "cdef"], k = 3
Output: 2
Explanation: "cd" is the only block appearing in all three strings
             ("ab|cd|", "b|cd|e", "|cd|ef") -> length 2. Requiring k = 3 shrinks
             the answer compared to k = 2.
```

### Example 3
```
Input:  strings = ["aaa", "aaa", "bbb"], k = 2
Output: 3
Explanation: "aaa" occurs in both of the first two strings (2 >= k) -> length 3.
             "bbb" appears in only one string, so it does not qualify.
```

## Hint

Build a **Generalized Suffix Structure** over all `n` strings and give each state
a bitmask of which strings occur there (propagate up the suffix-link tree). The
number of set bits in a state's mask is how many distinct strings contain its
substrings; the answer is the largest `len[v]` among states with **popcount >= k**.
