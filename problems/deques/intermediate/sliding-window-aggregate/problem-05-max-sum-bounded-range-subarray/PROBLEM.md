# Maximum Sum of a Bounded-Range Subarray

**Difficulty:** Medium

**Source:** Classic — largest subarray sum under a max - min range cap

## Description

Given an array `nums` of **positive** integers and an integer `limit`, return the largest possible sum of a non-empty contiguous subarray whose range (`max - min`) is `<= limit`.

Because every value is positive, longer valid windows always have larger sums, so we want the widest window that still satisfies the range cap ending at each position. Slide a variable-size window: expand the right edge and add the new value to a running sum; whenever `max - min > limit`, drop values from the left (subtracting them from the running sum) until the window is valid again. Track the maximum running sum over all valid windows.

Constraints: `1 <= len(nums)`, every `nums[i] >= 1`, `0 <= limit`.

## Examples

### Example 1

```
Input:  nums = [1,3,6,2,4], limit = 2
Output: 6
```

**Explanation:** `[2,4]` has `max - min = 2 <= 2` and sum `6`. No valid window sums higher (e.g. `[1,3]` sums to 4, and any window containing 6 alongside a neighbour breaks the cap).

### Example 2

```
Input:  nums = [8,2,4,7], limit = 4
Output: 11
```

**Explanation:** `[4,7]` has `max - min = 3 <= 4` and sum `11`, the largest bounded-range sum.

### Example 3

```
Input:  nums = [10,1,2,4,7,2], limit = 5
Output: 15
```

**Explanation:** `[2,4,7,2]` has `max - min = 7 - 2 = 5 <= 5` and sum `15`.

## Hint

Two monotonic deques give the window max and min; keep a running window sum. While `max - min > limit`, subtract `nums[left]` and advance `left`, evicting stale deque fronts, then update the answer with the current window sum.
