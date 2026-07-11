# Contains Duplicate

**Difficulty:** Easy

**Source:** LeetCode 217 (Contains Duplicate)

## Description

Given an integer array `nums`, return `true` if any value appears **at least
twice** in the array, and return `false` if every element is distinct.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples

### Example 1

```
Input:  nums = [1, 2, 3, 1]
Output: true
Explanation: The value 1 appears at indices 0 and 3, so a duplicate exists.
```

### Example 2

```
Input:  nums = [1, 2, 3, 4]
Output: false
Explanation: All four values are distinct, so no duplicate exists.
```

### Example 3

```
Input:  nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
Explanation: Several values repeat (for example 1 appears three times), so the
answer is true.
```

## Hint

Use **Hashing**: build a hash set of values you have already encountered. Before
adding each new value, check whether it is already in the set — the very first
time a value is already present, you have found a duplicate.
