# Find the Duplicate Number

**Difficulty:** Medium

**Source:** LeetCode 287 (Find the Duplicate Number)

## Description

Given an array of integers `nums` containing `n + 1` integers where each integer
is in the range `[1, n]` inclusive, there is **only one repeated number** in
`nums`. Return **this repeated number**.

You must solve the problem **without modifying** the array `nums` and use only
**constant** extra space.

## Constraints

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only **once** except for **precisely one
  integer** which appears **two or more** times.

## Examples

### Example 1

```
Input:  nums = [1, 3, 4, 2, 2]
Output: 2
```

**Explanation:** The number `2` is the only value that appears more than once.

### Example 2

```
Input:  nums = [3, 1, 3, 4, 2]
Output: 3
```

**Explanation:** The number `3` is the only value that appears more than once.

### Example 3

```
Input:  nums = [2, 2, 2, 2, 2]
Output: 2
```

**Explanation:** `2` appears five times; it is the repeated number.

## Hint

Use the **fast-slow** member of the Two Pointers family (Floyd's cycle
detection). Treat each index `i` as a node with an edge to `nums[i]`; the
duplicate value forces a cycle, and the cycle's entrance is the answer — found
with O(1) space and without modifying the array.
