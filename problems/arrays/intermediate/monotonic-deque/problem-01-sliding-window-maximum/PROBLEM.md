# Sliding Window Maximum

**Difficulty:** Medium (widely considered Hard for the O(n) solution)

**Source:** LeetCode 239 — Sliding Window Maximum

## Description

You are given an array of integers `nums` and an integer `k`. A sliding window
of size `k` moves from the very left of the array to the very right. At each
step the window slides one position to the right, so it always covers exactly
`k` consecutive elements.

Return an array containing the **maximum** value in each window, in order. If the
array has `n` elements, there are `n - k + 1` windows and therefore `n - k + 1`
values in the answer.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Examples

### Example 1

```
Input:  nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
```

**Explanation:**

| Window                 | Max |
|------------------------|-----|
| `[1, 3, -1]`           | 3   |
| `[3, -1, -3]`          | 3   |
| `[-1, -3, 5]`          | 5   |
| `[-3, 5, 3]`           | 5   |
| `[5, 3, 6]`            | 6   |
| `[3, 6, 7]`            | 7   |

### Example 2

```
Input:  nums = [1], k = 1
Output: [1]
```

**Explanation:** There is a single window `[1]`, whose maximum is `1`.

### Example 3

```
Input:  nums = [9, 10, 9, -7, -4, -8, 2, -6], k = 5
Output: [10, 10, 9, 2]
```

**Explanation:** The four windows are `[9,10,9,-7,-4] -> 10`,
`[10,9,-7,-4,-8] -> 10`, `[9,-7,-4,-8,2] -> 9`, and `[-7,-4,-8,2,-6] -> 2`.

## Hint

Use a **Monotonic Deque** of **indices** kept in decreasing order of value. Pop
from the back any index whose value is dominated by the incoming element, and
pop from the front any index that has slid out of the window. The front always
holds the current window's maximum.
