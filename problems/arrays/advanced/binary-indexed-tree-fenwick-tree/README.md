# Binary Indexed Tree (Fenwick Tree)

A **Binary Indexed Tree (BIT)**, also called a **Fenwick Tree**, is a compact array-based
data structure that maintains prefix aggregates (classically prefix sums) of a sequence
while supporting **both** point updates and prefix/range queries in **O(log n)** time.

It is the go-to structure when you have a mutable array and repeatedly need to answer
"what is the sum of a range?" mixed with "change one element." A prefix-sum array answers
range-sum in O(1) but costs O(n) per update; a plain array costs O(1) per update but O(n)
per range-sum. A Fenwick Tree balances both at O(log n).

## Core idea

Store the array 1-indexed. Each index `i` in the tree is responsible for a range of
`lowbit(i) = i & (-i)` original elements ending at `i`. To move to the parent when
updating, add `i & (-i)`; to walk down to disjoint responsible blocks when querying a
prefix, subtract `i & (-i)`. Both walks touch at most `log2(n)` indices.

```
update(i, delta):  while i <= n:  tree[i] += delta;  i += i & (-i)
prefix(i):         s = 0; while i > 0: s += tree[i]; i -= i & (-i); return s
rangeSum(l, r) = prefix(r) - prefix(l - 1)
```

## Complexity

| Operation                       | Time      | Space |
|---------------------------------|-----------|-------|
| Build (naive, n updates)        | O(n log n)| O(n)  |
| Build (linear)                  | O(n)      | O(n)  |
| Point update                    | O(log n)  | -     |
| Prefix / range query            | O(log n)  | -     |
| 2D point update / region query  | O(log n · log m) | O(n · m) |

## When to reach for a Fenwick Tree

- Point update + prefix/range **sum** (or any invertible group operation) on a mutable array.
- **Counting problems** solved by sweeping values and asking "how many seen so far are
  smaller/greater than x?" — usually paired with **coordinate compression**.
- Counting inversions and their variants (reverse pairs, insertion cost).
- 2D point-update / rectangle-sum queries via a Fenwick Tree of Fenwick Trees.
- Range-update + range-query using the classic **two-BIT** trick.

A Segment Tree is strictly more general (handles min/max, gcd, non-invertible merges, and
lazy range updates more naturally), but a Fenwick Tree wins on simplicity, constant factor,
and memory when the operation is an invertible aggregate like sum.

## Problems

| # | Problem | Difficulty | Summary |
|---|---------|------------|---------|
| 1 | [Range Sum Query - Mutable](problem-01-range-sum-query-mutable/PROBLEM.md) | Medium | Canonical point-update + range-sum; the "hello world" of Fenwick Trees. |
| 2 | [Count of Smaller Numbers After Self](problem-02-count-of-smaller-numbers-after-self/PROBLEM.md) | Hard | Sweep right-to-left, count smaller values with a BIT over compressed values. |
| 3 | [Create Sorted Array Through Instructions](problem-03-create-sorted-array-through-instructions/PROBLEM.md) | Hard | Insertion cost = min(#smaller, #larger) already present, tracked by a BIT. |
| 4 | [Reverse Pairs](problem-04-reverse-pairs/PROBLEM.md) | Hard | Count pairs with `nums[i] > 2*nums[j]` via a BIT over compressed values. |
| 5 | [Range Sum Query 2D - Mutable](problem-05-range-sum-query-2d-mutable/PROBLEM.md) | Hard | 2D Fenwick Tree for point update + rectangle-sum queries. |
| 6 | [Range Update Range Sum](problem-06-range-update-range-sum/PROBLEM.md) | Hard | Range-add + range-sum using the two-BIT (B1/B2) difference trick. |
