# Number of Pairs Satisfying Inequality

**Difficulty:** Hard

**Source:** LeetCode 2426 — "Number of Pairs Satisfying Inequality"

## Description

You are given two 0-indexed integer arrays `nums1` and `nums2`, each of length
`n`, and an integer `diff`. Count the number of pairs `(i, j)` such that:

- `0 <= i < j <= n - 1`, and
- `nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff`.

Return that count.

**Key rearrangement.** Move the `nums2` terms to the left:

```
nums1[i] - nums2[i]  <=  nums1[j] - nums2[j] + diff
```

Define a derived array `d[k] = nums1[k] - nums2[k]`. The condition becomes

```
d[i] <= d[j] + diff      (with i < j)
```

which is a monotone comparison between two positions of a single array — exactly
the shape that merge-sort cross-pair counting handles.

## Constraints

- `n == nums1.length == nums2.length`
- `2 <= n <= 10^5`
- `-10^4 <= nums1[i], nums2[i] <= 10^4`
- `-10^4 <= diff <= 10^4`

## Examples

### Example 1

```
Input:  nums1 = [3, 2, 5], nums2 = [2, 2, 1], diff = 1
Output: 3
Explanation: d = [3-2, 2-2, 5-1] = [1, 0, 4]. We need d[i] <= d[j] + 1 with i < j:
  (0,1): 1 <= 0 + 1 = 1   (valid)
  (0,2): 1 <= 4 + 1 = 5   (valid)
  (1,2): 0 <= 4 + 1 = 5   (valid)
All 3 pairs qualify.
```

### Example 2

```
Input:  nums1 = [3, -1], nums2 = [-2, 2], diff = -1
Output: 0
Explanation: d = [3-(-2), -1-2] = [5, -3]. We need d[i] <= d[j] - 1:
  (0,1): 5 <= -3 - 1 = -4   (invalid)
There are no valid pairs.
```

## Hint

Build the derived array `d[k] = nums1[k] - nums2[k]`, then use **Count Inversions
(merge sort)** to count pairs `i < j` with `d[i] <= d[j] + diff`. During the
merge, both halves are sorted; for each right-half element `j`, the qualifying
left-half elements form a prefix, so a monotone two-pointer counts them in linear
time per level.
