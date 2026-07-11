# Burrows–Wheeler Transform (BWT)

The **Burrows–Wheeler Transform** is a *reversible* permutation of a string. Given a
string `T` (conventionally terminated by a unique sentinel `$` that is
lexicographically smaller than every other character), the BWT forms all cyclic
rotations of `T`, sorts them lexicographically into the **Burrows–Wheeler Matrix
(BWM)**, and outputs the **last column** `L`. The magic is twofold:

1. **Reversibility** — despite scrambling the characters, `T` can be reconstructed
   exactly from `L` alone using the **LF-mapping** (Last-to-First correspondence).
2. **Clustering** — the transform tends to group equal characters into runs, which is
   why it is the heart of the `bzip2` compressor (BWT → move-to-front → run-length →
   entropy coding).

On top of the transform sits the **FM-index**: by precomputing, for the last column,
a `C[]` array (count of characters smaller than each symbol) and a `Occ`/rank
structure, you can count and locate every occurrence of a pattern `P` in `T` in
`O(|P|)` time using **backward search** — the workhorse behind read aligners like
Bowtie and BWA in bioinformatics.

## When to reach for it

- You need a **self-index**: a compressed representation of a text that *also* answers
  substring queries without decompressing.
- You want **lossless compression** that exploits local context (bzip2 family).
- You must do **exact pattern matching / counting** on a huge text (e.g. a genome)
  with a memory budget close to the size of the text itself.

## Complexity at a glance

| Operation | Time | Space | Notes |
|---|---|---|---|
| Build BWT (naive rotations) | `O(n^2 log n)` | `O(n^2)` | sort explicit rotations |
| Build BWT (via suffix array) | `O(n)`–`O(n log n)` | `O(n)` | `L[i] = T[SA[i]-1]` |
| Inverse BWT (LF-mapping) | `O(n)` | `O(n + σ)` | walk the LF chain once |
| Build LF / `C` + `Occ` | `O(n + σ)` | `O(n)` | σ = alphabet size |
| Count occurrences of `P` (FM-index) | `O(\|P\|)` | `O(1)` extra | backward search |
| Locate all `k` occurrences | `O(\|P\| + k)` | `O(n)` | needs suffix array (or sampled) |

Here `n = |T|` and `σ` is the alphabet size.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Compute the BWT](problem-01-compute-bwt/PROBLEM.md) | Build the last column from sorted cyclic rotations | Easy |
| 2 | [Inverse the BWT](problem-02-inverse-bwt/PROBLEM.md) | Reconstruct the original string from `L` using LF-mapping | Medium |
| 3 | [Last-to-First Mapping](problem-03-last-to-first-mapping/PROBLEM.md) | Compute the LF array that links the last column to the first | Medium |
| 4 | [Count Pattern Occurrences (FM-index)](problem-04-count-pattern-occurrences-fm-index/PROBLEM.md) | Backward search to count matches of many patterns | Hard |
| 5 | [Locate Pattern Positions](problem-05-locate-pattern-positions/PROBLEM.md) | Report every start index of a pattern via FM-index + suffix array | Hard |

Work them top to bottom: each problem reuses machinery from the previous one.
