# Longest Common Substring of Two Strings

**Difficulty:** Hard

**Source:** Classic (SPOJ LCS; CP-Algorithms; also the generalized-suffix-array pattern).

## Description

Given two strings `A` and `B`, find the **longest contiguous substring** that
occurs in **both**. Return the substring (any one if multiple share the maximum
length); return `""` if they share no character.

**Key observation.** Concatenate the two strings with a separator that appears in
neither, e.g. `T = A + '#' + B` (with a second sentinel conceptually at the end).
Build the suffix array and LCP array of `T`. A common substring corresponds to two
suffixes of `T` that share a prefix, where **one suffix starts inside `A` and the
other starts inside `B`**. In sorted order, the best such pair is **adjacent** in
the suffix array. So scan adjacent pairs, and whenever the two suffixes come from
different source strings, take their `LCP`; the maximum over all such
"cross-source" adjacent pairs is the answer length.

## Constraints

- `1 <= len(A), len(B) <= 10^5`
- Characters are lowercase English letters; the separator `#` is guaranteed not to
  appear in `A` or `B`.
- Overlaps within a single string do not count — the two occurrences must come from
  different source strings.

## Examples

### Example 1
```
Input:  A = "banana", B = "ananas"
Output: "anana"
Explanation: "anana" is a substring of "banana" (index 1) and of "ananas"
(index 0). No longer common substring exists.
```

### Example 2
```
Input:  A = "abcde", B = "cdefg"
Output: "cde"
Explanation: "cde" occurs in both. "cdef" is not in A and "bcde" is not in B, so 3
is the maximum common length.
```

### Example 3
```
Input:  A = "abc", B = "xyz"
Output: ""
Explanation: The two strings share no character, so the longest common substring
is empty.
```

## Hint

Use **Suffix Array (prefix-doubling / DC3)** on the concatenation `A + '#' + B`
plus the **LCP array**. The answer is the maximum `LCP[i]` over adjacent sorted
suffixes whose two suffixes originate from *different* source strings.
