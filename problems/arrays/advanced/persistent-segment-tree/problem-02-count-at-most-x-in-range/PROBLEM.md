# Count Elements ≤ X in a Subarray

**Difficulty:** Medium

Source: Classic range-frequency query (a staple "persistent segment tree over
prefixes" exercise; closely related to LeetCode 2080 "Range Frequency Queries"
and to offline range-rank problems).

## Description

You are given an integer array `nums` of length `n`. You must answer `q`
**offline or online** queries. Each query is a triple `(l, r, x)` and asks:

> How many indices `i` with `l ≤ i ≤ r` satisfy `nums[i] ≤ x`?

Return a list of answers, one per query, in the order the queries are given.

The intended solution builds, for every prefix of the array, a segment tree over
the **value domain** that counts how many times each value has appeared so far.
Version `i` is the tree after inserting `nums[0..i]`. The count of values `≤ x`
in `nums[l..r]` is then

```
countLE(version[r], x)  −  countLE(version[l−1], x)
```

where `version[-1]` is the empty tree. This "subtract two prefix versions" trick
is the heart of persistent-segment-tree range queries.

## Constraints

- `1 ≤ n ≤ 10^5`
- `-10^9 ≤ nums[i] ≤ 10^9`
- `1 ≤ q ≤ 10^5`
- `0 ≤ l ≤ r < n`
- `-10^9 ≤ x ≤ 10^9`

## Examples

### Example 1

```
Input:
  nums = [1, 3, 2, 4, 2]
  queries = [
    (0, 4, 2),     # how many of [1,3,2,4,2] are <= 2 ?
    (1, 3, 3),     # how many of [3,2,4]     are <= 3 ?
    (0, 4, 0),     # how many of the whole array are <= 0 ?
  ]

Output: [3, 2, 0]
```

Explanation:
- `[1,3,2,4,2] ≤ 2` → the values `1, 2, 2` qualify → `3`.
- `nums[1..3] = [3,2,4] ≤ 3` → `3, 2` qualify → `2`.
- Nothing is `≤ 0` → `0`.

### Example 2

```
Input:
  nums = [5, 5, 5, 5]
  queries = [
    (0, 3, 5),     # all four are <= 5
    (0, 3, 4),     # none are <= 4
    (2, 2, 5),     # single element nums[2]=5 <= 5
  ]

Output: [4, 0, 1]
```

Explanation: every element equals `5`. With `x = 5` all four in `[0,3]` count;
with `x = 4` none count; the single-index query `[2,2]` has exactly one element,
which is `≤ 5`.

## Hint

Build one **Persistent Segment Tree** version per prefix over the (coordinate-
compressed) value domain. Each version inserts one more element. The answer for
`(l, r, x)` is `countLE(root[r], x) − countLE(root[l−1], x)`, computed by walking
both roots down to the value `x`.
