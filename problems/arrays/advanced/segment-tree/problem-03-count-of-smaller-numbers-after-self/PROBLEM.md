# Count of Smaller Numbers After Self

**Difficulty:** Hard

**Source:** LeetCode 315 — Count of Smaller Numbers After Self

## Description

You are given an integer array `nums`. Return a new array `counts` where
`counts[i]` is the number of elements to the **right** of `nums[i]` that are
**strictly smaller** than `nums[i]`.

Formally, `counts[i] = |{ j : j > i and nums[j] < nums[i] }|`.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]
```

**Explanation:**
- To the right of `5` are `2, 6, 1`; the smaller ones are `2` and `1` → count `2`.
- To the right of `2` are `6, 1`; the smaller one is `1` → count `1`.
- To the right of `6` is `1`; smaller → count `1`.
- To the right of `1` there is nothing → count `0`.

### Example 2

```
Input:  nums = [-1, -1]
Output: [0, 0]
```

**Explanation:**
- To the right of the first `-1` is `-1`, which is **not strictly smaller** → count `0`.
- The second `-1` has nothing to its right → count `0`.

## Constraints recap on values

Because values fit in `[-10^4, 10^4]` (a range of `20001` distinct values), you can
index a structure directly by value after an offset, or compress coordinates.

## Hint

Sweep the array from **right to left**, maintaining a **Segment Tree over the value
domain** that stores how many times each value has been seen so far. For each element,
query the count of already-seen values strictly smaller than it (a prefix count),
then insert the current value.
