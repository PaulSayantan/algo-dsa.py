# Number of Sub-arrays of Size K and Average >= Threshold

**Difficulty:** Medium

**Source:** LeetCode 1343 — Number of Sub-arrays of Size K and Average Greater or Equal to Threshold

## Description

Given an integer array `arr`, an integer `k`, and an integer `threshold`, return the number of sub-arrays of size `k` whose average is greater than or equal to `threshold`.

The average of a sub-array is its sum divided by `k`. Comparing `sum >= k * threshold` avoids floating point entirely.

Constraints: `1 <= arr.length <= 10^5`, `1 <= arr[i] <= 10^4`, `1 <= k <= arr.length`, `0 <= threshold <= 10^4`.

## Examples

### Example 1

```
Input:  arr=[2,2,2,2,5,5,5,8], k=3, threshold=4
Output: 3
```

**Explanation:** The windows with sum >= 12 are `[2,5,5]`, `[5,5,5]`, and `[5,5,8]`.

## Hint

Slide a fixed size-`k` window keeping a running sum: add the incoming element and subtract the one leaving, exactly like a moving average — count windows whose sum reaches `k * threshold`.
