# 4Sum

**Difficulty:** Medium

**Source:** LeetCode 18 (4Sum)

## Description

Given an array `nums` of `n` integers, return an array of all the **unique
quadruplets** `[nums[a], nums[b], nums[c], nums[d]]` such that:

- `0 <= a, b, c, d < n`
- `a`, `b`, `c`, and `d` are **distinct** indices.
- `nums[a] + nums[b] + nums[c] + nums[d] == target`.

You may return the answer in any order. The solution set must **not** contain
duplicate quadruplets (same multiset of values).

## Constraints

- `1 <= nums.length <= 200`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

## Examples

**Example 1**

```
Input:  nums = [1, 0, -1, 0, -2, 2], target = 0
Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
Explanation: These are the three distinct quadruplets that sum to 0. For instance
             -2 + -1 + 1 + 2 = 0. Reorderings and duplicate value-multisets are excluded.
```

**Example 2**

```
Input:  nums = [2, 2, 2, 2, 2], target = 8
Output: [[2, 2, 2, 2]]
Explanation: Any four of the 2's sum to 8, but they form the same multiset [2,2,2,2],
             so it is reported exactly once.
```

**Example 3**

```
Input:  nums = [1, -2, -5, -4, -3, 3, 3, 5], target = -11
Output: [[-5, -4, -3, 1]]
Explanation: -5 + -4 + -3 + 1 = -11 is the only quadruplet reaching the target.
```

## Hint

Generalize the k-Sum reduction: **fix the outer two indices** with nested loops,
then solve the inner 2-Sum-to-target with **Two-Pointer on Sorted Sums (k-Sum)**.
Sort first and skip equal neighbors at every level to avoid duplicate quadruplets.
