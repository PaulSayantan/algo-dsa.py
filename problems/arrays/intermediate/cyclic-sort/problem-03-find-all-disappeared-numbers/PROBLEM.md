# Find All Numbers Disappeared in an Array

**Difficulty:** Easy

**Source:** LeetCode 448 — Find All Numbers Disappeared in an Array

## Description

You are given an array `nums` of `n` integers where each value is in the range
`[1, n]` (inclusive). Some numbers appear **twice** and others appear **once**,
which means some numbers in `[1, n]` do **not** appear at all.

Return a list of all the integers in the range `[1, n]` that do **not** appear in
`nums`. The order of the returned numbers does not matter.

Follow-up: can you do it in **O(n)** time using only **O(1)** extra space (the
returned list does not count as extra space)?

## Constraints

- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`

## Examples

### Example 1
```
Input:  nums = [4, 3, 2, 7, 8, 2, 3, 1]
Output: [5, 6]
```
**Explanation:** n = 8. The values present are {1,2,3,4,7,8}; the numbers in [1,8] that never appear are 5 and 6.

### Example 2
```
Input:  nums = [1, 1]
Output: [2]
```
**Explanation:** n = 2. Value 1 appears twice and 2 is missing, so the answer is [2].

### Example 3
```
Input:  nums = [2, 2]
Output: [1]
```
**Explanation:** n = 2. Value 2 appears twice and 1 never appears, so 1 is disappeared.

## Hint

Use **Cyclic Sort** to send each value `v` to index `v - 1`. Duplicates block some
slots; after the pass, every index `i` whose value isn't `i + 1` marks a
disappeared number `i + 1`.
