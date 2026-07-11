# Longest Consecutive Sequence

**Difficulty:** Medium/Hard

**Source:** LeetCode 128 (Longest Consecutive Sequence)

## Description

Given an unsorted array of integers `nums`, return the length of the longest run
of **consecutive integers** (values that differ by 1, in any order within the
array). The elements of the run need not be adjacent in the array.

You must design an algorithm that runs in **O(n)** time.

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- The array may contain duplicates.

## Examples

### Example 1

```
Input:  nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive run is [1, 2, 3, 4], which has length 4.
The values 100 and 200 are isolated.
```

### Example 2

```
Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
Explanation: The run 0, 1, 2, 3, 4, 5, 6, 7, 8 is present (the duplicate 0 does
not extend it), giving length 9.
```

### Example 3

```
Input:  nums = []
Output: 0
Explanation: An empty array has no consecutive run, so the answer is 0.
```

## Hint

Use **Hashing**: put every value in a hash set for O(1) membership tests. Only
start counting a run from a value `x` when `x - 1` is absent (so `x` is the start
of its run), then walk `x, x+1, x+2, ...` upward using the set.
