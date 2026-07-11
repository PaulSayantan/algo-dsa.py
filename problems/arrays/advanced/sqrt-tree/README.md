# Sqrt Tree

The **Sqrt Tree** is a static data structure that answers **associative** range queries
(`sum`, `min`, `gcd`, product mod *m*, matrix / affine composition, ...) in **O(1)** time
after an **O(n log log n)** preprocessing, using **O(n log log n)** space.

## The one-sentence pitch

> Sparse Table gives O(1) queries too — but *only* for **idempotent** operations
> (`min`, `max`, `gcd`, `and`, `or`), because it overlaps two ranges. Prefix sums give
> O(1) queries too — but *only* for **invertible** operations (`sum`, `xor`).
> **Sqrt Tree gives O(1) queries for *any associative* operation**, including those that
> are neither idempotent nor invertible (product mod *m*, affine map composition,
> min-plus matrix products, ...). That is its reason to exist.

## Intuition (why "sqrt")

Split the array of size `n` into `√n` blocks of size `√n`.

- Precompute, for **each block**, the **prefix** and **suffix** answers inside that block.
- Precompute, for **every pair of whole blocks** `(i, j)`, the answer over blocks `i..j`
  (the `between` table). There are `√n · √n = n` such pairs.

Any query `[l, r]` then decomposes into at most three precomputed pieces:

1. the **suffix** of `l`'s block (from `l` to the block end),
2. the **between**-blocks answer for the whole blocks strictly inside,
3. the **prefix** of `r`'s block (from the block start to `r`),

combined with two `op` calls — hence **O(1)**. To handle queries that stay *within* one
block (where the three-piece trick collapses), the structure is applied **recursively**
to each block. The recursion depth is `O(log log n)` because the block count square-roots
each level (`n → √n → n^{1/4} → ...`), which is where the `O(n log log n)` build and space
come from.

## When to reach for it

- You need **O(1)** range queries on a **static** array (build once, then only queries),
  **and**
- the operation is **associative but not idempotent and not invertible**, so neither a
  sparse table nor prefix sums apply. Classic cases: **product modulo m**, **composition
  of linear/affine functions**, **matrix products**.
- If your op is idempotent (min/max/gcd) a Sparse Table is simpler; if it is invertible
  (sum/xor) prefix arrays are simpler. Sqrt Tree still works for those and is the *only*
  simple O(1) option that covers *all three* categories at once.

There is also an **updatable** variant supporting O(√n) point updates (still O(1) query),
which competes with segment trees when queries vastly outnumber updates.

## Complexity summary

| Operation                      | Complexity        |
|--------------------------------|-------------------|
| Build                          | O(n log log n)    |
| Query (range)                  | **O(1)**          |
| Space                          | O(n log log n)    |
| Point update (updatable form)  | O(√n)             |

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Static Range Sum Query](problem-01-static-range-sum/PROBLEM.md) | Warm-up: O(1) range sum, invertible op | Easy |
| 2 | [Range Minimum Query](problem-02-range-minimum-query/PROBLEM.md) | Idempotent op (min); contrast with sparse table | Easy |
| 3 | [Range GCD Query](problem-03-range-gcd-query/PROBLEM.md) | GCD over subarrays | Medium |
| 4 | [Range Product Modulo m](problem-04-range-product-modulo/PROBLEM.md) | **Non-invertible** op — where Sqrt Tree truly shines | Hard |
| 5 | [Range Affine Composition](problem-05-range-affine-composition/PROBLEM.md) | **Non-commutative, non-invertible** function composition | Hard |

Problems 1–3 build fluency; **problems 4 and 5 are the true motivating use cases** where
prefix sums and sparse tables both fail and Sqrt Tree is the idiomatic choice.
