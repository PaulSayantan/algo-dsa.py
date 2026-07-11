# Random Pick Index

**Difficulty:** Medium

**Source:** LeetCode 398 — Random Pick Index

## Description

Given an integer array `nums` that may contain **duplicates**, implement a
`pick(target)` method that returns a **random index** `i` such that `nums[i] == target`.

If `target` appears multiple times in the array, each of its indices must be returned
with **equal probability**. It is guaranteed that `target` exists in `nums` whenever
`pick` is called.

Implement the `Solution` class:

- `Solution(int[] nums)` — initializes the object with the array `nums`.
- `int pick(int target)` — returns a uniformly random index `i` with `nums[i] == target`.

**Follow-up:** Can you do it using only `O(1)` extra space (beyond storing `nums`),
i.e. without building a map from each value to its list of indices?

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `target` is an integer from `nums`.
- At most `10^4` calls will be made to `pick`.

## Examples

### Example 1

```
Input:
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]

Output (one possible run):
[null, 4, 0, 2]
```

**Explanation:** `pick(3)` returns index `2`, `3`, or `4`, each with probability `1/3`
(these are the positions where `nums[i] == 3`). `pick(1)` must return `0`, the only
index where the value is `1`.

### Example 2

```
Input:
["Solution", "pick", "pick"]
[[[5, 5]], [5], [5]]

Output (one possible run):
[null, 0, 1]
```

**Explanation:** Both indices `0` and `1` hold the value `5`, so each `pick(5)` returns
`0` or `1` with probability `1/2`.

## Hint

Scan the array once. Among the positions matching `target`, treat them as a stream and
keep the current position as your answer with probability `1/count`, where `count` is how
many matches you have seen so far. This is **Reservoir Sampling** with `k = 1` applied to
the matching indices.
