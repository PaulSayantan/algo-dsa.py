# Count Subarrays Summing to Target (with Negatives)

**Difficulty:** Medium

**Source:** Classic — prefix-sum counting with negatives

## Description

Given an integer array `nums` (which may contain negatives and zeros) and an integer `target`, return the number of contiguous subarrays whose sum equals `target`. A sliding window does not work because sums are not monotonic; use a prefix-sum frequency map.

## Hint

Identical to Subarray Sum Equals K — the frequency map is negative-safe.
