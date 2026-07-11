# EquiLeader

**Difficulty:** Medium

**Source:** Codility Lesson 8 (Leader) — EquiLeader

## Description

A non-empty array `A` of `N` integers is given. The **leader** of an array is the value that
occurs in **more than half** of its elements (a strict majority). Note an array has at most
one leader.

An index `S` (where `0 <= S < N - 1`) is an **equi leader** if the two disjoint sub-arrays
`A[0], A[1], ..., A[S]` and `A[S + 1], A[S + 2], ..., A[N - 1]` have **the same leader** (both
non-empty, both with an actual leader, and the two leaders are equal).

Return the **number of equi leaders** in `A`.

Aim for **O(N)** time and **O(1)** extra space (beyond the input).

## Constraints

- `1 <= N <= 100000`
- Each element of `A` is an integer within the range `[-1,000,000,000, 1,000,000,000]`.

## Examples

### Example 1

```
Input:  A = [4, 3, 4, 4, 4, 2]
Output: 2
```

Explanation: The whole array's leader is `4` (it appears 4 times out of 6). Split point
`S = 0` gives left `[4]` (leader 4) and right `[3,4,4,4,2]` (4 appears 3 of 5, a majority) —
equi leader. Split point `S = 2` gives left `[4,3,4]` (4 appears 2 of 3) and right `[4,4,2]`
(4 appears 2 of 3) — equi leader. No other split qualifies, so the answer is `2`.

### Example 2

```
Input:  A = [1, 1, 1, 1]
Output: 3
```

Explanation: `1` is the leader of every prefix and suffix. All three split points
`S = 0, 1, 2` produce two halves both led by `1`, so all `3` are equi leaders.

### Example 3

```
Input:  A = [1, 2, 3]
Output: 0
```

Explanation: The whole array has no leader (each value appears once), and no split point
yields two halves sharing a common leader, so the answer is `0`.

## Hint

An equi leader's shared value must be a strict majority of **both** halves, which forces it to
be the leader of the **whole** array. Find that global leader with **Boyer–Moore Voting**
(and verify it), then sweep split points comparing the leader's prefix count against the
majority threshold of each half.
