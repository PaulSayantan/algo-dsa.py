# Find K Pairs with Smallest Sums

**Difficulty:** Hard

**Source:** LeetCode 373 — Find K Pairs with Smallest Sums

## Description

You are given two integer arrays `nums1` and `nums2` sorted in **non-decreasing order**,
and an integer `k`.

Define a pair `(u, v)` which consists of one element from the first array and one element
from the second array.

Return the `k` pairs `(u1, v1), (u2, v2), ..., (uk, vk)` with the **smallest sums**
`u + v`.

## Constraints

- `1 <= nums1.length, nums2.length <= 10^5`
- `-10^9 <= nums1[i], nums2[i] <= 10^9`
- `nums1` and `nums2` are both sorted in non-decreasing order.
- `1 <= k <= 10^4`
- `k <= nums1.length * nums2.length`

## Examples

### Example 1

```
Input:  nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 3
Output: [[1, 2], [1, 4], [1, 6]]
```

**Explanation:** The 3 smallest sums come from pairing 1 with each of 2, 4, 6, giving sums
3, 5, and 7 — smaller than any pair starting with 7 (whose smallest sum is 7 + 2 = 9).

### Example 2

```
Input:  nums1 = [1, 1, 2], nums2 = [1, 2, 3], k = 2
Output: [[1, 1], [1, 1]]
```

**Explanation:** The two smallest sums are both 2, from `1 + 1` using either copy of 1 in
`nums1` paired with the leading 1 in `nums2`.

### Example 3

```
Input:  nums1 = [1, 2], nums2 = [3], k = 3
Output: [[1, 3], [2, 3]]
```

**Explanation:** Only `2 x 1 = 2` pairs exist. Their sums are `1 + 3 = 4` and `2 + 3 = 5`,
so all available pairs are returned even though `k = 3`.

## Hint

Do **not** materialize all `m x n` pairs. Because both arrays are sorted, the smallest
unseen sum always sits on a "frontier" of candidates. Use **Top-K via Heap**: seed the heap
with the first column and, each time you pop a pair, push its right neighbor.
