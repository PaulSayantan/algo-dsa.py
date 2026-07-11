# Locate Pattern Positions with the FM-index

**Difficulty:** Hard

**Source:** Rosalind "Find All Occurrences of Collection of Patterns in a String" / "Implement BetterBWMatching + locate" (BA9M family); FM-index + suffix-array locate.

## Description

Given a text `text` (terminated by a unique smallest sentinel `$`) and a query `pattern`,
report **every start index** in `text` where `pattern` occurs, as a **sorted** list of
0-based indices.

Counting (Problem 4) tells you *how many* matches there are; locating tells you *where*.
The FM-index narrows the matches to a contiguous row range `[top, bottom]` of the
Burrows–Wheeler Matrix via backward search. To convert those rows into text positions
you use the **suffix array**: row `i` of the sorted matrix corresponds to the suffix
starting at `SA[i]`, so each start position is `SA[j]` for `j` in `[top, bottom]`.

Build the pieces yourself:

1. The **suffix array** `SA` of `text`.
2. The **BWT** `L`, where `L[i] = text[SA[i] - 1]`.
3. The **FM-index** (`C[]` and rank `Occ`) over `L`.
4. **Backward search** the pattern to obtain `[top, bottom]`.
5. Return `sorted(SA[top .. bottom])` (empty list if there is no match).

The sentinel position (index `len(text) - 1`) is never a valid start for a non-empty
pattern, so it will not appear in the answer.

## Constraints

- `2 <= len(text) <= 10^5` (the last character is `$`).
- `text` contains exactly one `$`, the lexicographically smallest character.
- `1 <= len(pattern) <= len(text)`; the pattern does not contain `$`.
- Output indices are 0-based, sorted ascending; return `[]` when there is no occurrence.

## Examples

### Example 1

```
Input:  text = "banana$", pattern = "ana"
Output: [1, 3]
```

Explanation: `banana` — positions 1 (`b[ana]na`) and 3 (`ban[ana]`) start an `ana`.
Backward search returns a row range of size 2; mapping those rows through the suffix
array `SA = [6, 5, 3, 1, 0, 4, 2]` yields start indices `{1, 3}`.

### Example 2

```
Input:  text = "mississippi$", pattern = "issi"
Output: [1, 4]
```

Explanation: `mississippi` contains `issi` at index 1 (`m[issi]ssippi`) and index 4
(`miss[issi]ppi`); these overlap and both are reported. `SA[top..bottom]` sorted gives
`[1, 4]`.

### Example 3

```
Input:  text = "banana$", pattern = "z"
Output: []
```

Explanation: `z` never appears, so the backward-search range is empty and no positions
are returned.

## Hint

Use the **Burrows–Wheeler Transform (BWT)** with an **FM-index** to shrink the match to a
row interval `[top, bottom]` via backward search, then translate those rows into text
positions with the **suffix array** (`position = SA[row]`). Sort before returning.
