# Longest Bounded-Ratio Subarray

**Difficulty:** Medium

**Source:** Classic — longest window with a bounded max/min ratio

## Description

Given an array `nums` of **positive** integers and an integer `multiplier` (`>= 1`), return the length of the **longest** contiguous subarray whose maximum is at most `multiplier` times its minimum — that is, `max <= multiplier * min`.

Note this is a **ratio** constraint (`max / min <= multiplier`), not a difference constraint, which keeps the metric scale-invariant. Because the window's validity depends on both its running max and running min, maintain two monotonic deques (a decreasing max-deque and an increasing min-deque) over a variable-width window: expand the right edge each step, and while `max > multiplier * min` advance the left edge, evicting any deque front that falls out of the window.

Constraints: `0 <= len(nums) <= 10^5`, `1 <= nums[i] <= 10^9`, `multiplier >= 1`.

## Examples

### Example 1

```
Input:  nums = [2,4,3,8,5], multiplier = 2
Output: 3
```

**Explanation:** The subarray `[2,4,3]` has max 4 and min 2, and 4 <= 2*2. Extending to include 8 breaks the ratio, so the longest valid length is 3.

### Example 2

```
Input:  nums = [10,1,10,1], multiplier = 2
Output: 1
```

**Explanation:** Any pair mixes 10 and 1 (ratio 10 > 2), so no window longer than a single element is valid.

## Hint

Slide a left pointer; while `nums[maxd[0]] > multiplier * nums[mind[0]]`, increment `left` and pop any deque front whose index is now below `left`.
