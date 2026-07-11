# Sort an Array

**Difficulty:** Medium/Hard

**Source:** LeetCode 912 — Sort an Array

## Description

Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem **without using any built-in sorting functions** (no
`sorted`/`list.sort`), and you should aim for a solution with **O(n log n)** time complexity
and the smallest space complexity you can manage.

Note that the input can contain **duplicate** values and can be **large** (up to `5 * 10^4`
elements), and adversarial orderings (already sorted, reverse sorted, many equal keys) are
possible — your algorithm should handle these efficiently.

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

## Examples

### Example 1

```
Input:  nums = [5, 2, 3, 1]
Output: [1, 2, 3, 5]
```

**Explanation:** After sorting in ascending order, `1 < 2 < 3 < 5`.

### Example 2

```
Input:  nums = [5, 1, 1, 2, 0, 0]
Output: [0, 0, 1, 1, 2, 5]
```

**Explanation:** The array contains duplicates (`0` and `1` appear twice). All copies are
kept and placed in non-decreasing order.

### Example 3

```
Input:  nums = [3, 3, 3]
Output: [3, 3, 3]
```

**Explanation:** All elements are equal, so the sorted array is identical to the input. A
good implementation must not degrade to O(n^2) on all-equal input.

## Hint

Use **Randomization**: quicksort with a **random pivot** (and, for robustness against many
duplicates, three-way / Dutch-national-flag partitioning). The random pivot yields
O(n log n) *expected* time and prevents adversarial inputs (sorted / reverse-sorted) from
triggering the O(n^2) worst case that fixed-pivot quicksort suffers.
