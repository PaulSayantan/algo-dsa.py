# Cyclic Sort

**Difficulty:** Easy

**Source:** Classic pattern (Grokking the Coding Interview — "Cyclic Sort")

## Description

You are given an array `nums` of length `n` that contains **every integer from `1`
to `n` exactly once**, but in some arbitrary order. Sort the array **in place** in
ascending order.

The catch that makes this problem interesting: because the values are exactly the
numbers `1..n`, you can sort without any comparison-based algorithm (no merge sort,
no quicksort) and without any extra array. Each value already "knows" where it
belongs — value `v` must end up at index `v - 1`.

Return the sorted array (sorting is performed in place, so mutating the input is
expected).

## Constraints

- `1 <= n <= 10^5`
- `nums` contains each integer in the range `[1, n]` exactly once.
- Solve it in **O(n)** time and **O(1)** extra space.

## Examples

### Example 1
```
Input:  nums = [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
```
**Explanation:** Every value is moved to index `value - 1`: 1 -> index 0, 2 -> index 1, and so on.

### Example 2
```
Input:  nums = [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]
```
**Explanation:** The array holds `1..6` shuffled; placing each value at index `value - 1` yields the sorted order.

### Example 3
```
Input:  nums = [1]
Output: [1]
```
**Explanation:** A single element is already in its correct slot.

## Hint

Use **Cyclic Sort**: for each position, swap the element into the index equal to
`value - 1` until the element that lands at the current position already belongs
there, then advance.
