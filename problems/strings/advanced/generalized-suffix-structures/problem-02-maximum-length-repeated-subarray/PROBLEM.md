# Maximum Length of Repeated Subarray

**Difficulty:** Medium

**Source:** LeetCode 718 — "Maximum Length of Repeated Subarray".

## Description

Given two integer arrays `nums1` and `nums2`, return the **maximum length of a
subarray that appears in both arrays**.

A *subarray* is a contiguous block of the array (order matters and elements must
be adjacent), so this is the array analogue of the **longest common substring**
of two strings — not the longest common *subsequence*.

If the two arrays share no common element, the answer is `0`.

## Constraints

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 100`
- Values are small integers; treat each distinct value as a symbol of an
  alphabet.

## Examples

### Example 1
```
Input:  nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
             It appears in nums1 at index 2..4 and in nums2 at index 0..2.
```

### Example 2
```
Input:  nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The entire array [0,0,0,0,0] is common to both, length 5.
```

### Example 3
```
Input:  nums1 = [1,2,3], nums2 = [4,5,6]
Output: 0
Explanation: The arrays share no common value, so no common subarray exists.
```

## Hint

Treat each array as a string over the integer alphabet and build a **Generalized
Suffix Structure** over the two of them. Annotate each automaton state with the
set of source arrays whose occurrences reach it (propagate up the suffix-link
tree). The answer is the largest `len[v]` among states owned by **both** arrays.
(A textbook `O(m*n)` DP also works and is a good sanity check.)
