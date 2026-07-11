# Rotate Array

**Difficulty:** Medium

**Source:** LeetCode 189 — Rotate Array

## Description

Given an integer array `nums`, rotate the array to the **right** by `k` steps,
where `k` is non-negative.

Rotating right by one step means each element moves one position to the right,
and the last element wraps around to the front. After `k` steps, the last `k`
elements (in order) become the leading elements of the array.

Try to solve it **in place** with **O(1) extra space**. There is a well-known
follow-up asking for exactly this — the reversal trick achieves it.

Note that `k` may be larger than the array length, so a rotation by `k` is the
same as a rotation by `k % n`.

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

## Examples

### Example 1

```
Input:  nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

Explanation: The last 3 elements `[5,6,7]` move to the front; the first 4
elements `[1,2,3,4]` shift to the back. Rotating right by 3.

### Example 2

```
Input:  nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
```

Explanation: `k = 2`, and `n = 4`, so `k % n = 2`. The last 2 elements
`[3,99]` move to the front, giving `[3,99,-1,-100]`.

### Example 3

```
Input:  nums = [1,2], k = 3
Output: [2,1]
```

Explanation: `k % n = 3 % 2 = 1`, so this is a single right rotation: the last
element `2` moves to the front.

## Hint

Use the **Rotate Array (reversal trick)**: reduce `k` modulo `n`, reverse the
entire array, then reverse the first `k` and the last `n - k` elements
separately.
