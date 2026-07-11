# Staircase / Saddleback Search

## What it is

**Staircase Search** (also called **Saddleback Search**) is a linear-time search
technique for a matrix that is sorted along **both** dimensions — each row is
sorted left-to-right and each column is sorted top-to-bottom. Such a matrix is
sometimes called a **Young tableau**.

The trick is to start at a corner where the two sort directions *disagree* — the
**top-right** corner (or, symmetrically, the **bottom-left** corner). From there,
every element you look at lets you eliminate an entire row **or** an entire
column in one comparison:

Starting at the top-right cell `M[r][c]` (with `r = 0`, `c = n-1`), to find `target`:

- If `M[r][c] == target` → found it.
- If `M[r][c] >  target` → everything **below** in this column is even larger, so
  the target cannot be in column `c`. Discard the column: `c -= 1` (move left).
- If `M[r][c] <  target` → everything **to the left** in this row is even smaller,
  so the target cannot be in row `r`. Discard the row: `r += 1` (move down).

Each step throws away one row or one column, so the walk visits at most
`m + n` cells — hence the "staircase": the path descends and steps left like a
flight of stairs.

## When to reach for it

- You are given a matrix sorted **row-wise and column-wise** and asked to
  **search**, **count**, or find a **boundary** (e.g. how many values are `< x`,
  the row with the most 1s, how many negatives).
- You want `O(m + n)` instead of the `O(m·n)` brute-force scan, but the matrix is
  **not** fully flattened-sorted (so a single `O(log(m·n))` binary search does
  not directly apply).
- As a **subroutine** inside *binary-search-on-the-answer*: to answer "how many
  matrix entries are `≤ x`?" in `O(m + n)`, which powers order-statistic problems
  like "kth smallest element".

## Complexity

| | Cost |
|---|---|
| Time | `O(m + n)` for one staircase walk (`m` rows, `n` columns) |
| Space | `O(1)` — only two index variables |

For the binary-search-on-value problems (4 and 5 below), the total time is
`O((m + n) · log(range))`, where the staircase count is the inner loop.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Search a 2D Matrix II](problem-01-search-a-2d-matrix-ii/PROBLEM.md) | Target search from the top-right corner | Medium |
| 2 | [Count Negative Numbers in a Sorted Matrix](problem-02-count-negative-numbers/PROBLEM.md) | Counting a region with a staircase walk | Easy |
| 3 | [Row with Maximum Number of 1s](problem-03-row-with-max-ones/PROBLEM.md) | Finding an argmax boundary in one pass | Easy/Medium |
| 4 | [Kth Smallest Element in a Sorted Matrix](problem-04-kth-smallest-in-sorted-matrix/PROBLEM.md) | Staircase count inside binary-search-on-value | Medium |
| 5 | [Kth Smallest Number in a Multiplication Table](problem-05-kth-smallest-multiplication-table/PROBLEM.md) | Saddleback count over an *implicit* matrix | Hard |

Work them top to bottom: problems 1–3 teach the raw staircase walk, and
problems 4–5 layer it inside binary search on the answer.
