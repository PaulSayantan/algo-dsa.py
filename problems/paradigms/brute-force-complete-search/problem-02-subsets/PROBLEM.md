# Subsets

**Difficulty:** Medium

**Source:** LeetCode 78 (Subsets)

## Description

Given an integer array `nums` of **unique** elements, return *all possible
subsets* (the power set).

The solution set must not contain duplicate subsets. You may return the answer
in any order.

Because every element is independently either **in** or **out** of a subset, a
set of `n` elements has exactly `2^n` subsets. A brute-force / complete-search
solution simply enumerates all `2^n` in/out combinations and materializes the
corresponding subset for each.

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are **unique**.

## Examples

### Example 1

```
Input:  nums = [1, 2, 3]
Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
Explanation: There are 2^3 = 8 subsets. Each of the three elements is
independently included or excluded, giving every combination from the empty set
up to the full set. (Any ordering of these 8 subsets is accepted.)
```

### Example 2

```
Input:  nums = [0]
Output: [[], [0]]
Explanation: With a single element there are 2^1 = 2 subsets: the empty set and
the set containing 0 itself.
```

## Constraints on the answer

- The output has exactly `2^n` subsets.
- No two subsets in the output are equal.

## Hint

Use **Brute Force / Complete Search**: iterate a bitmask from `0` to `2^n - 1`;
bit `i` of the mask decides whether `nums[i]` belongs to the current subset.
