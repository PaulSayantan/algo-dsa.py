# Kth Largest Element in an Array

**Difficulty:** Medium

**Source:** LeetCode 215 — Kth Largest Element in an Array

## Description

Given an integer array `nums` and an integer `k`, return the **k-th largest
element** in the array.

Note that it is the k-th largest element in **sorted order**, not the k-th
distinct element. For example, in `[3,2,3,1,2,4,5,5,6]` the 4th largest is `4`
even though `5` appears twice.

Can you solve it **without fully sorting** the array?

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Explanation:** Sorted ascending: `[1,2,3,4,5,6]`. The 2nd largest is `5`.

### Example 2

```
Input:  nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

**Explanation:** Sorted ascending: `[1,2,2,3,3,4,5,5,6]`. Counting from the
largest: `6` (1st), `5` (2nd), `5` (3rd), `4` (4th). Duplicates each count.

## Hint

Use a **heap**. Either build a max-heap of all `n` elements and pop it `k`
times (partial heap sort, `O(n + k log n)`), or maintain a **min-heap of size
`k`**: push each value and evict the smallest whenever the heap exceeds `k`, so
its root is always the k-th largest so far (`O(n log k)`).
