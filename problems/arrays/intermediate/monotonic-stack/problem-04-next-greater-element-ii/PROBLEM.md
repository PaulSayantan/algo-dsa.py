# Next Greater Element II

**Difficulty:** Medium

**Source:** LeetCode 503 — Next Greater Element II

## Description

Given a **circular** integer array `nums` (i.e. the next element of
`nums[nums.length - 1]` is `nums[0]`), return the *next greater number* for every
element in `nums`.

The **next greater number** of an element `x` is the first strictly greater
number encountered when traversing the array in order, starting from the element
right after `x` and wrapping around the end back to the beginning. If it does not
exist, the answer for that element is `-1`.

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`

## Examples

### Example 1

```
Input:  nums = [1, 2, 1]
Output: [2, -1, 2]
```

**Explanation:**
- For `nums[0] = 1`: the next greater number is `2`.
- For `nums[1] = 2`: no number is greater (even wrapping around), so `-1`.
- For `nums[2] = 1`: searching forward wraps around to `nums[0]`... but the first
  strictly greater is `nums[1] = 2`, so `2`.

### Example 2

```
Input:  nums = [1, 2, 3, 4, 3]
Output: [2, 3, 4, -1, 4]
```

**Explanation:**
- `1 -> 2`, `2 -> 3`, `3 -> 4`.
- `nums[3] = 4` is the maximum; nothing is greater even after wrapping -> `-1`.
- `nums[4] = 3` wraps around and finds `4` at index 3... it wraps to the front
  and the first strictly greater value is `4` -> `4`.

### Example 3

```
Input:  nums = [5, 4, 3, 2, 1]
Output: [-1, 5, 5, 5, 5]
```

**Explanation:** The leading `5` is the global maximum, so it has no greater
element -> `-1`. Every smaller element wraps around and finds the `5` -> `5`.

## Hint

Simulate the circular array by iterating the indices **twice** (`0 .. 2n-1`,
using `i % n`) while maintaining a single decreasing **Monotonic Stack** of
indices. The second pass lets elements near the end "see" the wrap-around
candidates at the front.
