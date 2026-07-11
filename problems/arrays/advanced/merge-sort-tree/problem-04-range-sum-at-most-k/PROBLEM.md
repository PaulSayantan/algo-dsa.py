# Range Sum of Elements ≤ K

**Difficulty:** Hard

Source: Classic **augmented Merge Sort Tree** problem (appears in competitive-programming
judges as "sum of elements not exceeding a threshold in a range"; a natural extension of
the count query).

## Description

You are given a static integer array `nums` of length `n`. Answer `q` queries. Each query
is a triple `(l, r, k)` and asks:

> What is the **sum of all elements** `nums[p]` with `l <= p <= r` and `nums[p] <= k`?

Indices `l`, `r` are **0-based and inclusive**. Return one answer per query, in order.

Counting elements `<= k` is not enough here — you need their *sum*. The trick is to
augment each Merge Sort Tree node with a **prefix-sum array** of its sorted list. After a
binary search locates the position of `k`, the sum of the qualifying prefix is read off
the prefix-sum array in `O(1)`.

## Constraints

- `1 <= n <= 10^5`
- `1 <= q <= 10^5`
- `-10^9 <= nums[p] <= 10^9`
- `-10^9 <= k <= 10^9`
- `0 <= l <= r <= n - 1`
- The answer fits in a 64-bit signed integer.

## Examples

### Example 1

```
Input:  nums = [3, 1, 4, 1, 5], queries = [[0, 4, 3], [1, 3, 4], [0, 4, 0]]
Output: [5, 6, 0]
```

Explanation:
- Query `(0, 4, 3)`: whole array; elements `<= 3` are `3, 1, 1`; sum = `3 + 1 + 1 = 5`.
- Query `(1, 3, 4)`: subarray `[1, 4, 1]`; elements `<= 4` are `1, 4, 1`; sum = `6`.
- Query `(0, 4, 0)`: no element is `<= 0`; sum = `0`.

### Example 2

```
Input:  nums = [-2, 7, -2, 3], queries = [[0, 3, 0], [0, 3, 7], [1, 1, 6]]
Output: [-4, 6, 0]
```

Explanation:
- Query `(0, 3, 0)`: elements `<= 0` are `-2, -2`; sum = `-4`.
- Query `(0, 3, 7)`: all elements `<= 7`: `-2 + 7 - 2 + 3 = 6`.
- Query `(1, 1, 6)`: subarray `[7]`; `7 <= 6` is false; sum = `0`.

## Hint

Build a **Merge Sort Tree** but store, in each node, both the sorted list **and** its
prefix-sum array. Binary search (`upper_bound`) for `k` to find how many elements qualify,
then read the corresponding prefix sum to get their total in `O(1)`.
