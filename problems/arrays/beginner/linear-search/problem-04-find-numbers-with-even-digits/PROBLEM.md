# Find Numbers with Even Number of Digits

**Difficulty:** Easy

**Source:** LeetCode 1295 — "Find Numbers with Even Number of Digits"

## Description

Given an array `nums` of integers, return **how many of them contain an even number of
digits**.

For example, 12 has 2 digits (even), 345 has 3 digits (odd), and 2 has 1 digit (odd).

## Constraints

- `1 <= nums.length <= 500`
- `1 <= nums[i] <= 10^5`

## Examples

### Example 1

```
Input:  nums = [12, 345, 2, 6, 7896]
Output: 2
```

**Explanation:**
- 12 has 2 digits (even).
- 345 has 3 digits (odd).
- 2 has 1 digit (odd).
- 6 has 1 digit (odd).
- 7896 has 4 digits (even).
Two numbers (12 and 7896) have an even number of digits.

### Example 2

```
Input:  nums = [555, 901, 482, 1771]
Output: 1
```

**Explanation:**
- 555 has 3 digits (odd).
- 901 has 3 digits (odd).
- 482 has 3 digits (odd).
- 1771 has 4 digits (even).
Only 1771 qualifies, so the answer is 1.

## Hint

Use **Linear Search**: scan each number in the array, compute its digit count, and
increment a counter when that count is even.
