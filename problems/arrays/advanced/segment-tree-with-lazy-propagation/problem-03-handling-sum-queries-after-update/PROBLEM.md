# Handling Sum Queries After Update

**Difficulty:** Hard

**Source:** LeetCode 2569 — "Handling Sum Queries After Update".

## Description

You are given two 0-indexed arrays `nums1` and `nums2` of equal length. `nums1`
contains only `0`s and `1`s. You are also given a 2-D array `queries` where each
`queries[i]` is one of three types:

- **`[1, l, r]`** — *flip* every value of `nums1` in the inclusive index range
  `[l, r]`: each `0` becomes `1` and each `1` becomes `0`.
- **`[2, p, 0]`** — for every index `i`, perform `nums2[i] = nums2[i] + nums1[i] * p`.
- **`[3, 0, 0]`** — report the sum of all elements of `nums2`.

Return an array containing the answers to all queries of type `3`, in order.

The trick: a type-2 update adds `p` to `nums2[i]` for exactly the indices where
`nums1[i] == 1`. So the increment to `sum(nums2)` is `p * (number of 1s currently
in nums1)`. If you can maintain the count of 1s in `nums1` under range flips
efficiently, you never have to touch `nums2` element-by-element.

## Constraints

- `1 <= len(nums1) == len(nums2) <= 10^5`
- `1 <= len(queries) <= 10^5`
- `queries[i].length == 3`
- `0 <= l <= r <= len(nums1) - 1`
- `0 <= p <= 10^6`
- `nums1[i]` is `0` or `1`.
- `0 <= nums2[i] <= 10^9`

## Examples

### Example 1

```
Input:
  nums1 = [1, 0, 1]
  nums2 = [0, 0, 0]
  queries = [[1,1,1], [2,1,0], [3,0,0]]
Output:
  [3]
Explanation:
  [1,1,1]: flip nums1[1..1]  -> nums1 = [1, 1, 1]
  [2,1,0]: nums2[i] += nums1[i]*1 -> nums2 = [1, 1, 1]
  [3,0,0]: sum(nums2) = 1 + 1 + 1 = 3
```

### Example 2

```
Input:
  nums1 = [1]
  nums2 = [5]
  queries = [[2,0,0], [3,0,0]]
Output:
  [5]
Explanation:
  [2,0,0]: p = 0, so nums2[i] += nums1[i]*0 -> nums2 = [5] (unchanged)
  [3,0,0]: sum(nums2) = 5
```

## Hint

Keep a running total of `sum(nums2)`. Build a **Segment Tree with Lazy
Propagation** over `nums1` that stores the *count of 1s* in each range and
supports a range *flip*. The flip is a self-inverse (XOR) lazy tag: applying it to
a node covering `k` elements replaces its count of ones with `k - count`, and two
flips cancel. On a type-2 query, add `p * (total ones in nums1)` to the running
total.
