# Range of Each Sliding Window

**Difficulty:** Medium

**Source:** Classic — per-window max minus min

## Description

Given an integer array `nums` and a window size `k`, return a list where the `i`-th entry is the **range** (maximum minus minimum) of the `i`-th contiguous window of size `k`, in left-to-right order. Use one decreasing deque for the window max and one increasing deque for the window min.

## Examples

### Example 1

```
Input:  nums = [4,2,7,1], k = 2
Output: [2,5,6]
```

**Explanation:** Windows [4,2],[2,7],[7,1] have ranges 2,5,6.

## Hint

Maintain a max-deque and a min-deque together; per window append nums[maxd[0]] - nums[mind[0]].
