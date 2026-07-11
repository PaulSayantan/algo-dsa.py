# Fuzzy Substring Search (Wu-Manber, k Edits)

**Difficulty:** Hard

**Source:** Wu & Manber, "Fast Text Searching Allowing Errors" (CACM 1992) — the
bit-parallel approximate-matching algorithm behind `agrep`.

## Description

Given a `text`, a `pattern`, and an integer `k`, find every position where the
pattern approximately matches, allowing up to `k` **edit operations**
(insertions, deletions, and substitutions — i.e. **Levenshtein distance**).

Concretely, return all **end positions** `pos` in `text` such that **some**
substring of `text` ending at index `pos` is within edit distance `k` of `pattern`.
(Reporting end positions is the natural output of the streaming automaton; because a
match of variable length can end at `pos`, end positions are unambiguous while start
positions are not.) Return the end positions in increasing order.

Unlike the `k`-mismatch problem, the matched substring may be **shorter or longer**
than the pattern, since insertions and deletions change the length. When `k = 0`
this degenerates to exact matching (end positions of exact occurrences).

Solve it with the **Wu-Manber** bit-parallel recurrence: maintain `k+1` state words
`R[0..k]` and update each with terms for match, substitution, deletion, and
insertion in `O(1)` per level per character.

## Constraints

- `1 <= len(text) <= 10^5`
- `1 <= len(pattern) <= len(text)` (bit-parallel is ideal when `len(pattern) <= 64`)
- `0 <= k <= len(pattern)`
- Characters are printable ASCII.

## Examples

### Example 1
```
Input:  text = "survey", pattern = "surgery", k = 2
Output: [5]
Explanation: The substring "survey" (ending at index 5, the last character) is within
             edit distance 2 of "surgery": insert 'g' and insert 'r' (equivalently,
             two edits) turns "survey" into "surgery". So end position 5 qualifies.
             No shorter substring ending earlier gets within 2 edits.
```

### Example 2
```
Input:  text = "hello", pattern = "hallo", k = 1
Output: [4]
Explanation: The substring "hello" (ending at index 4) differs from "hallo" by a
             single substitution ('e' -> 'a'), edit distance 1 <= k, so end position
             4 qualifies. With k = 0 the answer would be empty.
```

### Example 3
```
Input:  text = "dog", pattern = "cat", k = 1
Output: []
Explanation: Every substring of "dog" is at edit distance >= 2 from "cat" (e.g.
             "dog" vs "cat" needs 3 substitutions), so no end position is within 1
             edit and the result is empty.
```

## Hint

Use **Bit-mask / Bitset String Matching (Shift-And / Shift-Or)** in its Wu-Manber
form. Keep `R[0..k]`, initialize `R[d] = (1 << d) - 1` (a length-`d` deletion head
start), and for each text character combine four terms per level: match
`((R_old[d] << 1) | 1) & B[c]`, substitution `(R_old[d-1] << 1) | 1`, deletion
`R_old[d-1]`, and insertion `R_new[d-1] << 1`. A match ends at `pos` when the top
bit of `R[k]` is set.
