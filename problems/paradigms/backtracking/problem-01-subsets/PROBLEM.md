# Subsets

**Difficulty:** Easy / Medium

**Source:** LeetCode 78 — "Subsets"

## Description

Given an integer array `nums` of **unique** elements, return *all possible
subsets* (the **power set**).

The solution set **must not contain duplicate subsets**. You may return the
answer in **any order**.

Because every element can either be included or excluded independently, an array
of `n` elements has exactly `2^n` subsets, including the empty set and the full
set itself.

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are **unique**.

## Examples

### Example 1

```
Input:  nums = [1, 2, 3]
Output: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
Explanation: There are 2^3 = 8 subsets. The list above contains the empty
subset, all three singletons, all three pairs, and the full set — 8 distinct
subsets in total. Any ordering of these 8 subsets is accepted.
```

### Example 2

```
Input:  nums = [0]
Output: [[], [0]]
Explanation: A single-element array has 2^1 = 2 subsets: the empty set and
the set containing 0.
```

## Hint

Use **Backtracking**: walk left-to-right through the array, and at each index
decide whether to *include* the current element or *skip* it, recording the
running subset whenever you have made a decision for every element.
