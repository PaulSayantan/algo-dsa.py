# Sum of Subarray Minimums

**Difficulty:** Medium

**Source:** LeetCode 907 — Sum of Subarray Minimums

## Description

Given an array of integers `arr`, find the **sum of `min(b)`** over every (contiguous)
subarray `b` of `arr`. Since the answer may be large, return it **modulo** `10^9 + 7`.

A subarray is a contiguous, non-empty slice of `arr`. For each such slice you take its
minimum element, and you add up all those minimums.

## Constraints

- `1 <= arr.length <= 3 * 10^4`
- `1 <= arr[i] <= 3 * 10^4`

## Examples

### Example 1

```
Input:  arr = [3, 1, 2, 4]
Output: 17
```

**Explanation:** The subarrays and their minimums are:
`[3]=3, [1]=1, [2]=2, [4]=4, [3,1]=1, [1,2]=1, [2,4]=2, [3,1,2]=1, [1,2,4]=1, [3,1,2,4]=1`.
Summing: `3 + 1 + 2 + 4 + 1 + 1 + 2 + 1 + 1 + 1 = 17`.

### Example 2

```
Input:  arr = [11, 81, 94, 43, 3]
Output: 444
```

**Explanation:** Grouping by subarray length, the sums of minimums are
`232 (len 1) + 138 (len 2) + 57 (len 3) + 14 (len 4) + 3 (len 5) = 444`.

## Hint

Instead of enumerating subarrays, count each element's **contribution**: for `arr[i]`, use a
**Monotonic Stack / Queue** to find how many subarrays have `arr[i]` as their minimum
(previous-smaller and next-smaller boundaries). Multiply span counts by the value.
