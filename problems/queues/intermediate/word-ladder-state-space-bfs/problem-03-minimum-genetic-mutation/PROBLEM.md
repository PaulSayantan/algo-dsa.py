# Minimum Genetic Mutation

**Difficulty:** Medium

**Source:** LeetCode 433 — Minimum Genetic Mutation

## Description

A gene string is 8 characters long, each from `'A'`, `'C'`, `'G'`, `'T'`. A single mutation changes exactly one character. Given `startGene`, `endGene`, and a `bank` of valid gene strings, return the minimum number of mutations to transform `startGene` into `endGene`.

Every intermediate mutated gene (including `endGene`) must appear in `bank`. `startGene` is assumed valid and does not need to be in `bank`. Return `-1` if no valid mutation path exists.

Constraints: all strings have length 8 over `ACGT`; `0 <= len(bank) <= 10`.

## Examples

### Example 1

```
Input:  startGene="AACCGGTT", endGene="AAACGGTA", bank=["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
```

**Explanation:** `AACCGGTT -> AACCGGTA -> AAACGGTA`, two mutations, both intermediates in the bank.

## Hint

Genes are states; a neighbor flips one of the 8 characters to another base and must be in `bank`. BFS from `startGene` counts the fewest mutations.
