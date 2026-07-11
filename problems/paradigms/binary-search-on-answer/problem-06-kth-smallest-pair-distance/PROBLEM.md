# Find K-th Smallest Pair Distance

**Difficulty:** Hard

**Source:** LeetCode 719 (Find K-th Smallest Pair Distance)

## Description

The **distance** of a pair of integers `a` and `b` is defined as the absolute
difference `|a - b|`.

Given an integer array `nums` and an integer `k`, return the **`k`-th smallest
distance among all the pairs** `nums[i]` and `nums[j]` where `0 <= i < j <
nums.length`.

There are exactly `n * (n - 1) / 2` pairs; the distances are considered in sorted
order (with duplicates counted separately), and you must return the `k`-th one
(1-indexed).

## Constraints

- `n == nums.length`
- `2 <= n <= 10^4`
- `0 <= nums[i] <= 10^6`
- `1 <= k <= n * (n - 1) / 2`

## Examples

### Example 1

```
Input:  nums = [1, 3, 1], k = 1
Output: 0
```

Explanation: The pairs and distances are `(1,3) → 2`, `(1,1) → 0`, `(3,1) → 2`.
Sorted distances: `[0, 2, 2]`. The `1`-st smallest is `0`.

### Example 2

```
Input:  nums = [1, 1, 1], k = 2
Output: 0
```

Explanation: All three pairs have distance `0`. Sorted distances: `[0, 0, 0]`.
The `2`-nd smallest is `0`.

### Example 3

```
Input:  nums = [1, 6, 1], k = 3
Output: 5
```

Explanation: The pairs and distances are `(1,6) → 5`, `(1,1) → 0`, `(6,1) → 5`.
Sorted distances: `[0, 5, 5]`. The `3`-rd smallest is `5`.

## Hint

Enumerating all `O(n^2)` distances is too slow. Instead **Binary Search on
Answer** over the *distance value* range `[0, max(nums) - min(nums)]`. For a
candidate distance `d`, count how many pairs have distance `<= d` — that count is
monotonic in `d`. Sort `nums` first so the counting can be done with a **sliding
window / two pointers** in `O(n)`.
