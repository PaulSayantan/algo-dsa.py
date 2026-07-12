# Longest Subarray With Sum K (Negatives)

**Difficulty:** Medium

**Source:** Classic — longest subarray with given sum (with negatives)

## Description

Given an array `nums` containing positive and negative integers and an integer `k`, return the length of the longest contiguous subarray whose sum equals `k`.

## Hint

Earliest-index prefix map; when cur-k was seen, best = i - first[cur-k].
