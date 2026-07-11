# Merge Sort Tree

A **Merge Sort Tree** is a segment tree in which every node stores the **sorted list
of the elements** in the subarray it covers (not just an aggregate like a sum or a
min). The name comes from the fact that the sorted list of a parent node is exactly
the *merge* of the sorted lists of its two children — the same merge step used in
merge sort. Because the merges at each level touch every element once, the whole tree
occupies `O(n log n)` space and takes `O(n log n)` time to build.

## What it is good for

The Merge Sort Tree shines on **static arrays** (no element updates) that must answer
many **"order-statistic over a range"** queries, such as:

- Count how many elements in `a[l..r]` are `<= x` (or `< x`, `> x`, or inside `[a, b]`).
- Sum of the elements in `a[l..r]` that are `<= x` (with an extra prefix-sum array per node).
- The k-th smallest value in `a[l..r]`.
- Any query that decomposes a range into `O(log n)` canonical nodes and then answers a
  *sorted-order* sub-question (usually via binary search) inside each node.

To answer a range query, the tree decomposes `[l, r]` into `O(log n)` canonical nodes and
runs a **binary search** inside each node's sorted list. That gives `O(log^2 n)` per query
(one `log n` for the node decomposition, one for the binary search inside each node).

## When to reach for it

Reach for a Merge Sort Tree when:

- The array is **static** (values do not change between queries — the sorted lists are
  built once and never mutated). If you need point updates, prefer a BIT of sorted
  structures, a wavelet tree, or offline techniques.
- Queries are **online** and each asks something about the *distribution* of values in a
  subrange (rank / count / k-th).
- You want something simpler to code than a persistent segment tree or a wavelet tree
  and can afford the extra `log` factor.

## Complexity

| Operation            | Time          | Space        |
|----------------------|---------------|--------------|
| Build                | `O(n log n)`  | `O(n log n)` |
| Count `<= x` in range| `O(log^2 n)`  | —            |
| Sum `<= x` in range  | `O(log^2 n)`  | —            |
| k-th smallest in range | `O(log^3 n)` (binary search on value + count query) | — |

(With fractional cascading the count query drops to `O(log n)`, but the plain
`O(log^2 n)` version below is what is almost always coded in practice.)

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Range Count of Elements ≤ X](problem-01-range-count-less-equal/PROBLEM.md) | Count values `<= x` in a subarray — the canonical Merge Sort Tree query | Medium |
| 2 | [K-Query (Count Greater Than K)](problem-02-kquery-greater-than/PROBLEM.md) | SPOJ KQUERY: count values strictly greater than `k` in a subarray | Medium |
| 3 | [Count of Smaller Numbers After Self](problem-03-count-smaller-after-self/PROBLEM.md) | LeetCode 315: for each index count later elements that are smaller | Medium |
| 4 | [Range Sum of Elements ≤ K](problem-04-range-sum-at-most-k/PROBLEM.md) | Augmented tree (sorted list + prefix sums): sum of values `<= k` in a subarray | Hard |
| 5 | [K-th Smallest Number in Range](problem-05-kth-smallest-in-range/PROBLEM.md) | Online k-th order statistic over any subarray | Hard |
