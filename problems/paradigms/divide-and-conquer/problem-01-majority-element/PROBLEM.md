# Majority Element

**Difficulty:** Easy

**Source:** LeetCode 169 (Majority Element)

## Description

Given an array `nums` of size `n`, return the **majority element** — the element that
appears **more than `⌊n / 2⌋` times**.

You may assume that a majority element **always exists** in the array.

While this problem has a famous `O(1)`-space Boyer–Moore voting solution, it is also a
clean introduction to **Divide and Conquer**: the majority of the whole array must be
the majority of at least one of its two halves, so you can recurse on halves and
resolve the answer with a linear count in the combine step.

## Constraints

- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`
- A majority element always exists.

## Examples

### Example 1

```
Input:  nums = [3, 2, 3]
Output: 3
```

Explanation: `n = 3`, so a majority element must appear more than `⌊3/2⌋ = 1` time.
`3` appears twice, so `3` is the majority element.

### Example 2

```
Input:  nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
```

Explanation: `n = 7`, so a majority element must appear more than `⌊7/2⌋ = 3` times.
`2` appears 4 times (indices 0, 1, 5, 6), which is more than 3, so the answer is `2`.

### Example 3

```
Input:  nums = [7]
Output: 7
```

Explanation: A single element is trivially the majority of a length-1 array.

## Hint

Use **Divide and Conquer**: split the array in half and find the majority of each
half. The overall majority must be a majority in the left half, the right half, or
both. Compare the two candidates by counting their occurrences across the full range,
and return whichever actually dominates.
