# Sequence Reconstruction

**Difficulty:** Medium

**Source:** LeetCode 444 — Sequence Reconstruction

## Description

You are given an integer array `nums` of length `n` where `nums` is a permutation of the integers `1..n`, and a list of integer arrays `sequences`, where each `sequences[i]` is a subsequence of `nums`.

Return `True` if `nums` is the **unique** shortest supersequence that can be reconstructed from `sequences` — that is, `nums` is the only sequence that is a valid supersequence of every array in `sequences` — otherwise return `False`.

Constraints: `1 <= n`, every value in `sequences` lies in `1..n`, and any value not in `1..n` makes reconstruction impossible.

## Examples

### Example 1

```
Input:  nums = [1, 2, 3], sequences = [[1, 2], [1, 3]]
Output: false
```

**Explanation:** `[1, 3, 2]` is also a valid supersequence, so the reconstruction is not unique.

### Example 2

```
Input:  nums = [1, 2, 3], sequences = [[1, 2], [1, 3], [2, 3]]
Output: true
```

**Explanation:** The edges `1->2`, `1->3`, `2->3` force the single order `[1, 2, 3]`.

## Hint

Build a graph from consecutive pairs of each sequence and run Kahn's algorithm; the reconstruction is unique only if the in-degree-0 queue holds exactly one node at every step and the emitted order equals `nums`.
