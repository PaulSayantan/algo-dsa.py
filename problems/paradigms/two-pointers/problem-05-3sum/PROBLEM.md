# 3Sum

**Difficulty:** Medium

**Source:** LeetCode 15 (3Sum)

## Description

Given an integer array `nums`, return all the triplets
`[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and
`nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set **must not contain duplicate triplets**. The order
of the triplets and the order of numbers within a triplet do not matter for
correctness, though the examples below present each triplet in non-decreasing
order.

## Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Examples

### Example 1

```
Input:  nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
```

Explanation: The distinct triplets summing to zero are `(-1) + (-1) + 2 = 0` and
`(-1) + 0 + 1 = 0`. Although the value `-1` appears twice in the input, the
triplet `[-1, 0, 1]` is only listed once.

### Example 2

```
Input:  nums = [0, 1, 1]
Output: []
```

Explanation: The only possible triplet is `0 + 1 + 1 = 2 != 0`, so there is no
valid triplet.

### Example 3

```
Input:  nums = [0, 0, 0]
Output: [[0, 0, 0]]
```

Explanation: `0 + 0 + 0 = 0`, and it is the only triplet.

## Hint

Sort the array first, then fix one element and reduce the rest to a two-sum
problem solved with the **Two Pointers** technique. Skipping over equal
neighbors is how you avoid emitting duplicate triplets.
