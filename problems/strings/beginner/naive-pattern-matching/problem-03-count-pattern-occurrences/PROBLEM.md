# Count Pattern Occurrences (Including Overlaps)

**Difficulty:** Easy

**Source:** Classic string exercise (a counting variant of GeeksforGeeks
"Naive algorithm for Pattern Searching")

## Description

Given a text string `text` and a non-empty pattern string `pattern`, count how many
times `pattern` occurs in `text`. **Overlapping occurrences are counted separately.**

Return the total number of starting indices `i` such that
`text[i : i + len(pattern)] == pattern`.

## Constraints

- `1 <= len(text) <= 10^4`
- `1 <= len(pattern) <= 10^4`
- `text` and `pattern` consist of printable ASCII characters.
- If `len(pattern) > len(text)`, the answer is `0`.

## Examples

### Example 1

```
Input:  text = "AABAACAADAABAABA", pattern = "AABA"
Output: 3
```

**Explanation:** `"AABA"` starts at indices `0`, `9`, and `12`
(`[AABA]ACAAD[AABA][AABA]` — note the last two overlap at index 12), giving `3`
matches.

### Example 2

```
Input:  text = "aaaa", pattern = "aa"
Output: 3
```

**Explanation:** `"aa"` occurs at indices `0`, `1`, and `2`
(`[aa]aa`, `a[aa]a`, `aa[aa]`). Overlapping matches all count, so the answer is `3`.

### Example 3

```
Input:  text = "abcabc", pattern = "xyz"
Output: 0
```

**Explanation:** `"xyz"` never appears in `"abcabc"`, so the count is `0`.

## Hint

Use **Naive Pattern Matching**, but instead of stopping at the first match, keep a
counter and continue sliding by **one** position after every alignment — sliding by one
(not by `len(pattern)`) is what lets overlapping matches be counted.
