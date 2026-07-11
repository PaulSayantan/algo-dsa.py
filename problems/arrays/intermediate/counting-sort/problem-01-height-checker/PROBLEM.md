# Height Checker

**Difficulty:** Easy

**Source:** LeetCode 1051 — Height Checker

## Description

A school is trying to take an annual photo of all its students. The students are asked to
stand in a single file line in **non-decreasing order by height**. Let `expected` be the
array obtained by sorting `heights` in non-decreasing order.

You are given an integer array `heights` representing the **current** order in which the
students are standing. Return the number of indices where `heights[i] != expected[i]` — i.e.
the number of students who are **not** standing in the correct position.

Because every height is a small positive integer, you can produce the sorted `expected`
array without a comparison sort: tally how many students have each height and read the
tallies back out in order.

## Constraints

- `1 <= heights.length <= 100`
- `1 <= heights[i] <= 100`

## Examples

### Example 1

```
Input:  heights = [1,1,4,2,1,3]
Output: 3
```

**Explanation:** The sorted (expected) order is `[1,1,1,2,3,4]`. Comparing position by
position, indices 2 (`4` vs `1`), 4 (`1` vs `3`), and 5 (`3` vs `4`) differ, so 3 students
are out of place.

### Example 2

```
Input:  heights = [5,1,2,3,4]
Output: 5
```

**Explanation:** The expected order is `[1,2,3,4,5]`. Every single position differs from the
current arrangement, so all 5 students must move.

### Example 3

```
Input:  heights = [1,2,3,4,5]
Output: 0
```

**Explanation:** The students are already sorted, so no one is out of place.

## Hint

The heights are bounded by 100, so you never need to compare elements. Use **Counting Sort**:
count how many students have each height in a small array, rebuild the sorted line by reading
those counts in order, then compare against the original.
