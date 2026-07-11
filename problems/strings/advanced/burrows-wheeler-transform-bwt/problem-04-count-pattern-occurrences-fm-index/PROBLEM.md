# Count Pattern Occurrences with the FM-index

**Difficulty:** Hard

**Source:** Rosalind "Implement BWMatching" (BA9L); Ferragina–Manzini FM-index backward search.

## Description

You are given the Burrows–Wheeler Transform `bwt` of a sentinel-terminated text, and a
list of query `patterns`. For each pattern, report **how many times it occurs as a
substring** of the original text.

The naive approach would reconstruct the text and run a matcher per pattern. Instead,
build an **FM-index** on top of the BWT and answer each query with **backward search** in
`O(|pattern|)` time — regardless of how long the text is.

Backward search maintains a half-open range `[top, bottom]` of rows in the
Burrows–Wheeler Matrix whose row prefixes match the suffix of the pattern processed so
far. Process the pattern **right to left**; for the current character `c` update:

```
top    = C[c] + Occ(c, top)          # Occ(c, i) = # of c in bwt[0..i-1]
bottom = C[c] + Occ(c, bottom + 1) - 1
```

where `C[c]` is the number of characters in the text strictly smaller than `c`. If at
any step `top > bottom`, the pattern does not occur (count `0`). After consuming the
whole pattern, the number of matches is `bottom - top + 1`.

Return a list of counts, one per pattern, in the same order as the input.

## Constraints

- `1 <= len(bwt) <= 10^5`
- `bwt` contains exactly one `$`, the lexicographically smallest character.
- `1 <= len(patterns) <= 10^4`, and each pattern has length `>= 1`.
- A pattern may contain characters that never appear in the text; such a pattern has
  count `0`.
- The sentinel `$` never appears inside a query pattern.

## Examples

### Example 1

```
Input:  bwt = "annb$aa"                       # BWT of "banana$"
        patterns = ["ana", "ban", "na", "x"]
Output: [2, 1, 2, 0]
```

Explanation: In `banana` the substring `ana` occurs at indices 1 and 3 (count 2), `ban`
once, `na` at indices 2 and 4 (count 2), and `x` never appears (count 0).

### Example 2

```
Input:  bwt = "ipssm$pissii"                  # BWT of "mississippi$"
        patterns = ["iss", "ss", "ppi", "z"]
Output: [2, 2, 1, 0]
```

Explanation: In `mississippi`, `iss` occurs twice, `ss` occurs twice, `ppi` once, and
`z` never — matching `[2, 2, 1, 0]`.

## Hint

Use the **Burrows–Wheeler Transform (BWT)** with an **FM-index**: precompute the `C[]`
array and a rank function `Occ(c, i)`, then run **backward search** over each pattern,
shrinking a `[top, bottom]` row range from the last character to the first. The count is
the size of the surviving range.
