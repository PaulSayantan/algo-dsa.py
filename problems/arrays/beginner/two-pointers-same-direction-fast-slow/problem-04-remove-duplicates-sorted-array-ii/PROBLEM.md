# Remove Duplicates from Sorted Array II

**Difficulty:** Medium

**Source:** LeetCode 80 (Remove Duplicates from Sorted Array II)

## Description

Given an integer array `nums` sorted in **non-decreasing order**, remove some
duplicates **in place** such that each unique element appears **at most twice**.
The relative order of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you
must instead have the result placed in the **first part** of the array `nums`.
More formally, if there are `k` elements after removing the duplicates, then the
first `k` elements of `nums` should hold the final result. The elements beyond
the first `k` positions do not matter.

Return `k`.

You must do this using only O(1) extra space.

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.

## Examples

### Example 1

```
Input:  nums = [1, 1, 1, 2, 2, 3]
Output: 5, nums = [1, 1, 2, 2, 3, _]
```

**Explanation:** Your function should return `k = 5`, with the first five
elements being `1, 1, 2, 2, 3`. The third `1` is removed because `1` may appear
at most twice.

### Example 2

```
Input:  nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
Output: 7, nums = [0, 0, 1, 1, 2, 3, 3, _, _]
```

**Explanation:** Your function should return `k = 7`, with the first seven
elements being `0, 0, 1, 1, 2, 3, 3`. Two extra `1`'s are removed (four `1`'s
become two).

### Example 3

```
Input:  nums = [1, 1]
Output: 2, nums = [1, 1]
```

**Explanation:** `1` appears exactly twice, which is allowed, so nothing is
removed and `k = 2`.

## Hint

Use **Two Pointers (same direction / fast-slow)**. This is the general form of
"keep at most `m` copies": compare the reader's candidate against the element
`m` positions behind the writer (`nums[write - 2]` for `m = 2`) to decide whether
there is still room to keep it.
