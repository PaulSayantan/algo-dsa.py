# Set Mismatch

**Difficulty:** Easy / Medium

**Source:** LeetCode 645 — Set Mismatch

## Description

You have a set that originally contained all the integers from `1` to `n`. Due to an
error, **one** of the numbers got **duplicated** — it now appears twice — which in
turn caused **another** number in `[1, n]` to go **missing**. You are given the
corrupted array `nums` (length `n`).

Return a two-element array `[duplicated, missing]`: the number that appears twice
followed by the number that is missing.

## Constraints

- `n == nums.length`
- `1 <= n <= 10^4`
- `1 <= nums[i] <= n`
- Exactly one number is duplicated and exactly one number in `[1, n]` is missing.

## Examples

### Example 1
```
Input:  nums = [1, 2, 2, 4]
Output: [2, 3]
```
**Explanation:** n = 4. Value 2 appears twice, and value 3 (which should be present) is missing.

### Example 2
```
Input:  nums = [1, 1]
Output: [1, 2]
```
**Explanation:** n = 2. Value 1 is duplicated, and 2 is missing.

### Example 3
```
Input:  nums = [3, 2, 3, 4, 6, 5]
Output: [3, 1]
```
**Explanation:** n = 6. Value 3 appears twice, and value 1 is missing.

## Hint

Use **Cyclic Sort** to send each value `v` to index `v - 1`. After the pass, the one
index `i` whose value isn't `i + 1` reveals both answers at once: `nums[i]` is the
duplicate and `i + 1` is the missing number.
