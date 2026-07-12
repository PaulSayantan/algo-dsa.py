# Shortest Subarray With Range At Least K

**Difficulty:** Medium

**Source:** Classic — shortest window whose max - min is at least K

## Description

Given an integer array `nums` and an integer `k`, return the length of the **shortest** non-empty contiguous subarray whose range (`max - min`) is `>= k`. If no such subarray exists, return `-1`.

Because widening a window can only raise its max and lower its min, the range is non-decreasing as the window grows: for each right end there is a longest prefix of valid left starts. Slide the right edge forward, and whenever the current window already satisfies `max - min >= k`, shrink from the left as far as possible while the condition still holds, tracking the smallest width seen.

Constraints: `1 <= len(nums)`, `0 <= k`.

## Examples

### Example 1

```
Input:  nums = [1,3,6,2,4], k = 5
Output: 3
```

**Explanation:** No length-2 window reaches a range of 5 (the widest is `[6,2]` with range 4), but `[1,3,6]` has `max - min = 6 - 1 = 5`, so the shortest qualifying width is 3.

### Example 2

```
Input:  nums = [4,1,7,2], k = 3
Output: 2
```

**Explanation:** `[4,1]` already has `max - min = 3`, so a width of 2 suffices.

### Example 3

```
Input:  nums = [1,2,3], k = 10
Output: -1
```

**Explanation:** The whole array only spans `3 - 1 = 2 < 10`, so no subarray qualifies.

## Hint

Run two monotonic deques (a decreasing one for the window max, an increasing one for the window min). After appending each right index, while `max - min >= k` record `right - left + 1` and advance `left`, evicting any deque front that leaves the window.
