# Insertion Sort Shift Count (Inversions)

**Difficulty:** Hard

*Source: Classic "count inversions" problem, framed through insertion sort (CLRS Problem 2-4 / competitive programming staple).*

## Description

When insertion sort processes an array, its inner loop shifts elements to the right to make
room for each key. Your task: return the **total number of shifts** insertion sort performs to
sort `nums` into ascending order.

A shift is a single "move one element one slot to the right" operation inside the inner
`while` loop (the assignment `nums[j+1] = nums[j]`). Placing the key into its final gap does
**not** count as a shift.

This count is a famous quantity: it equals the number of **inversions** in the array — pairs of
indices `(i, j)` with `i < j` but `nums[i] > nums[j]`. It measures "how far from sorted" the
array is. A sorted array has 0 inversions; a reverse-sorted array of length `n` has the maximum
`n*(n-1)/2`.

You may return the count using the direct insertion-sort simulation. (For very large inputs
the same quantity can be computed in `O(n log n)` with a merge-sort based counter — see the
solution — but the insertion-sort view is what connects shifts to inversions.)

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- The answer can be as large as `n*(n-1)/2` (up to ~5*10^7 here), which fits in a 64-bit
  integer (and Python ints are unbounded).

## Examples

**Example 1**

```
Input:  nums = [2, 4, 1, 3, 5]
Output: 3
```
Explanation: The inversions are `(2,1)`, `(4,1)`, and `(4,3)` — three pairs out of order.
Insertion sort shifts exactly 3 times: inserting `1` shifts `4` and `2` (2 shifts), inserting
`3` shifts `4` (1 shift). Total = 3.

**Example 2**

```
Input:  nums = [3, 2, 1]
Output: 3
```
Explanation: Every pair is inverted: `(3,2)`, `(3,1)`, `(2,1)`. Reverse-sorted length 3 gives
`3*2/2 = 3` shifts.

**Example 3**

```
Input:  nums = [1, 2, 3, 4]
Output: 0
```
Explanation: Already sorted — the inner loop never shifts anything, so the count is 0.

## Hint

Use **Insertion Sort** and simply count each `nums[j+1] = nums[j]` shift the inner loop
performs. That running total equals the number of inversions in the array.
