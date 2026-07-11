# Maximum Sum Subarray of Size K

**Difficulty:** Easy

**Source:** Classic (GeeksforGeeks "Maximum sum subarray of size K"; a staple sliding-window warm-up)

## Description

You are given an array of integers `nums` and a positive integer `k`. Among all
**contiguous** subarrays that contain exactly `k` elements, return the **largest
possible sum**.

A subarray is a run of consecutive elements — you may not skip elements or reorder
them. It is guaranteed that `1 <= k <= nums.length`, so at least one valid window
exists.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Examples

### Example 1

```
Input:  nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
```

**Explanation:** The length-3 windows are `[2,1,5]=8`, `[1,5,1]=7`, `[5,1,3]=9`,
`[1,3,2]=6`. The maximum is `9` from the window `[5,1,3]`.

### Example 2

```
Input:  nums = [2, 3, 4, 1, 5], k = 2
Output: 7
```

**Explanation:** The length-2 windows sum to `5, 7, 5, 6`. The best is `7` from
`[3,4]`.

### Example 3

```
Input:  nums = [-1, -2, -3, -4], k = 2
Output: -3
```

**Explanation:** All values are negative. The windows sum to `-3, -5, -7`, and the
maximum (least negative) is `-3` from `[-1,-2]`.

## Hint

Use a **Sliding Window (fixed size)**. Compute the sum of the first `k` elements once,
then slide the window one step at a time — add the new right element and subtract the
one that falls off the left — instead of re-summing every window from scratch.
