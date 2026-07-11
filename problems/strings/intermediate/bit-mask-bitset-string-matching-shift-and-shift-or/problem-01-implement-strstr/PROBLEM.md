# Implement strStr()

**Difficulty:** Easy

**Source:** LeetCode 28 — Find the Index of the First Occurrence in a String

## Description

Given two strings `haystack` and `needle`, return the index of the **first**
occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of
`haystack`.

Occurrences may not skip characters: `needle` must appear as a **contiguous
substring** of `haystack`. If `needle` is the empty string, return `0` (it
matches at the very beginning).

While the classic solutions are KMP or Rabin-Karp, this exercise asks you to solve
it with **bit-parallelism**: pack a matching state for every prefix of `needle`
into the bits of one integer and advance them all at once as you scan `haystack`.

## Constraints

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English letters.
- (For the bit-parallel approach it is easiest when `needle.length` is small, e.g.
  `<= 64`, so it fits a single machine word; Python's arbitrary-precision integers
  remove this restriction in practice.)

## Examples

### Example 1
```
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and also at index 6. The first occurrence is at index 0.
```

### Example 2
```
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" never appears in "leetcode" (the 'o' breaks the match), so return -1.
```

### Example 3
```
Input:  haystack = "hello", needle = "ll"
Output: 2
Explanation: "ll" first appears starting at index 2 ("he[ll]o").
```

## Hint

Use **Bit-mask / Bitset String Matching (Shift-And / Shift-Or)**. Precompute, for
each character, a bitmask marking the positions where it occurs in `needle`. Keep a
running state word `D`; for each text character do `D = ((D << 1) | 1) & B[c]`. When
the bit at position `len(needle) - 1` becomes set, the pattern ends at the current
index.
