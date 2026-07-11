# Count of Smaller Numbers After Self

**Difficulty:** Hard

**Source:** LeetCode 315 (Count of Smaller Numbers After Self)

## Description

You are given an integer array `nums`. Return an integer array `counts` where
`counts[i]` is the **number of elements to the right of `nums[i]` that are strictly
smaller than `nums[i]`**.

Formally, `counts[i] = |{ j : j > i and nums[j] < nums[i] }|`.

This is a **counting-inversions** problem in disguise, and the classic Divide and
Conquer solution embeds the counting inside a **merge sort**: while merging two sorted
halves, each time you take an element from the right half you learn how many
right-side elements are smaller than the remaining left-side elements.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]
```

Explanation:
- To the right of `5` are `{2, 6, 1}`; the smaller ones are `2` and `1` → count `2`.
- To the right of `2` are `{6, 1}`; smaller is `1` → count `1`.
- To the right of `6` are `{1}`; smaller is `1` → count `1`.
- To the right of `1` there is nothing → count `0`.

### Example 2

```
Input:  nums = [-1, -1]
Output: [0, 0]
```

Explanation: To the right of the first `-1` is `{-1}`, which is **not strictly
smaller**, so count `0`. The second `-1` has nothing to its right → count `0`.

### Example 3

```
Input:  nums = [3, 1, 2, 4]
Output: [2, 0, 0, 0]
```

Explanation: Right of `3` are `{1, 2, 4}`; smaller are `1` and `2` → count `2`. `1`,
`2`, and `4` each have no smaller element to their right → count `0`.

## Hint

Use **Divide and Conquer** with a merge sort over `(value, original_index)` pairs.
During the **merge**, when an element from the **right** half is placed before some
elements still remaining in the **left** half, those left elements each gain smaller
elements to their right — credit them. Sort indices, not just values, so counts land
in the right output slot.
