# Maximum Length of Repeated Subarray

**Difficulty:** Medium

**Source:** LeetCode 718 — "Maximum Length of Repeated Subarray". Commonly taught
with DP, but has a clean **binary-search + hashing** solution that generalizes to
the longest-common-substring problem.

## Description

Given two integer arrays `nums1` and `nums2`, return the **maximum length** of a
subarray that appears in **both** arrays.

A subarray is a contiguous block of elements. You are looking for the longest
contiguous run of values that occurs (at some position) in `nums1` and also
occurs (at some, possibly different, position) in `nums2`.

The hashing insight: "does a common subarray of length `L` exist?" is a
**monotone** predicate — if a common length-`L` block exists, so does one of
length `L-1` (a prefix of it). So you can **binary search** on `L`. For a fixed
`L`, hash every length-`L` window of `nums1` into a set, then hash every
length-`L` window of `nums2` and check for a set hit — each check is `O(n + m)`
using rolling hashes. Total `O((n + m) · log(min(n, m)))`.

## Constraints

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 100`

## Examples

### Example 1

```
Input:  nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1],
             which appears in nums1 (indices 2..4) and nums2 (indices 0..2).
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
Explanation: There is no common element, so no common subarray; the answer is 0.
```

## Hint

The predicate "there is a common subarray of length `L`" is monotone in `L`, so
**binary search** on `L`. For each candidate `L`, use a **polynomial rolling
hash** to fingerprint all length-`L` windows of both arrays and look for a shared
fingerprint in `O(n + m)`. This is **Rolling Hash / Polynomial Hashing**.
