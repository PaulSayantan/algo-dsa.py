# Find All Numbers Disappeared in an Array

**Difficulty:** Easy

**Source:** LeetCode 448 — Find All Numbers Disappeared in an Array

## Description

You are given an array `nums` of `n` integers where each `nums[i]` is in the
range `[1, n]` (`n` being the length of the array). Some integers appear twice
and others are missing entirely.

Return an array of all the integers in the range `[1, n]` that **do not** appear
in `nums`.

The classic follow-up — and the whole point of this exercise — is to do it
**without allocating extra space** (the returned list does not count) and in
`O(n)` time. Because every legal value is itself a valid *index* (after
subtracting 1), you can use the array as its own bookkeeping structure by
flipping the sign of the slot that each value "points at".

## Constraints

- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`

## Examples

### Example 1

```
Input:  nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
```

**Explanation:** `n = 8`, so the full range is `1..8`. The values present are
`{1,2,3,4,7,8}`. The values `5` and `6` never appear, so they are returned.

### Example 2

```
Input:  nums = [1,1]
Output: [2]
```

**Explanation:** `n = 2`, so the range is `1..2`. The value `1` appears (twice),
but `2` is missing, so the answer is `[2]`.

### Example 3

```
Input:  nums = [1,2,3,4]
Output: []
```

**Explanation:** Every value in `1..4` is present exactly once, so nothing is
disappeared and the result is empty.

## Hint

Use the **Set Matrix Zeroes** family of in-place marking. Every value `v` maps
to index `v - 1`; mark that slot as "seen" by negating `nums[v-1]`, using
`abs()` when you read a value so a previously flipped sign does not corrupt the
lookup. Indices that remain positive after one pass were never visited.
