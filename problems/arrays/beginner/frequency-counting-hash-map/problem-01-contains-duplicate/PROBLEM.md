# Contains Duplicate

**Difficulty:** Easy

**Source:** LeetCode 217 (https://leetcode.com/problems/contains-duplicate/)

## Description

Given an integer array `nums`, return `true` if any value appears **at least
twice** in the array, and return `false` if every element is distinct.

This is a foundational "detect duplicates" problem. The naive idea of comparing
every pair of elements works but is slow. The core observation is that we only
need to know whether a value has been *seen before*, which a hash-based
structure answers in constant time on average.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples

### Example 1

```
Input:  nums = [1, 2, 3, 1]
Output: true
Explanation: The value 1 appears at index 0 and again at index 3, so a
duplicate exists.
```

### Example 2

```
Input:  nums = [1, 2, 3, 4]
Output: false
Explanation: Every element is unique, so there is no duplicate.
```

### Example 3

```
Input:  nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
Explanation: Several values repeat (for example 1, 3, 4, and 2), so the array
contains duplicates.
```

## Hint

Use **Frequency Counting with a Hash Map** (or a hash set): track the values you
have already encountered and stop as soon as one repeats.
