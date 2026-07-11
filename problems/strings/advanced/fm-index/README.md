# FM-Index

## What it is

The **FM-Index** (Ferragina–Manzini index) is a *compressed, self-indexing*
full-text data structure built on top of the **Burrows–Wheeler Transform (BWT)**.
Given a text `T` of length `n`, it lets you answer substring queries — *how many
times does pattern `P` occur?* (**count**) and *where does it occur?* (**locate**)
— in time proportional to the pattern length, while occupying space close to the
compressed size of the text itself.

The engine is a routine called **backward search**. It relies on two small
precomputed tables over the BWT string `L`:

- `C[c]` — the number of characters in `T` that are lexicographically **smaller**
  than `c` (equivalently, the index of the first row in the sorted suffix matrix
  whose first character is `c`).
- `Occ(c, i)` — the number of occurrences of character `c` in `L[0 .. i-1]`
  (a **rank** query over the BWT). In practice this is stored as a wavelet tree
  or blocked bit-vectors so each rank is `O(1)` or `O(log sigma)`.

Backward search maintains a half-open interval `[sp, ep)` of rows in the sorted
suffix matrix (equivalently, positions in the suffix array) whose suffixes start
with the pattern suffix processed so far. Reading `P` **right to left**, each
character `c` updates the interval with the **LF-mapping** step:

```
sp <- C[c] + Occ(c, sp)
ep <- C[c] + Occ(c, ep)
```

When the whole pattern is consumed, `ep - sp` is the number of occurrences. If
the interval ever becomes empty (`sp >= ep`), the pattern does not occur.

## When to reach for it

Reach for an FM-Index when you have **one (large, static) text** and must answer
**many substring queries** under a tight space budget:

- Counting / locating occurrences of arbitrary patterns (search engines, `grep`
  over a fixed corpus).
- Read alignment in bioinformatics (`bowtie`, `BWA`): aligning millions of short
  DNA reads against a reference genome, including **approximate** matching with a
  few mismatches via branching backward search.
- Full-text search over a compressed corpus where storing an uncompressed suffix
  tree/array would be too big.
- Document-listing / "which documents contain P" over a concatenated corpus.

If you only need to match one pattern once, KMP or Z-algorithm is simpler. The
FM-Index wins when the **index is built once** and reused across queries, and
when **space** matters.

## Typical complexity

Let `n = |T|`, `m = |P|`, `sigma` the alphabet size, `occ` the number of
occurrences, and `s` the suffix-array sample rate.

| Operation | Time | Space |
|-----------|------|-------|
| Build (BWT via suffix array) | `O(n)` (SA-IS) or `O(n log n)` (doubling) | `O(n)` |
| `count(P)` | `O(m)` with `O(1)`-rank | `O(n log sigma)` bits |
| `locate(P)` | `O(m + occ * s)` | + `O((n/s) log n)` bits of SA samples |
| `extract` a substring | `O(len * s)` | — |

The headline property is **space**: `n * H_k(T) + o(n log sigma)` bits — close to
the entropy-compressed size of the text — while still supporting search. The
teaching implementations in this folder favor clarity over the bit-packing that
achieves those bounds (they store plain rank tables and a full suffix array).

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Count Substring Occurrences](problem-01-count-substring-occurrences/PROBLEM.md) | Answer many "how many times does `P` occur in `T`?" queries with backward search | Medium |
| 2 | [Locate Substring Occurrences](problem-02-locate-substring-occurrences/PROBLEM.md) | Report every start position of `P` in `T` using the BWT interval + suffix array | Medium |
| 3 | [Longest Matchable Suffix](problem-03-longest-matchable-suffix/PROBLEM.md) | Longest suffix of `P` that appears in `T`, via partial backward search | Medium |
| 4 | [Approximate Matching (k Mismatches)](problem-04-approximate-matching-k-mismatches/PROBLEM.md) | Count alignments of `P` in `T` allowing up to `k` mismatches via branching backward search | Hard |
| 5 | [Document Containment Count](problem-05-document-containment-count/PROBLEM.md) | Over a concatenated corpus, count how many documents contain `P` | Hard |
