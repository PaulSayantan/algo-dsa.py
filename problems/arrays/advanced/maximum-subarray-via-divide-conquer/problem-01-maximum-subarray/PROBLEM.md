# Maximum Subarray

**Difficulty:** Easy/Medium

**Source:** LeetCode 53 — Maximum Subarray (also CLRS 4.1)

## Description

Given an integer array `nums`, find the contiguous subarray (containing at least
one number) which has the largest sum, and return that sum.

A *subarray* is a contiguous, non-empty slice of the array. You do **not** need to
return the subarray itself — only its sum.

While this problem is famously solvable in linear time with Kadane's algorithm,
here we practice the **divide & conquer** formulation: split the array in half,
solve each half, and stitch the two solutions together by considering the best
subarray that straddles the midpoint.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- The array always has at least one element, so the answer is always defined
  (it may be negative if every element is negative).

## Examples

### Example 1

```
Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum, 4 + (-1) + 2 + 1 = 6.
```

### Example 2

```
Input:  nums = [1]
Output: 1
Explanation: The only subarray is [1], with sum 1.
```

### Example 3

```
Input:  nums = [5, 4, -1, 7, 8]
Output: 23
Explanation: The whole array [5, 4, -1, 7, 8] sums to 23, and no proper subarray beats it.
```

### Example 4

```
Input:  nums = [-3, -1, -2]
Output: -1
Explanation: Every element is negative, so the best we can do is the single element -1.
```

## Hint

Use **Maximum Subarray via Divide & Conquer**: recurse on the left half and the
right half, then compute the best subarray that crosses the midpoint as the best
suffix of the left plus the best prefix of the right. The answer is the max of the
three.
