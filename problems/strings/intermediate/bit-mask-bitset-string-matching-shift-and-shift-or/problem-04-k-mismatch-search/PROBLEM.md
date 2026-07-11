# k-Mismatch Search (Hamming Distance)

**Difficulty:** Medium

**Source:** Classic approximate string matching — "matching with `k` mismatches"
(Baeza-Yates & Gonnet bit-parallel formulation; a staple of bioinformatics /
competitive-programming approximate search).

## Description

Given a `text`, a `pattern`, and an integer `k`, return all start indices `i` such
that the length-`m` window `text[i .. i+m-1]` differs from `pattern` in **at most
`k` positions**. "Differs in a position" means the characters at the same offset are
unequal — this is **Hamming distance** (substitutions only; the window and the
pattern always have the same length `m`, so no insertions or deletions).

When `k = 0` this reduces to exact matching. As `k` grows you tolerate more
single-character substitutions. Return the start indices in increasing order.

Solve it with **bit-parallelism**: keep `k+1` state words `R[0..k]`, where `R[d]`
tracks matches achievable with at most `d` mismatches, and advance them all with
one pass over the text.

## Constraints

- `1 <= len(text) <= 10^5`
- `1 <= len(pattern) <= len(text)`
- `0 <= k <= len(pattern)`
- Characters are printable ASCII.

## Examples

### Example 1
```
Input:  text = "abcde", pattern = "xbcdx", k = 2
Output: [0]
Explanation: Aligning "xbcdx" with window "abcde" at index 0, the mismatches are at
             position 0 ('x' vs 'a') and position 4 ('x' vs 'e') -> Hamming distance
             2 <= k. So index 0 qualifies. (It is the only length-5 window.)
```

### Example 2
```
Input:  text = "abcde", pattern = "xbcdx", k = 1
Output: []
Explanation: The same alignment has Hamming distance 2, which exceeds k = 1, so
             there is no qualifying window and the answer is empty.
```

### Example 3
```
Input:  text = "hello", pattern = "jello", k = 1
Output: [0]
Explanation: "hello" vs "jello" differ only at position 0 ('h' vs 'j') -> distance 1
             <= k, so index 0 qualifies.
```

## Hint

Use **Bit-mask / Bitset String Matching (Shift-And / Shift-Or)**. Maintain a ladder
of `k+1` state words. For each text character `c`, `R[0]` updates like plain
Shift-And, and for `d >= 1`:
`R[d] = (((R_old[d] << 1) | 1) & B[c]) | ((R_old[d-1] << 1) | 1)` — the first term
is "match this character", the second is "spend one more mismatch and advance
anyway". A window ending here is within `k` mismatches when the top bit of `R[k]` is
set.
