# Find All Duplicates in an Array

**Difficulty:** Medium

**Source:** LeetCode 442 — Find All Duplicates in an Array

## Description

Given an integer array `nums` of length `n` where every value is in the range
`[1, n]`, each integer appears **either once or twice**. Return an array of all the
integers that appear **twice**.

You must write an algorithm that runs in **O(n)** time and uses only **O(1)** extra
space (the output list is not counted against your space budget). The order of the
returned duplicates does not matter.

## Constraints

- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`
- Each element in `nums` appears **once or twice**.

## Examples

### Example 1
```
Input:  nums = [4, 3, 2, 7, 8, 2, 3, 1]
Output: [2, 3]
```
**Explanation:** n = 8. Values 2 and 3 each appear twice; all other values appear once.

### Example 2
```
Input:  nums = [1, 1, 2]
Output: [1]
```
**Explanation:** n = 3. Value 1 appears twice, so it is the only duplicate.

### Example 3
```
Input:  nums = [1, 2, 3, 4]
Output: []
```
**Explanation:** n = 4. Every value appears exactly once, so there are no duplicates.

## Hint

Use **Cyclic Sort** to send each value `v` to index `v - 1`. After the pass, any
index `i` holding a value that is not `i + 1` is holding a **duplicate** — collect
those values.
