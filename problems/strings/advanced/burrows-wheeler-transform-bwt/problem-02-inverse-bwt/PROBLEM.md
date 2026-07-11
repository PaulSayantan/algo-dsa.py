# Inverse the Burrows–Wheeler Transform

**Difficulty:** Medium

**Source:** Rosalind "Reconstruct a String from its Burrows-Wheeler Transform" (BA9J); classic stringology exercise.

## Description

You are given `bwt`, the last column `L` of the Burrows–Wheeler Matrix of some unknown
string `text` (which was terminated by a unique smallest sentinel `$`). Reconstruct and
return the original `text`, sentinel included.

The transform is reversible even though it looks like a scramble. The trick is the
**Last-to-First (LF) mapping**. Two facts make it work:

- The **first column** `F` of the matrix is simply `L` sorted (every rotation appears
  once, so the multiset of first characters equals the multiset of last characters).
- **Rank preservation:** the `k`-th occurrence of a character `c` in the last column `L`
  corresponds to the `k`-th occurrence of `c` in the first column `F`. This holds
  because rows are sorted, so all rows starting with `c` keep their relative order in
  both columns.

Using this, `LF(i)` maps row `i` (whose *last* character is `L[i]`) to the row where that
same character sits in the *first* column. Repeatedly following the sentinel around the
cycle rebuilds `text` one character at a time.

## Constraints

- `1 <= len(bwt) <= 10^5`
- `bwt` contains exactly one `$`, which is the lexicographically smallest character.
- `bwt` is a valid Burrows–Wheeler Transform of some sentinel-terminated string, so a
  unique original string exists.
- The returned string has the same length as `bwt` and ends with `$`.

## Examples

### Example 1

```
Input:  bwt = "annb$aa"
Output: "banana$"
```

Explanation: Sorting `L = "annb$aa"` gives the first column `F = "$aaabnn"`. Following
the LF-mapping from the row containing `$` reconstructs `b, a, n, a, n, a` and finally
the sentinel — the string `"banana$"`.

### Example 2

```
Input:  bwt = "ard$rcaaaabb"
Output: "abracadabra$"
```

Explanation: This is the inverse of Example 2 from Problem 1. The LF walk reproduces
`"abracadabra$"` exactly, confirming the transform is a genuine bijection.

### Example 3

```
Input:  bwt = "AA$"
Output: "AA$"
```

Explanation: `F = "$AA"`. The LF-mapping walk starting from `$` yields `A, A`, giving
back `"AA$"`.

## Hint

Use the **Burrows–Wheeler Transform (BWT)** inverse via the **LF-mapping**: build the
first column by sorting, precompute for each row where its last-column character lands
in the first column (the `k`-th `c` in `L` ↔ the `k`-th `c` in `F`), then walk that
mapping starting at the sentinel row.
