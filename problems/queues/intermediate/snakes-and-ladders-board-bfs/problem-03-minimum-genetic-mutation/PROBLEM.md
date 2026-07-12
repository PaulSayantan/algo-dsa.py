# Minimum Genetic Mutation

**Difficulty:** Medium

**Source:** LeetCode 433 — Minimum Genetic Mutation

## Description

A gene string is 8 characters long, each from `'A'`, `'C'`, `'G'`, `'T'`. A single mutation changes exactly one character to one of the other three. A mutation is only valid if the resulting gene string appears in the mutation `bank`.

Given `startGene`, `endGene`, and the `bank` of valid gene strings, return the minimum number of mutations needed to transform `startGene` into `endGene`, or `-1` if there is no such path.

Constraints: `startGene` and `endGene` have length 8 over `{A,C,G,T}`; `0 <= bank.length <= 10`. `startGene` is assumed valid (it need not be in the bank).

## Examples

### Example 1

```
Input:  startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
```

**Explanation:** `AACCGGTT -> AACCGGTA -> AAACGGTA`, and each intermediate string is in the bank.

## Hint

Each valid gene is a node; edges connect genes one character apart that live in the bank. BFS from `startGene` gives the fewest mutations to `endGene`.
