# Sum of Subarray Minimums

**Difficulty:** Medium

**Source:** LeetCode 907 — Sum of Subarray Minimums

## Description

Given an array of integers `arr`, find the sum of `min(b)` over every (contiguous) subarray `b` of `arr`. Because the answer can be large, return it modulo `10^9 + 7`.

Constraints: `1 <= len(arr) <= 3 * 10^4`, `1 <= arr[i] <= 3 * 10^4`.

## Examples

### Example 1

```
Input:  arr = [3,1,2,4]
Output: 17
```

**Explanation:** The subarray minimums are `3,1,2,4,1,1,2,1,1,1`, and their sum is `17`.

## Hint

For each element, use a monotonic stack to find how far it stays the minimum on each side (the "left span" and "right span"), then it contributes `arr[i] * left * right` — the same span-counting trick that resolves bars in trapping rain water.
