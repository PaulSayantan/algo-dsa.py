# Sliding Window Median

**Difficulty:** Hard

**Source:** LeetCode 480 — Sliding Window Median

## Description

The median is the middle value of an ordered list of numbers. If the list has an
even number of elements, the median is the average of the two middle values.

You are given an integer array `nums` and an integer `k`. There is a sliding window
of size `k` moving from the very left of the array to the very right. You can only
see the `k` numbers inside the window; each time the window moves right by one
position.

Return the median array for each window in the original order. Answers within
`10^-5` of the actual value are accepted.

An order-statistics tree fits perfectly: maintain the window as a dynamic multiset,
supporting `insert` (element entering), `delete` (element leaving), and `select`
(pick the middle element(s)) — each in `O(log k)`.

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Examples

### Example 1

```
Input:  nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
```

**Explanation:** The windows and their medians:
```
Window            Median
[1,  3, -1]        1
[3, -1, -3]       -1
[-1, -3, 5]       -1
[-3,  5,  3]       3
[5,   3,  6]       5
[3,   6,  7]       6
```

### Example 2

```
Input:  nums = [1, 2, 3, 4, 2, 3, 1, 4, 2], k = 3
Output: [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]
```

**Explanation:** Each window of size 3 is sorted and its middle (2nd smallest)
element taken. For example, the first window `[1,2,3]` has median `2`, and the
window `[3,4,2]` sorts to `[2,3,4]` with median `3`.

## Hint

Keep the window in an **Order-Statistics Tree** (a balanced BST augmented with
subtree sizes). Slide by `insert`-ing the entering element and `delete`-ing the
leaving one, then read the median with one `select` (odd `k`) or two `select`s
(even `k`), all in `O(log k)`.
