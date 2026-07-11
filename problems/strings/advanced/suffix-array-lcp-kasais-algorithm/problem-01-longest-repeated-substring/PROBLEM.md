# Longest Repeated Substring

**Difficulty:** Medium

Source: Classic (CLRS / competitive programming; closely related to LeetCode 1044 "Longest Duplicate Substring")

## Description

Given a string `s`, find the **longest substring that appears at least twice**
in `s`. The two occurrences are allowed to overlap (for example, in `"aaaa"`
the substring `"aaa"` occurs starting at index 0 and index 1, which overlap).

Return the repeated substring itself. If no character repeats, there is no
repeated substring, so return the empty string `""`.

If several repeated substrings share the maximum length, returning any one of
them is acceptable.

## Constraints

- `1 <= len(s) <= 10^5`
- `s` consists of lowercase English letters.
- A "substring" is a contiguous, non-empty slice of `s`.
- Overlapping occurrences count as two occurrences.

## Examples

### Example 1
```
Input:  s = "banana"
Output: "ana"
Explanation: The suffixes sorted lexicographically are
  a, ana, anana, banana, na, nana.
  Adjacent sorted suffixes "ana" and "anana" share the prefix "ana" of length 3,
  which is the largest shared prefix of any two suffixes, so "ana" (occurring at
  indices 1 and 3) is the longest repeated substring.
```

### Example 2
```
Input:  s = "abcd"
Output: ""
Explanation: Every character is unique, so no substring occurs twice. The
  longest repeated substring has length 0.
```

### Example 3
```
Input:  s = "aabcaabdaab"
Output: "aab"
Explanation: "aab" occurs at indices 0, 4, and 8. No substring of length 4 or
  more repeats, so "aab" (length 3) is the answer.
```

## Hint

Build the **Suffix Array**, then compute the **LCP array with Kasai's
algorithm**. Two equal substrings are exactly a common prefix of two suffixes;
the longest such repeat is the maximum value in the LCP array, and the suffix it
belongs to tells you where the substring starts.
