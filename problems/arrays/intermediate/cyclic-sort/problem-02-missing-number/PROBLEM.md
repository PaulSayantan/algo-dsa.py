# Missing Number

**Difficulty:** Easy

**Source:** LeetCode 268 — Missing Number

## Description

Given an array `nums` containing `n` **distinct** numbers taken from the range
`[0, n]`, exactly one number in that range is missing from the array. Return the
missing number.

For example, if `n = 3` the array should contain three of the four numbers
`{0, 1, 2, 3}`; your job is to report the one that is absent.

Aim for a solution that runs in **O(n)** time and uses only **O(1)** extra space.

## Constraints

- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- All the numbers in `nums` are **distinct**.

## Examples

### Example 1
```
Input:  nums = [3, 0, 1]
Output: 2
```
**Explanation:** n = 3. The range is [0, 3]. The numbers 0, 1, 3 are present, so 2 is missing.

### Example 2
```
Input:  nums = [0, 1]
Output: 2
```
**Explanation:** n = 2. The range is [0, 2]. Both 0 and 1 are present, so 2 (the top of the range) is missing.

### Example 3
```
Input:  nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
Output: 8
```
**Explanation:** n = 9. Every value in [0, 9] appears except 8.

## Hint

Use **Cyclic Sort** on a `[0..n]` range — value `v` belongs at index `v`. After
placing everything home, the first index whose value isn't equal to the index
reveals the missing number (and if all match, the answer is `n`).
