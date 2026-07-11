# Maximum Gap

**Difficulty:** Hard

**Source:** LeetCode 164 — Maximum Gap

## Description

Given an integer array `nums`, return the **maximum difference between two
successive elements in its sorted form**. If the array contains fewer than two
elements, return `0`.

The twist that makes this problem interesting: you must design an algorithm that
runs in **linear time** and uses **linear extra space**. That rules out an
`O(n log n)` comparison sort as the intended solution — you need a linear-time
sorting primitive (or the bucket/pigeonhole idea that underlies it).

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

## Examples

### Example 1

```
Input:  nums = [3, 6, 9, 1]
Output: 3
Explanation: The sorted form is [1, 3, 6, 9]. The successive differences are
(3-1)=2, (6-3)=3, (9-6)=3. The maximum is 3.
```

### Example 2

```
Input:  nums = [10]
Output: 0
Explanation: The array has fewer than two elements, so by definition the answer
is 0.
```

### Example 3

```
Input:  nums = [1, 1, 1, 1]
Output: 0
Explanation: Sorted form is [1, 1, 1, 1]; every successive difference is 0, so
the maximum gap is 0.
```

### Example 4

```
Input:  nums = [100, 3, 2, 1]
Output: 97
Explanation: Sorted form is [1, 2, 3, 100]. Differences are 1, 1, 97; the
largest gap is 97 (between 3 and 100).
```

## Hint

Use **Radix Sort** to sort the array in `O(d · (n + k)) = O(n)` time (the values
are bounded by `10^9`, so a fixed number of digit passes suffices), then make a
single linear scan over the sorted array tracking the maximum adjacent
difference.
