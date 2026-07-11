# 4Sum II

**Difficulty:** Medium

**Source:** LeetCode 454 — 4Sum II

## Description

You are given four integer arrays `nums1`, `nums2`, `nums3`, and `nums4`, all
of the same length `n`.

Return the number of index tuples `(i, j, k, l)` with
`0 <= i, j, k, l < n` such that:

```
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
```

Every valid combination of indices counts, even if the resulting values are
equal — the tuples are distinguished by their indices, not their values.

## Constraints

- `n == nums1.length == nums2.length == nums3.length == nums4.length`
- `1 <= n <= 200`
- `-2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28`

## Examples

### Example 1

```
Input:  nums1 = [1, 2], nums2 = [-2, -1], nums3 = [-1, 2], nums4 = [0, 2]
Output: 2
```

**Explanation:** The two tuples that sum to 0 are:
- `(i, j, k, l) = (0, 0, 0, 1)` → `1 + (-2) + (-1) + 2 = 0`
- `(i, j, k, l) = (1, 1, 0, 0)` → `2 + (-1) + (-1) + 0 = 0`

### Example 2

```
Input:  nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
```

**Explanation:** The only tuple is `(0, 0, 0, 0)` → `0 + 0 + 0 + 0 = 0`.

### Example 3

```
Input:  nums1 = [1, -1], nums2 = [1, -1], nums3 = [1, -1], nums4 = [1, -1]
Output: 6
```

**Explanation:** Out of `2^4 = 16` index tuples, exactly the ones with two
`+1`s and two `-1`s sum to 0. There are `C(4, 2) = 6` such tuples.

## Hint

A naive four-nested loop is `O(n^4)`. Instead of searching all four arrays at
once, split them into two independent pairs and **meet in the middle**:
precompute all pair-sums of the first two arrays, then scan the pair-sums of
the last two and look up the value that would complete a zero sum.
