# Approximate Search Within k Edits (Levenshtein Distance)

**Difficulty:** Hard

**Source:** Wu & Manber, "Fast Text Searching Allowing Errors" (CACM 1992) — the algorithm behind GNU `agrep`.
The canonical "approximate string matching with `k` differences" problem.

## Description

Given a `text`, a `pattern`, and an integer `k`, find every position in `text` where the pattern occurs allowing
up to `k` **edits**, where an edit is an insertion, deletion, or substitution of a single character (i.e. the
**Levenshtein / edit distance** between the pattern and the matched substring is at most `k`). Unlike the
Hamming version (Problem 3), the matched substring may be **shorter or longer** than the pattern, because
insertions and deletions change the length.

Because a given end position can be reached by matched substrings of several lengths, the standard and
unambiguous way to report results is by **end position**: return the sorted list of all indices `e` such that
**some** substring of `text` ending at index `e` (inclusive) is within edit distance `k` of the pattern.

The Bitap solution keeps `k + 1` registers, but the recurrence now also models insertions and deletions with
extra shifts and ORs. The registers are initialized to `R[d] = (1 << d) - 1` (the low `d` bits set), which
encodes "you may delete the first `d` characters of the pattern for free" at the start.

## Constraints

- `1 <= text.length <= 10^5`
- `1 <= pattern.length <= 64` (the pattern fits in a single 64-bit machine word).
- `0 <= k <= pattern.length`
- `text` and `pattern` consist of printable ASCII characters (lowercase letters and DNA bases in the examples).
- Report **end positions** (0-based, inclusive) in ascending order; return an empty list if there is no match.

## Examples

### Example 1
```
Input:  text = "approximatly", pattern = "approximately", k = 1
Output: [11]
```
Explanation: The text is the pattern with the single letter `e` deleted (`approximat[e]ly` → `approximatly`).
That one deletion is within budget `k = 1`, and the closest matching substring ends at the last character, index
`11`. No shorter prefix reaches distance `<= 1`, so the only end position is `11`.

### Example 2
```
Input:  text = "banana", pattern = "anna", k = 1
Output: [3, 5]
```
Explanation: Two windows land within one edit of `"anna"`. Ending at index 3, the substring `"ana"` (= `text[1:4]`)
becomes `"anna"` with one insertion. Ending at index 5, the substring `"ana"` (= `text[3:6]`) is again one
insertion away. Both are within `k = 1`, so the end positions are `3` and `5`.

### Example 3
```
Input:  text = "hello", pattern = "help", k = 1
Output: [2, 3]
```
Explanation: Ending at index 2, the substring `"hel"` (= `text[0:3]`) needs one insertion (`help` has an extra
`p`), distance 1. Ending at index 3, the substring `"hell"` (= `text[0:4]`) needs one substitution (`l` → `p`),
distance 1. Both are within budget, so the end positions are `2` and `3`.

## Hint

Use the full **Bitap / Fuzzy Matching** Wu–Manber recurrence with `k + 1` registers initialized to
`R[d] = (1 << d) - 1`. Per character:
`R[d] = (((R[d] << 1) | 1) & peq[c]) | ((oldR[d-1] | R[d-1]) << 1) | oldR[d-1] | 1`,
where the three added terms encode substitution, insertion, and deletion. A match ends at index `e` when the top
bit of `R[k]` is set.
