# Count of Smaller Numbers After Self

**Difficulty:** Hard

**Source:** LeetCode 315 — Count of Smaller Numbers After Self

## Description

You are given an integer array `nums`. Return an integer array `counts` where
`counts[i]` is the number of elements strictly smaller than `nums[i]` that appear
to the **right** of index `i` (i.e. among `nums[i+1 .. n-1]`).

The natural order-statistics approach is to scan the array from **right to left**,
maintaining a dynamic multiset of the elements already seen (those to the right of
the current index). For each `nums[i]`, before inserting it we ask the multiset
"how many stored keys are strictly less than `nums[i]`?" — that is exactly a
**rank** query on an order-statistics tree.

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
- To the right of `5` there are `2` and `1`, both smaller -> `2`.
- To the right of `2` there is `1`, which is smaller -> `1`.
- To the right of `6` there is `1`, which is smaller -> `1`.
- To the right of `1` there is nothing -> `0`.

### Example 2

```
Input:  nums = [-1, -1]
Output: [0, 0]
```

**Explanation:** For the first `-1`, the only element to its right is another `-1`,
which is **not strictly smaller**, so the count is `0`. The second `-1` has nothing
to its right, so its count is `0` as well.

### Example 3

```
Input:  nums = [-1]
Output: [0]
```

**Explanation:** A single element has no elements to its right, so its count is `0`.

## Hint

Scan right to left, inserting each value into an **Order-Statistics Tree**. Before
inserting `nums[i]`, query how many already-inserted keys are strictly less than
`nums[i]` (a rank query), which counts the smaller elements to its right in
`O(log n)`.
