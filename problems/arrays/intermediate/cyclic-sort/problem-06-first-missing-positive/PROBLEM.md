# First Missing Positive

**Difficulty:** Hard

**Source:** LeetCode 41 — First Missing Positive

## Description

Given an **unsorted** integer array `nums`, return the smallest **positive** integer
that is **not present** in `nums`.

Unlike the earlier problems, `nums` here is arbitrary: it may contain negative
numbers, zeros, duplicates, and values far larger than `n`. Despite that, you must
run in **O(n)** time and use only **O(1)** auxiliary space.

Key fact that unlocks O(1) space: for an array of length `n`, the answer is always
somewhere in `[1, n + 1]`. Values `<= 0` or `> n` can never be the first missing
positive within reach, so they can be ignored during placement.

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Must run in **O(n)** time and **O(1)** auxiliary space.

## Examples

### Example 1
```
Input:  nums = [1, 2, 0]
Output: 3
```
**Explanation:** n = 3. Both 1 and 2 are present, so the smallest missing positive is 3.

### Example 2
```
Input:  nums = [3, 4, -1, 1]
Output: 2
```
**Explanation:** 1 is present but 2 is not, so the answer is 2. Negatives are irrelevant.

### Example 3
```
Input:  nums = [7, 8, 9, 11, 12]
Output: 1
```
**Explanation:** None of 1..5 appear (all values exceed n), so the smallest missing positive is 1.

## Hint

Use **Cyclic Sort**, but only place values that fall in `[1, n]` (skip zeros,
negatives, and out-of-range values). After the pass, the first index `i` with
`nums[i] != i + 1` gives answer `i + 1`; if all match, the answer is `n + 1`.
