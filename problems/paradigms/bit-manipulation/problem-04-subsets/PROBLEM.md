# Subsets (Power Set)

**Difficulty:** Medium

**Source:** LeetCode 78 — Subsets

## Description

Given an integer array `nums` of **unique** elements, return all possible subsets (the
**power set**). The solution set must not contain duplicate subsets, and you may return
the subsets in any order.

A set with `n` elements has exactly `2^n` subsets. Because `n` is small, you can map each
subset to an `n`-bit number: bit `j` of the mask decides whether `nums[j]` is included.
Iterating every mask from `0` to `2^n - 1` therefore enumerates every subset exactly
once.

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are **unique**.

## Examples

### Example 1
```
Input:  nums = [1, 2, 3]
Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
Explanation: All 2^3 = 8 subsets. (Order of subsets and of the outer list may vary.)
```

### Example 2
```
Input:  nums = [0]
Output: [[], [0]]
Explanation: 2^1 = 2 subsets: the empty set and the set {0}.
```

### Example 3
```
Input:  nums = [9, 8]
Output: [[], [9], [8], [9, 8]]
Explanation: 2^2 = 4 subsets formed from the two elements.
```

## Hint

Each subset corresponds to a binary choice per element (in / out). **Bit Manipulation** —
loop `mask` over `0 .. 2^n - 1` and include `nums[j]` when the `j`-th bit of `mask` is
set: `(mask >> j) & 1`.
