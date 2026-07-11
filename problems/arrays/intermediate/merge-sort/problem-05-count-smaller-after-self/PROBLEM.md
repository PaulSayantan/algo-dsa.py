# Count of Smaller Numbers After Self

**Difficulty:** Hard

**Source:** LeetCode 315 — Count of Smaller Numbers After Self

## Description

Given an integer array `nums`, return an integer array `counts` where
`counts[i]` is the number of elements to the **right** of `nums[i]` that are
**smaller** than `nums[i]`.

Formally, `counts[i] = |{ j : j > i and nums[j] < nums[i] }|`.

This is a per-element generalization of counting inversions: instead of one total,
you must attribute the "smaller-to-the-right" count to each originating index.

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
- To the right of `5` there are `2` smaller elements (`2` and `1`).
- To the right of `2` there is `1` smaller element (`1`).
- To the right of `6` there is `1` smaller element (`1`).
- To the right of `1` there are `0` smaller elements.

### Example 2

```
Input:  nums = [-1, -1]
Output: [0, 0]
```

**Explanation:** For the first `-1`, the element to its right (`-1`) is equal, not
smaller, so the count is `0`. The second `-1` has nothing to its right.

### Example 3

```
Input:  nums = [3, 2, 2, 1]
Output: [3, 1, 1, 0]
```

**Explanation:** To the right of the first `2` there is only `1` smaller element
(the trailing `1`); the equal `2` does not count.

## Hint

Use **Merge Sort** on (value, original-index) pairs. When merging, an element from
the right half that is placed before some left-half elements is smaller than them;
credit those left-half elements' original indices with the number of right-half
elements already emitted.
