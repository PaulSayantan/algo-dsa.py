# Count Occurrences of a Value

**Difficulty:** Easy

**Source:** Classic (introductory array problem)

## Description

Given an array of integers `nums` and an integer `target`, return the number of times
`target` appears in `nums`. If it never appears, return `0`.

The array is unsorted.

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

## Examples

### Example 1

```
Input:  nums = [1, 2, 3, 2, 4, 2, 5], target = 2
Output: 3
```

**Explanation:** The value 2 appears at indices 1, 3, and 5 — three times.

### Example 2

```
Input:  nums = [7, 8, 9], target = 6
Output: 0
```

**Explanation:** 6 does not occur in the array, so the count is 0.

### Example 3

```
Input:  nums = [4, 4, 4, 4], target = 4
Output: 4
```

**Explanation:** Every element equals the target, so the count equals the length, 4.

## Hint

Use **Linear Search**, but do not stop at the first match — scan the entire array and
increment a counter each time you find the target.
