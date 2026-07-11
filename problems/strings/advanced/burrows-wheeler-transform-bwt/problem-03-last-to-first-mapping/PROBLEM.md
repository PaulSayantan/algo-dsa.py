# Last-to-First (LF) Mapping

**Difficulty:** Medium

**Source:** Compeau & Pevzner, *Bioinformatics Algorithms* (the "Last-to-First" primitive underlying BWMatching); classic FM-index building block.

## Description

The **Last-to-First mapping** (LF-mapping) is the core primitive that powers both the
inverse BWT and the FM-index. Given the last column `L = bwt` of a Burrows–Wheeler
Matrix, define the first column `F` as `sorted(L)`.

For each row index `i`, `LF(i)` is the row index in the **first** column that holds the
**same physical occurrence** of the character `L[i]`. Concretely, if `L[i]` is the `k`-th
occurrence of character `c` when scanning `L` from the top, then `LF(i)` is the position
of the `k`-th occurrence of `c` in `F`. Because `F` is sorted, that position equals:

```
LF(i) = C[c] + (number of c's in L[0 .. i-1])
```

where `C[c]` is the number of characters in `L` strictly smaller than `c` (the offset of
`c`'s block in the sorted first column).

Return the full array `LF` of length `n` where `LF[i]` is defined as above.

## Constraints

- `1 <= len(bwt) <= 10^5`
- `bwt` contains exactly one `$`, the lexicographically smallest character.
- `LF` is a permutation of `range(len(bwt))` (it is a bijection on rows).
- `LF[i]` is a 0-based index.

## Examples

### Example 1

```
Input:  bwt = "annb$aa"          # BWT of "banana$"
Output: [1, 5, 6, 4, 0, 2, 3]
```

Explanation: `F = sorted("annb$aa") = "$aaabnn"`, so `C = {'$':0, 'a':1, 'b':4, 'n':5}`.
- `i=0`, `L[0]='a'`, 0 earlier a's → `1 + 0 = 1`
- `i=1`, `L[1]='n'`, 0 earlier n's → `5 + 0 = 5`
- `i=2`, `L[2]='n'`, 1 earlier n  → `5 + 1 = 6`
- `i=3`, `L[3]='b'`, 0 earlier b's → `4 + 0 = 4`
- `i=4`, `L[4]='$'`, 0 earlier $  → `0 + 0 = 0`
- `i=5`, `L[5]='a'`, 1 earlier a  → `1 + 1 = 2`
- `i=6`, `L[6]='a'`, 2 earlier a's → `1 + 2 = 3`

giving `[1, 5, 6, 4, 0, 2, 3]`.

### Example 2

```
Input:  bwt = "abba$aa"          # BWT of "abaaba$"
Output: [1, 5, 6, 2, 0, 3, 4]
```

Explanation: `F = "$aaaabb"`, `C = {'$':0, 'a':1, 'b':5}`. Applying
`LF(i) = C[L[i]] + rank_before(i)` to each position produces `[1, 5, 6, 2, 0, 3, 4]`.

## Hint

Use the **Burrows–Wheeler Transform (BWT)** structure: compute `C[c]` from character
counts, then sweep `L` once keeping a running tally of how many times each character has
appeared so far — that running rank is exactly the offset within character `c`'s block
in the first column.

