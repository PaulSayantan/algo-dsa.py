# Search Insert Position

**Difficulty:** Easy

**Source:** LeetCode 35 — Search Insert Position

## Description

Given a sorted array of **distinct** integers `nums` and a target value
`target`, return the index if the target is found. If not, return the index
where it **would be inserted** in order to keep the array sorted.

You must write an algorithm with `O(log n)` runtime complexity.

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains **distinct** values sorted in ascending order.
- `-10^4 <= target <= 10^4`

## Examples

### Example 1

```
Input:  nums = [1, 3, 5, 6], target = 5
Output: 2
Explanation: 5 is found at index 2.
```

### Example 2

```
Input:  nums = [1, 3, 5, 6], target = 2
Output: 1
Explanation: 2 is not present; it belongs between 1 (index 0) and 3 (index 1),
so it would be inserted at index 1.
```

### Example 3

```
Input:  nums = [1, 3, 5, 6], target = 7
Output: 4
Explanation: 7 is larger than every element, so it would be appended at index 4
(the length of the array).
```

### Example 4

```
Input:  nums = [1, 3, 5, 6], target = 0
Output: 0
Explanation: 0 is smaller than every element, so it would be inserted at the
front, index 0.
```

## Hint

Use **Binary Search** for the *lower bound*: find the first index whose value is
greater than or equal to the target. That index is both the found position and
the correct insertion position.
