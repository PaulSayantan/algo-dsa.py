# Distinct Elements in Range (Online)

**Difficulty:** Hard

Source: SPOJ **DQUERY** ("D-query"). A classic that can be solved offline with a
BIT, but has an elegant *online* persistent-segment-tree solution.

## Description

You are given an integer array `nums` of length `n` and `q` queries. Each query
is a pair `(l, r)` and asks:

> How many **distinct** values appear in the subarray `nums[l..r]` (inclusive)?

Return the answer to each query in order. Queries must be answerable **online**
(each in `O(log n)`), without reordering them.

The persistent trick: process indices left to right, maintaining a 0/1 segment
tree over **positions** where position `j` is marked `1` iff `j` is the *last
occurrence so far* of the value `nums[j]`. Version `r` of this tree, summed over
positions `[l, r]`, counts exactly the distinct values in `nums[l..r]`.

## Constraints

- `1 ≤ n ≤ 3 × 10^5`
- `1 ≤ nums[i] ≤ 10^6`
- `1 ≤ q ≤ 2 × 10^5`
- `0 ≤ l ≤ r < n`

## Examples

### Example 1

```
Input:
  nums = [1, 1, 2, 1, 3]
  queries = [
    (0, 4),        # whole array [1,1,2,1,3]; distinct = {1,2,3}
    (0, 2),        # [1,1,2];               distinct = {1,2}
    (1, 3),        # [1,2,1];               distinct = {1,2}
  ]

Output: [3, 2, 2]
```

Explanation: The full array uses three distinct values `{1, 2, 3}`. `nums[0..2] =
[1,1,2]` has `{1, 2}`. `nums[1..3] = [1,2,1]` also has `{1, 2}` — the repeated
`1` is counted only once.

### Example 2

```
Input:
  nums = [1, 2, 3, 4, 5]
  queries = [
    (0, 4),        # all distinct
    (2, 4),        # [3,4,5]
    (1, 1),        # single element [2]
  ]

Output: [5, 3, 1]
```

Explanation: With all values distinct, the count equals the window length:
`[0,4]` → 5, `[2,4]` → 3, and the single-element window `[1,1]` → 1.

## Hint

Build a **Persistent Segment Tree** over positions, one version per prefix. When
you process index `i` with value `v`: if `v` last appeared at position `p`,
create the next version by setting position `p` to `0` **and** position `i` to
`1` (two point updates chained). Then the answer to `(l, r)` is the range-sum
over positions `[l, r]` in version `r`.
