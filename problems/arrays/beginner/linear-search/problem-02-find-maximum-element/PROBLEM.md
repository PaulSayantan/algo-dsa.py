# Find the Maximum Element

**Difficulty:** Easy

**Source:** Classic (introductory array problem)

## Description

Given a non-empty array of integers `nums`, return the **largest** value in the
array. The array is unsorted, and values may be negative.

You must find the answer in a single pass without sorting or using a built-in max
helper (the point is to practice scanning).

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples

### Example 1

```
Input:  nums = [3, 41, 52, 26, 38, 57, 9, 49]
Output: 57
```

**Explanation:** Scanning left to right, the running maximum climbs 3 → 41 → 52 → 57
(at index 5) and never gets beaten by 9 or 49, so the answer is 57.

### Example 2

```
Input:  nums = [-7, -3, -19, -2, -11]
Output: -2
```

**Explanation:** All values are negative. The least-negative (largest) value is -2.

### Example 3

```
Input:  nums = [42]
Output: 42
```

**Explanation:** A single element is trivially the maximum.

## Hint

Use **Linear Search** with an accumulator: keep a "best so far" variable and update
it every time you encounter a larger element during your scan.
