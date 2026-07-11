# Smallest Subarrays With Maximum Bitwise OR

**Difficulty:** Medium

**Source:** LeetCode 2411

## Description

You are given a **0-indexed** array `nums` of length `n`, consisting of non-negative
integers.

For each index `i` (`0 <= i < n`), consider all subarrays that **start at `i`**, i.e.
`nums[i..j]` for `i <= j < n`. Among these, look at the ones whose bitwise OR is as
**large as possible**. Let `answer[i]` be the length `j - i + 1` of the **shortest**
such subarray (the smallest `j >= i` for which `OR(nums[i..j])` equals the maximum
achievable OR of any subarray starting at `i`).

Return the array `answer`.

Note: the OR of a subarray only ever **grows** as you extend it to the right (bits are
never removed), so the maximum OR for start `i` equals `OR(nums[i..n-1])`.

## Constraints

- `1 <= n <= 10^5`
- `0 <= nums[i] <= 10^9`

## Examples

### Example 1

```
Input:  nums = [1, 0, 2, 1, 3]
Output: [3, 3, 2, 2, 1]
```

Explanation (max OR for each start is OR of the suffix):
- `i = 0`: suffix OR = `1|0|2|1|3 = 3`. Shortest prefix reaching 3 is `[1,0,2]` → length 3.
- `i = 1`: suffix OR = `0|2|1|3 = 3`. Shortest is `[0,2,1]` → length 3.
- `i = 2`: suffix OR = `2|1|3 = 3`. Shortest is `[2,1]` → length 2.
- `i = 3`: suffix OR = `1|3 = 3`. Shortest is `[1,3]` → length 2.
- `i = 4`: suffix OR = `3`. `[3]` → length 1.

### Example 2

```
Input:  nums = [1, 2]
Output: [2, 1]
```

Explanation:
- `i = 0`: max OR = `1|2 = 3`, needs both elements → length 2.
- `i = 1`: max OR = `2`, single element → length 1.

## Hint

Bitwise OR is **idempotent** (`x | x = x`) and **monotone** when extending a window, so
`OR(nums[i..j])` is queryable in O(1) with a **Sparse Table**. For each start `i`, the
target OR is `OR(nums[i..n-1])`; **binary search** the smallest `j` whose prefix OR from
`i` reaches that target, using the Sparse Table to evaluate each candidate.
