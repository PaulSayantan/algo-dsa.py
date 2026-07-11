# Longest Duplicate Substring

**Difficulty:** Hard

**Source:** LeetCode 1044 — Longest Duplicate Substring.

## Description

Given a string `s`, consider all substrings that occur **at least twice** in `s`
(the two occurrences may overlap). Return **any** duplicated substring that has the
**maximum possible length**. If `s` has no duplicated substring, return the empty
string `""`.

This is the LeetCode-framed version of "longest repeated substring": it is the same
underlying quantity — the maximum LCP between two suffixes — but stated as a
standalone judge problem, and the intended scale (`|s|` up to `3 * 10^4`) rewards a
suffix-array (or binary-search + Rabin-Karp) solution over anything quadratic.

## Constraints

- `2 <= s.length <= 3 * 10^4`
- `s` consists of lowercase English letters.
- Overlapping occurrences are allowed.
- If multiple substrings share the maximum length, returning any one of them is accepted.

## Examples

### Example 1
```
Input:  s = "banana"
Output: "ana"
Explanation: "ana" appears at index 1 and index 3 (overlapping). It is a longest
duplicated substring; "anana" appears only once, so length 3 is the maximum.
```

### Example 2
```
Input:  s = "abcd"
Output: ""
Explanation: No substring repeats, so the answer is the empty string.
```

### Example 3
```
Input:  s = "aaaaa"
Output: "aaaa"
Explanation: "aaaa" appears at index 0 and index 1 (overlapping) -> length 4.
"aaaaa" occurs only once, so 4 is the longest duplicated length.
```

## Hint

Use **Suffix Array (prefix-doubling / DC3)** with the **LCP array**: sort all
suffixes, and the answer is the shared prefix at the adjacent pair with the
maximum LCP value. (The classic alternative is binary search on the length plus
Rabin-Karp hashing.)
