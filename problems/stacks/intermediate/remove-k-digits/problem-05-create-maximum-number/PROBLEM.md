# Create Maximum Number

**Difficulty:** Medium

**Source:** LeetCode 321 — Create Maximum Number

## Description

You are given two integer arrays `nums1` and `nums2` of lengths `m` and `n`, whose elements are digits `0`-`9`, and an integer `k` with `k <= m + n`. Create the maximum number of length `k` from digits of the two arrays such that the relative order of the digits from the same array is preserved. Return an array of the `k` digits representing that maximum number.

## Examples

### Example 1

```
Input:  nums1 = [3, 4, 6, 5], nums2 = [9, 1, 2, 5, 8, 3], k = 5
Output: [9, 8, 6, 5, 3]
```

**Explanation:** Take the best length-`i` subsequence from each array (max-subsequence via a monotonic stack), then merge to maximize.

### Example 2

```
Input:  nums1 = [6, 7], nums2 = [6, 0, 4], k = 5
Output: [6, 7, 6, 0, 4]
```

**Explanation:** With `k = m + n`, all digits are used; only the interleave order is chosen.

## Hint

Split `k` between the two arrays; for each split pick the max length-`t` subsequence with a monotonic *decreasing* drop-stack (the remove-k-digits maximize trick), then greedily merge the two picks.
