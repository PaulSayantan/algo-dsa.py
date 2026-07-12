# Distant Barcodes

**Difficulty:** Medium

**Source:** LeetCode 1054 — Distant Barcodes

## Description

Given an array `barcodes`, rearrange the codes so that no two adjacent codes are equal. The input is guaranteed to have at least one valid answer; return any such rearrangement.

Constraints: `1 <= len(barcodes) <= 10^4`, `1 <= barcodes[i] <= 10^4`.

## Examples

### Example 1

```
Input:  barcodes = [1, 1, 1, 2, 2, 2]
Output: [1, 2, 1, 2, 1, 2]
```

**Explanation:** No two adjacent positions hold the same code.

## Hint

This is cooldown with `n = 1` on a numeric alphabet: order codes by descending frequency, then fill the even indices first and wrap to the odd indices, so the most frequent code never lands next to itself.
