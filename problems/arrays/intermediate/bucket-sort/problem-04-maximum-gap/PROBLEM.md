# Maximum Gap

**Difficulty:** Hard

**Source:** LeetCode 164 — Maximum Gap

## Description

Given an integer array `nums`, return the **maximum difference between two
successive elements in its sorted form**. If the array contains fewer than two
elements, return `0`.

You must write an algorithm that runs in **linear time** and uses **linear extra
space**. (This constraint is what rules out simply calling a comparison sort.)

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

## Examples

### Example 1

```
Input:  nums = [3, 6, 9, 1]
Output: 3
Explanation: The sorted form is [1, 3, 6, 9]. The successive differences are
3 - 1 = 2, 6 - 3 = 3, and 9 - 6 = 3. The maximum is 3.
```

### Example 2

```
Input:  nums = [10]
Output: 0
Explanation: The array contains fewer than two elements, so by definition the
answer is 0.
```

### Example 3

```
Input:  nums = [1, 10, 5, 3]
Output: 5
Explanation: The sorted form is [1, 3, 5, 10]. Successive differences are
3 - 1 = 2, 5 - 3 = 2, and 10 - 5 = 5. The maximum is 5.
```

## Hint

Sorting outright costs `O(n log n)`. Instead, spread the `n` values across about
`n` equal-width **buckets** (pigeonhole). Because there are more buckets than
gaps between them, the maximum gap must occur **between** buckets, not inside
one — so you only need each bucket's min and max. This is a **Bucket Sort** /
pigeonhole argument that gives `O(n)`.
