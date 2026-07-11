# Count of Smaller Numbers After Self

**Difficulty:** Medium

Source: **LeetCode 315** — "Count of Smaller Numbers After Self".

## Description

You are given an integer array `nums`. Return a new array `counts` where `counts[i]` is
the number of elements to the **right** of `nums[i]` that are **strictly smaller** than
`nums[i]`.

Formally, `counts[i] = |{ j : j > i and nums[j] < nums[i] }|`.

This is naturally phrased as a family of range queries over a **static** array: for each
index `i`, count how many elements in the suffix `nums[i+1 .. n-1]` are `< nums[i]`. A
Merge Sort Tree answers each such range-count query in `O(log^2 n)`, giving an overall
`O(n log^2 n)` solution. (The classic `O(n log n)` solutions use a modified merge sort or
a BIT; the Merge Sort Tree is the segment-tree way to see the same problem and
generalizes to arbitrary — not just suffix — ranges.)

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
- To the right of `5` (`[2, 6, 1]`), smaller elements are `2` and `1` -> **2**.
- To the right of `2` (`[6, 1]`), smaller element is `1` -> **1**.
- To the right of `6` (`[1]`), smaller element is `1` -> **1**.
- To the right of `1` (`[]`), there is nothing -> **0**.

### Example 2

```
Input:  nums = [-1, -1]
Output: [0, 0]
```

Explanation:
- To the right of the first `-1` is `[-1]`; `-1` is **not** strictly smaller than `-1`, so **0**.
- To the right of the second `-1` is `[]`, so **0**.

## Hint

Build a **Merge Sort Tree** over `nums`. For each index `i`, answer a range query on the
suffix `[i+1, n-1]` counting elements strictly less than `nums[i]` (use a `lower_bound` /
`bisect_left` inside each covering node's sorted list).
