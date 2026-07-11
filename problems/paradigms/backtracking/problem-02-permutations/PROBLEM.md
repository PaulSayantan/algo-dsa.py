# Permutations

**Difficulty:** Medium

**Source:** LeetCode 46 — "Permutations"

## Description

Given an array `nums` of **distinct** integers, return *all the possible
permutations*. You can return the answer in **any order**.

A permutation is an arrangement of all the elements of `nums` in a specific
order. An array of `n` distinct elements has exactly `n!` permutations.

## Constraints

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

## Examples

### Example 1

```
Input:  nums = [1, 2, 3]
Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
Explanation: 3! = 6 arrangements. Each uses all three numbers exactly once;
they differ only in order. Any ordering of these 6 lists is accepted.
```

### Example 2

```
Input:  nums = [0, 1]
Output: [[0,1], [1,0]]
Explanation: 2! = 2 arrangements of two distinct numbers.
```

## Hint

Use **Backtracking**: build the permutation position by position. At each step
choose an element that has **not been used yet**, mark it used, recurse, then
un-mark it so the next branch can reuse it.
