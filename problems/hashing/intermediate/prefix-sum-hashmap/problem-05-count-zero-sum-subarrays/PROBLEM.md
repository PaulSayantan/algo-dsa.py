# Count Zero-Sum Subarrays

**Difficulty:** Medium

**Source:** Classic — zero-sum subarray counting

## Description

Given an integer array `nums`, return the number of contiguous subarrays whose elements sum to zero. Two prefix-sum boundaries with equal prefix sums delimit a zero-sum subarray.

## Hint

Count pairs of equal prefix sums: count += freq[cur] before freq[cur] += 1.
