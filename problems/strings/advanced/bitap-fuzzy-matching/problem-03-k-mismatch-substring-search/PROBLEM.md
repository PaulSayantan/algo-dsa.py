# k-Mismatch Substring Search (Hamming Distance)

**Difficulty:** Medium

**Source:** Classic approximate string matching problem — "pattern matching with `k` mismatches" (Baeza-Yates &
Gonnet / Wu & Manber). Common in bioinformatics (short-read alignment) and competitive programming.

## Description

Given a `text`, a `pattern`, and an integer `k`, find every place where `pattern` aligns to a substring of
`text` of the **same length** with **at most `k` mismatches** (positions where the characters differ). Only
substitutions are allowed — no insertions or deletions — so this is matching under **Hamming distance**.

Return the sorted list of all **start indices** `i` such that the Hamming distance between `pattern` and
`text[i : i + len(pattern)]` is at most `k`.

This is the first genuinely *fuzzy* Bitap problem. Instead of one register you maintain `k + 1` registers
`R[0], R[1], ..., R[k]`, where a set top bit in `R[d]` means "the pattern matches the substring ending here using
at most `d` substitutions." Register `R[d]` is updated from the exact-match transition of itself **plus** a
"spend one more mismatch" contribution from `R[d-1]`.

## Constraints

- `1 <= text.length <= 10^5`
- `1 <= pattern.length <= 64` (the pattern fits in a single 64-bit machine word).
- `0 <= k <= pattern.length`
- `text` and `pattern` consist of lowercase English letters (or, in the DNA example, `A`, `C`, `G`, `T`).
- Only substitutions count toward the mismatch budget; the aligned window always has length `len(pattern)`.
- Return start indices in ascending order (empty list if none).

## Examples

### Example 1
```
Input:  text = "GCATCGCAGAGAGTATACAGTACG", pattern = "GCAGAGAG", k = 1
Output: [5]
```
Explanation: The window `text[5:13] = "GCAGAGAG"` equals the pattern exactly (Hamming distance 0), which is
within the budget `k = 1`. No other length-8 window comes within distance `1`, so the only valid start index is
`5`. (Because the budget also admits distance-1 windows, the algorithm would report any near-miss too — here
there simply are none besides the exact hit.)

### Example 2
```
Input:  text = "aaaaa", pattern = "aa", k = 1
Output: [0, 1, 2, 3]
```
Explanation: With `k = 1`, `"aa"` matches every length-2 window of `"aaaaa"` (each window is `"aa"`, distance 0,
well within budget). The valid start indices are `0, 1, 2, 3` (index 4 would need `text[4:6]`, out of range).

### Example 3
```
Input:  text = "abcde", pattern = "xbz", k = 1
Output: []
```
Explanation: Every length-3 window differs from `"xbz"` in at least two positions (e.g. `text[0:3] = "abc"` vs
`"xbz"` differs at positions 0 and 2), exceeding the budget `k = 1`, so there is no match.

## Hint

Extend **Bitap / Fuzzy Matching** to `k + 1` registers. Update from `d = 0` upward using
`R[d] = (((R[d] << 1) | 1) & peq[c]) | (prevR[d-1] << 1) | 1`, where `prevR[d-1]` is `R[d-1]`'s value *before*
this character was processed. A match with `<= k` mismatches ends where `R[k]`'s top bit is set.
