# Search Insert Position

**Difficulty:** Easy

**Source:** LeetCode 35 — Search Insert Position

## Description

Given a sorted array of **distinct** integers `nums` and a target value `target`, return the
index if the target is found. If not, return the index where it **would be** if it were inserted
in order (so that the array stays sorted).

You must write an algorithm with `O(log n)` runtime complexity.

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains **distinct** values sorted in **ascending** order.
- `-10^4 <= target <= 10^4`

## Examples

### Example 1
```
Input:  nums = [1, 3, 5, 6], target = 5
Output: 2
Explanation: 5 is present at index 2, so we return 2.
```

### Example 2
```
Input:  nums = [1, 3, 5, 6], target = 2
Output: 1
Explanation: 2 is not present. It belongs between 1 (index 0) and 3 (index 1),
             so it would be inserted at index 1.
```

### Example 3
```
Input:  nums = [1, 3, 5, 6], target = 7
Output: 4
Explanation: 7 is larger than every element, so it would be appended at index 4
             (one past the last element).
```

## Hint

The insertion point is exactly the **first index whose value is `>= target`**. Use a
**Lower/Upper Bound (bisect)** search — specifically the lower bound.
