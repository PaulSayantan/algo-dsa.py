# Maximum Subarray With Indices

**Difficulty:** Medium

**Source:** CLRS 4.1 — `FIND-MAXIMUM-SUBARRAY` (classic textbook formulation)

## Description

Given an integer array `nums`, find the contiguous non-empty subarray with the
largest sum and return a triple `(start, end, total)` where:

- `start` is the (0-based, inclusive) index of the first element of the best
  subarray,
- `end` is the (0-based, inclusive) index of the last element, and
- `total` is the sum `nums[start] + ... + nums[end]`.

This is the CLRS version of the maximum-subarray problem, which returns the
actual boundaries rather than just the sum. If several subarrays tie for the best
sum, return any one of them — but be consistent so your output is reproducible
(the reference returns the one the recursion finds first, favoring the left half,
then the crossing, then the right).

The intended method is **divide & conquer**: the divide step recurses on each
half; the combine step must not only compute the best crossing *sum* but also
remember *where* that crossing subarray begins and ends.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- Indices are 0-based and inclusive.

## Examples

### Example 1

```
Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: (3, 6, 6)
Explanation: nums[3..6] = [4, -1, 2, 1] sums to 6, which is the maximum. It starts
             at index 3 and ends at index 6.
```

### Example 2

```
Input:  nums = [2, -1, 2]
Output: (0, 2, 3)
Explanation: The whole array [2, -1, 2] sums to 3. Dropping either end lowers the
             sum, so the best subarray spans indices 0 through 2.
```

### Example 3

```
Input:  nums = [-5, -2, -3]
Output: (1, 1, -2)
Explanation: All elements are negative, so the best subarray is the single largest
             element -2 at index 1: start = end = 1, total = -2.
```

## Constraints on ties

- When the left-only, right-only, and crossing candidates tie in sum, prefer the
  left-only candidate, then the crossing, then the right-only. This keeps the
  returned indices deterministic.

## Hint

Use **Maximum Subarray via Divide & Conquer**. Have your crossing helper return a
`(left_index, right_index, sum)` triple: scan left from `mid` remembering the
index that achieved the best suffix sum, scan right from `mid+1` remembering the
index for the best prefix sum, then join them.
