# 3Sum

**Difficulty:** Medium

**Source:** LeetCode 15 — 3Sum

## Description

Given an integer array `nums`, return all the triplets
`[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, `j != k`, and
`nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must **not contain duplicate triplets**. The order
of the triplets and the order of numbers within a triplet do not matter for
correctness, though examples below are shown in sorted form.

## Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Examples

### Example 1
- **Input:** `nums = [-1, 0, 1, 2, -1, -4]`
- **Output:** `[[-1, -1, 2], [-1, 0, 1]]`
- **Explanation:** `(-1) + (-1) + 2 = 0` and `(-1) + 0 + 1 = 0`. The triplet
  `(0, 1, -1)` is the same set as `(-1, 0, 1)` and is therefore not repeated.

### Example 2
- **Input:** `nums = [0, 1, 1]`
- **Output:** `[]`
- **Explanation:** The only possible triplet is `0 + 1 + 1 = 2 != 0`, so there
  is no valid triplet.

### Example 3
- **Input:** `nums = [0, 0, 0]`
- **Output:** `[[0, 0, 0]]`
- **Explanation:** `0 + 0 + 0 = 0`. There is exactly one unique triplet even
  though several index combinations produce it.

## Hint

Use **Two Pointers (opposite ends)**: first sort the array. Then fix one element
and use a left/right pointer pair on the remaining suffix to find pairs that
complete the sum to zero, skipping duplicates as you go.
