# Previous Smaller Element

**Difficulty:** Medium

**Source:** Classic — nearest smaller to the left

## Description

Given an array `nums`, for each index return the nearest element to its **left** that is strictly smaller than `nums[i]`, or `-1` if none exists. Return the array of such values.

## Hint

Increasing stack of values; pop while top >= current, then the top is the previous smaller.
