# Move Zeroes

**Difficulty:** Easy

**Source:** LeetCode 283 (Move Zeroes)

## Description

Given an integer array `nums`, move all `0`'s to the **end** of it while
maintaining the **relative order** of the non-zero elements.

**Note:** you must do this **in place** without making a copy of the array.

## Constraints

- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Examples

### Example 1

```
Input:  nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
```

**Explanation:** The non-zero elements `1, 3, 12` keep their original order and
move to the front; the two zeros are pushed to the end.

### Example 2

```
Input:  nums = [0]
Output: [0]
```

**Explanation:** A single zero stays where it is.

### Example 3

```
Input:  nums = [4, 0, 5, 0, 0, 7]
Output: [4, 5, 7, 0, 0, 0]
```

**Explanation:** Non-zeros `4, 5, 7` keep their relative order at the front,
followed by the three zeros.

## Hint

Use **Two Pointers (same direction / fast-slow)**. A *writer* pointer marks where
the next non-zero element should land while a *reader* scans the array; this is a
stable partition of non-zeros to the front. A follow-up swap fills the tail with
zeros.
