# Implement strStr()

**Difficulty:** Easy

**Source:** LeetCode 28 — "Find the Index of the First Occurrence in a String" (classic `strstr`)

## Description

Given two strings `haystack` and `needle`, return the index of the **first
occurrence** of `needle` in `haystack`, or `-1` if `needle` is not part of
`haystack`.

This is the canonical single-pattern substring search. A naive scan re-examines
text characters on every mismatch; the goal here is to match the pattern against
the text using a right-to-left comparison so that a mismatch lets you slide the
pattern forward by more than one character.

By convention, if `needle` is the empty string, the answer is `0`.

## Constraints

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.
- (Extended convention used by this workspace) if `needle == ""`, return `0`.

## Examples

### Example 1
```
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and again at index 6. The first
             occurrence is at index 0.
```

### Example 2
```
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" never appears in "leetcode", so the answer is -1.
```

### Example 3
```
Input:  haystack = "GCAATGCC", needle = "GCC"
Output: 5
Explanation: Comparing right-to-left, the mismatch on the 'A'/'T' region lets
             the pattern jump ahead, and "GCC" is finally found starting at
             index 5.
```

## Hint

Preprocess the pattern and compare it against the text from right to left. Use
**Boyer–Moore (string search)**: on a mismatch, jump ahead using the
bad-character and good-suffix shift rules instead of retreating by one.
