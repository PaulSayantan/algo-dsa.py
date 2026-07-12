# Sum of Window Max and Min

**Difficulty:** Medium

**Source:** Classic — per-window max plus min

## Description

Given an integer array `nums` and a window size `k`, return a list where the `i`-th entry is the sum of the **maximum** and **minimum** of the `i`-th contiguous window of size `k`, in left-to-right order.

This is the midpoint-scaled statistic `max + min` (twice the range's midrange), a different per-window aggregation from the plain range. Run a decreasing deque for the window max and an increasing deque for the window min together, and once each full window forms read both fronts and add them.

Constraints: `1 <= k <= len(nums)`, `len(nums) <= 10^5`, `-10^4 <= nums[i] <= 10^4`.

## Examples

### Example 1

```
Input:  nums = [4,2,7,1], k = 2
Output: [6,9,8]
```

**Explanation:** Windows `[4,2]`, `[2,7]`, `[7,1]` have (max+min) = 4+2=6, 7+2=9, 7+1=8.

### Example 2

```
Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [2,0,2,2,9,10]
```

**Explanation:** Window `[1,3,-1]` gives 3+(-1)=2; `[3,-1,-3]` gives 3+(-3)=0; and so on.

## Hint

Maintain a max-deque and a min-deque together; per full window append `nums[maxd[0]] + nums[mind[0]]`.
