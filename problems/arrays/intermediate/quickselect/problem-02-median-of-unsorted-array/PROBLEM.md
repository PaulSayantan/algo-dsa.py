# Median of an Unsorted Array

**Difficulty:** Medium

**Source:** Classic interview problem (CLRS "Selection in expected linear time", §9.2)

## Description

Given an array `nums` of `n` numbers, return its **median**.

The median is the value separating the higher half from the lower half of the data:

- If `n` is **odd**, the median is the single middle element of the sorted array
  (the element at 0-indexed position `n // 2`).
- If `n` is **even**, the median is the **average of the two middle elements** — the
  elements at 0-indexed positions `n // 2 - 1` and `n // 2` of the sorted array.

Solve it in **expected linear time**, i.e. faster than sorting.

## Constraints

- `1 <= n <= 10^5`
- `-10^6 <= nums[i] <= 10^6`
- The answer for an even-length array may be a non-integer (e.g. `2.5`); return a float
  in that case.

## Examples

### Example 1

```
Input:  nums = [3, 1, 2]
Output: 2
```

**Explanation:** Sorted -> `[1, 2, 3]`. Odd length (n = 3), so the median is the middle
element at index `3 // 2 = 1`, which is `2`.

### Example 2

```
Input:  nums = [4, 1, 3, 2]
Output: 2.5
```

**Explanation:** Sorted -> `[1, 2, 3, 4]`. Even length (n = 4), so the median is the
average of the elements at indices `1` and `2`: `(2 + 3) / 2 = 2.5`.

### Example 3

```
Input:  nums = [7]
Output: 7
```

**Explanation:** A single element is its own median.

## Hint

The median is nothing more than the element(s) at the middle sorted index/indices. Use
**Quickselect** to fetch the element at index `n // 2` in expected `O(n)`. For even `n`,
you additionally need the element at index `n // 2 - 1`.
