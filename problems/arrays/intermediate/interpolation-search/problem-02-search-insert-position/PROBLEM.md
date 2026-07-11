# Search Insert Position

**Difficulty:** Easy

Source: LeetCode 35 — "Search Insert Position"

## Description

Given a **sorted array of distinct integers** `nums` and a target value `target`, return the
index where `target` is found. If it is not present, return the index where it **would be
inserted** to keep the array sorted.

The reference problem asks for an O(log n) solution. When the values are numeric and fairly
evenly distributed, **Interpolation Search** locates the neighborhood of the target in
O(log log n) probes; you then resolve the exact insertion slot.

## Constraints

- `1 <= len(nums) <= 10^4`
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
Explanation: 2 is not present. It belongs between 1 (index 0) and 3 (index 1),
so the insertion index is 1.
```

### Example 3
```
Input:  nums = [1, 3, 5, 6], target = 7
Output: 4
Explanation: 7 is larger than every element, so it is inserted at the end, index 4.
```

## Hint

Use **Interpolation Search** to zero in on the target's neighborhood; when the value is absent,
the insertion index is the number of elements strictly less than `target` (the collapsed `lo`).
