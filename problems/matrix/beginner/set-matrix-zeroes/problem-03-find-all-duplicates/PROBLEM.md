# Find All Duplicates in an Array

**Difficulty:** Medium

**Source:** LeetCode 442 — Find All Duplicates in an Array

## Description

Given an integer array `nums` of length `n` where all the integers are in the
range `[1, n]` and each integer appears **once or twice**, return an array of
all the integers that appear **twice**.

You must write an algorithm that runs in `O(n)` time and uses only **constant
extra space** (the output list does not count). As with the rest of this
section, the trick is to let the array flag itself: each value `v` points at
index `v - 1`, and the *second* time you visit that index you know `v` is a
duplicate.

## Constraints

- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`
- Each element in `nums` appears **once or twice**.

## Examples

### Example 1

```
Input:  nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
```

**Explanation:** The values `2` and `3` each appear twice; every other value
appears once. Order of the output does not matter, so `[3,2]` is equally valid.

### Example 2

```
Input:  nums = [1,1,2]
Output: [1]
```

**Explanation:** Only `1` appears twice.

### Example 3

```
Input:  nums = [1]
Output: []
```

**Explanation:** A single element that appears once — there are no duplicates.

## Hint

Apply the **Set Matrix Zeroes** family of in-place sign marking. Visit index
`abs(v) - 1` for each value `v`; if that slot is **already negative**, this is
the second time you have reached it, so `abs(v)` is a duplicate. Otherwise
negate the slot to mark the first visit.
