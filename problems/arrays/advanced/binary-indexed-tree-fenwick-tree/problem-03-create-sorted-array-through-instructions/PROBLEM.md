# Create Sorted Array Through Instructions

**Difficulty:** Hard

**Source:** LeetCode 1649 — Create Sorted Array through Instructions

## Description

Given an integer array `instructions`, you are asked to create a sorted array from the
elements in `instructions`. You start with an empty container `nums`. For each element from
`instructions` **in order**, insert it into `nums`. The **cost** of each insertion is the
**minimum** of these two quantities:

- The number of elements currently in `nums` that are **strictly less than** the value
  being inserted.
- The number of elements currently in `nums` that are **strictly greater than** the value
  being inserted.

For example, if inserting element `3` into `nums = [1, 2, 3, 5]`, the cost of insertion is
`min(2, 1)` (two elements less than `3`: `1` and `2`; one element greater than `3`: `5`),
and `nums` becomes `[1, 2, 3, 3, 5]`.

Return the **total cost** to insert all elements from `instructions`. Since the answer may
be large, return it **modulo** `10^9 + 7`.

## Constraints

- `1 <= instructions.length <= 10^5`
- `1 <= instructions[i] <= 10^5`

## Examples

### Example 1

```
Input:  instructions = [1, 5, 6, 2]
Output: 1
```

**Explanation:**
- Insert `1` with cost `min(0, 0) = 0`, now `nums = [1]`.
- Insert `5` with cost `min(1, 0) = 0`, now `nums = [1, 5]`.
- Insert `6` with cost `min(2, 0) = 0`, now `nums = [1, 5, 6]`.
- Insert `2` with cost `min(1, 2) = 1`, now `nums = [1, 2, 5, 6]`.
- Total cost is `0 + 0 + 0 + 1 = 1`.

### Example 2

```
Input:  instructions = [1, 2, 3, 6, 5, 4]
Output: 3
```

**Explanation:**
- Insert `1`, `2`, `3`, `6` each with cost `0`, now `nums = [1, 2, 3, 6]`.
- Insert `5` with cost `min(4, 1) = 1`, now `nums = [1, 2, 3, 5, 6]`.
- Insert `4` with cost `min(3, 2) = 2`, now `nums = [1, 2, 3, 4, 5, 6]`.
- Total cost is `0 + 0 + 0 + 0 + 1 + 2 = 3`.

### Example 3

```
Input:  instructions = [1, 3, 3, 3, 2, 4, 2, 1, 2]
Output: 4
```

**Explanation:** The per-insertion costs are `0, 0, 0, 0, 1, 0, 1, 0, 2`, summing to `4`.
For instance, the final `2` is inserted into `[1, 1, 2, 2, 3, 3, 3, 4]`: two elements are
strictly less (`1, 1`) and four are strictly greater (`3, 3, 3, 4`), giving `min(2, 4) = 2`.
Equal elements count toward neither "strictly less" nor "strictly greater," which is why the
repeated `3`s each cost `0`.

## Hint

Maintain a frequency count over values. For each new value `v`, the count of elements
strictly less than `v` is a **prefix count**, and elements strictly greater is
`total_inserted - count(<= v)`. A **Binary Indexed Tree (Fenwick Tree)** over values gives
both counts and the point insertion in O(log n).
