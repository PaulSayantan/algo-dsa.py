# Range Addition

**Difficulty:** Medium

**Source:** LeetCode 370 — Range Addition

## Description

You are given an integer `length` and a 2D array `updates` where
`updates[i] = [startIdx_i, endIdx_i, inc_i]`.

Start with an array `arr` of size `length` filled with all zeros. For each update
you must add `inc_i` to **every** element in the inclusive index range
`[startIdx_i, endIdx_i]`.

Return `arr` after applying all `updates`.

## Constraints

- `1 <= length <= 10^5`
- `0 <= updates.length <= 10^4`
- `0 <= startIdx_i <= endIdx_i < length`
- `-1000 <= inc_i <= 1000`

## Examples

### Example 1

```
Input:  length = 5, updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
Output: [-2, 0, 3, 5, 3]
```

**Explanation:** Start with `[0, 0, 0, 0, 0]`.
- After `[1, 3, 2]`: add 2 to indices 1..3 -> `[0, 2, 2, 2, 0]`.
- After `[2, 4, 3]`: add 3 to indices 2..4 -> `[0, 2, 5, 5, 3]`.
- After `[0, 2, -2]`: add -2 to indices 0..2 -> `[-2, 0, 3, 5, 3]`.

### Example 2

```
Input:  length = 4, updates = [[0, 3, 1], [1, 2, 5]]
Output: [1, 6, 6, 1]
```

**Explanation:** Start with `[0, 0, 0, 0]`.
- After `[0, 3, 1]`: add 1 to every index -> `[1, 1, 1, 1]`.
- After `[1, 2, 5]`: add 5 to indices 1..2 -> `[1, 6, 6, 1]`.

## Hint

Applying each update directly is `O(length)` per update. Record only the
*boundaries* of each range with a **Difference Array** (`+inc` at `start`,
`-inc` just past `end`), then take a single prefix sum to build the answer.
