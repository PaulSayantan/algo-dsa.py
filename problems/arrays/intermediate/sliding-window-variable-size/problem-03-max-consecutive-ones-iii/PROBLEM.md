# Max Consecutive Ones III

**Difficulty:** Medium

**Source:** LeetCode 1004 — Max Consecutive Ones III

## Description

You are given a binary array `nums` (containing only `0`s and `1`s) and an integer
`k`. You may flip **at most `k`** of the `0`s to `1`s.

Return the length of the **longest contiguous subarray** that contains only `1`s
after performing at most `k` flips.

Equivalently: find the longest contiguous window that contains **at most `k`
zeros** (those zeros are the ones you would flip).

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.
- `0 <= k <= nums.length`

## Examples

### Example 1

```
Input:  nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: Flip the two 0s at indices 3 and 4. The subarray from index 3 to 8
             becomes [1,1,1,1,1,1] (originally [0,0,1,1,1,1]), length 6.
```

### Example 2

```
Input:  nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: Flipping three well-chosen 0s yields a run of 10 ones, e.g. the
             window from index 2 to 11: [1,1,0,0,1,1,1,0,1,1] has exactly three
             0s, all flippable, giving length 10.
```

### Example 3

```
Input:  nums = [0,0,0,0], k = 0
Output: 0
Explanation: With no flips allowed and no 1s present, the longest all-ones
             subarray is empty, length 0.
```

## Hint

Use a **Sliding Window (variable size)**. Grow the window while it holds at most
`k` zeros; when a `(k+1)`-th zero enters, shrink from the left until the zero
count drops back to `k`. Track the widest valid window.
