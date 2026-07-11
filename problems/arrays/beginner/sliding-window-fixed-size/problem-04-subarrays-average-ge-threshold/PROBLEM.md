# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

**Difficulty:** Medium

**Source:** LeetCode 1343 — "Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold"

## Description

Given an array of integers `arr` and two integers `k` and `threshold`, return the
**number of contiguous subarrays of size `k`** whose **average** is greater than or
equal to `threshold`.

## Constraints

- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 10^4`
- `1 <= k <= arr.length`
- `0 <= threshold <= 10^4`

## Examples

### Example 1

```
Input:  arr = [2, 2, 2, 2, 5, 5, 5, 8], k = 3, threshold = 4
Output: 3
```

**Explanation:** A window qualifies when its sum is at least `k * threshold = 12`.
The length-3 window sums are `6, 6, 9, 12, 15, 18`. Three of them (`12`, `15`, `18`,
i.e. windows `[2,5,5]`, `[5,5,5]`, `[5,5,8]`) reach the required sum, so the answer is
`3`.

### Example 2

```
Input:  arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k = 3, threshold = 5
Output: 6
```

**Explanation:** The required window sum is `k * threshold = 15`. The length-3 window
sums are `41, 53, 69, 83, 67, 43, 14, 10`. All except the last two (`14`, `10`) reach
`15`, giving `6` qualifying windows.

### Example 3

```
Input:  arr = [1, 1, 1, 1, 1], k = 2, threshold = 3
Output: 0
```

**Explanation:** The required window sum is `2 * 3 = 6`, but every length-2 window sums
to only `2`, so no window qualifies.

## Hint

Use a **Sliding Window (fixed size)**. Avoid floating point entirely: a window's
average is `>= threshold` exactly when its **sum** is `>= k * threshold`. Maintain the
window sum incrementally and count how many windows meet that integer bound.
