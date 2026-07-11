# Binary Insertion Sort

**Difficulty:** Medium

*Source: Classic algorithms exercise — the "binary insertion sort" refinement of insertion sort.*

## Description

Sort an array of integers in ascending order using **binary insertion sort**.

Plain insertion sort finds each element's slot by scanning the sorted prefix from right to
left, doing up to `i` comparisons *and* `i` shifts for element `i`. Because the prefix is
already sorted, you can instead use **binary search** to locate the insertion index in
`O(log i)` comparisons, then shift the elements after it. This does not change the `O(n^2)`
worst-case time (you still move elements), but it drastically reduces the **number of
comparisons** — useful when comparisons are expensive (e.g. comparing long strings or calling
a costly comparator).

Implement the sort so that it remains **stable**: equal elements keep their original relative
order.

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- The sort must be stable.

## Examples

**Example 1**

```
Input:  nums = [5, 2, 4, 6, 1, 3]
Output: [1, 2, 3, 4, 5, 6]
```
Explanation: For each element, binary search finds where it belongs in the sorted prefix; e.g.
inserting `1` into `[2,4,5,6]` finds index 0, then the four larger values shift right.

**Example 2**

```
Input:  nums = [10, 10, 9]
Output: [9, 10, 10]
```
Explanation: The two `10`s must stay in their original order. Binary search returns the
**rightmost** insertion point for a value equal to `10`, so the second `10` is placed after
the first — keeping the sort stable.

**Example 3**

```
Input:  nums = [1, 2, 3, 4]
Output: [1, 2, 3, 4]
```
Explanation: Already sorted — each binary search returns the current end, so nothing shifts.

## Hint

Use **Insertion Sort**, but replace the linear right-to-left scan with a **binary search** over
the sorted prefix to find the insertion index. To stay stable, search for the *upper bound*
(the first position whose value is strictly greater than the key), then shift and insert.
