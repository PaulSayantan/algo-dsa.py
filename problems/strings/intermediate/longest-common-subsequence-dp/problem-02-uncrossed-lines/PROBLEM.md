# Uncrossed Lines

**Difficulty:** Medium

**Source:** LeetCode 1035 — Uncrossed Lines

## Description

You are given two integer arrays `nums1` and `nums2`. We write the integers of
`nums1` and `nums2` (in the order they are given) on two separate horizontal
lines.

We may draw connecting lines: a straight line connecting two numbers
`nums1[i]` and `nums2[j]` such that:

- `nums1[i] == nums2[j]`, and
- the line we draw does not intersect any other connecting line.

Note that a connecting line cannot intersect even at the endpoints (i.e., each
number can belong to at most one connecting line).

Return the **maximum number of connecting lines** we can draw in this way.

## Constraints

- `1 <= nums1.length, nums2.length <= 500`
- `1 <= nums1[i], nums2[j] <= 2000`

## Examples

### Example 1

```
Input:  nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
```

Explanation: We can draw 2 uncrossed lines connecting `nums1[0]=1` to
`nums2[0]=1`, and `nums1[1]=4` to `nums2[2]=4`. Connecting `2` to `2` as well
would cross the line for `4`, so we cannot draw all three.

### Example 2

```
Input:  nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3
```

Explanation: The subsequence `[5,1,2]` appears in both arrays in order, giving
3 non-crossing lines.

### Example 3

```
Input:  nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
```

Explanation: The common ordered pairs are `1` and then `5` (or `1` then `1`),
giving 2 uncrossed lines.

## Hint

"Non-crossing" forces the connected values to keep the same relative order in
both arrays — that is precisely a common subsequence. Solve it with **Longest
Common Subsequence (DP)** on the two integer arrays.
