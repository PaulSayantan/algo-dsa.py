# Repeated DNA Sequences

**Difficulty:** Medium

**Source:** LeetCode 187 — "Repeated DNA Sequences"

## Description

The DNA sequence is composed of a series of nucleotides abbreviated as `'A'`,
`'C'`, `'G'`, and `'T'`.

- For example, `"ACGAATTCCG"` is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string `s` that represents a DNA sequence, return **all the
`10`-letter-long sequences (substrings) that occur more than once** in a DNA
molecule. You may return the answer in **any order**.

The natural approach is to slide a window of length 10 across `s`, hash each
window with a **rolling hash**, and use a set/counter of hashes to detect which
windows appear more than once.

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is either `'A'`, `'C'`, `'G'`, or `'T'`.

## Examples

### Example 1

```
Input:  s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]
Explanation:
  "AAAAACCCCC" appears at indices 0 and 10.
  "CCCCCAAAAA" appears at indices 5 and 15.
  Both 10-letter windows occur more than once, so both are returned.
```

### Example 2

```
Input:  s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
Explanation:
  The string has length 13, so its 10-letter windows are
  "AAAAAAAAAA" starting at indices 0, 1, 2, and 3 — the same sequence repeated.
  Since it occurs more than once, it is returned exactly once.
```

### Example 3

```
Input:  s = "ACGTACGT"
Output: []
Explanation:
  The string has length 8, which is shorter than 10, so there is no
  10-letter window at all and the answer is empty.
```

## Hint

Every candidate substring has the *same fixed length* (10). Slide a length-10
window and maintain a **Rabin–Karp rolling hash**; store seen hashes in a set
and add a window to the answer the moment its hash is seen a second time.
