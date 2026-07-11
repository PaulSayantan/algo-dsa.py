# Classic Assignment Problem

**Difficulty:** Easy

**Source:** Classic Operations Research / CLRS-style assignment problem (the canonical use case of the Hungarian Algorithm).

## Description

You are given an `n x n` integer matrix `cost`, where `cost[i][j]` is the cost of
assigning **worker `i`** to **job `j`**. Each worker must be assigned to exactly
one job, and each job must be handled by exactly one worker (a one-to-one
assignment, i.e. a perfect matching).

Return the **minimum possible total cost** over all valid assignments.

A valid assignment picks exactly one entry from every row and every column such
that no two picked entries share a row or a column, and its cost is the sum of
the picked entries.

## Constraints

- `1 <= n <= 200`
- `cost.length == cost[i].length == n`
- `0 <= cost[i][j] <= 10^6`

## Examples

### Example 1

```
Input:  cost = [[3, 1, 2],
                [2, 3, 1],
                [1, 2, 3]]
Output: 3
Explanation: Assign worker 0 -> job 1 (cost 1), worker 1 -> job 2 (cost 1),
worker 2 -> job 0 (cost 1). Total = 1 + 1 + 1 = 3, which is the minimum over
all 3! = 6 possible assignments.
```

### Example 2

```
Input:  cost = [[4, 1],
                [2, 3]]
Output: 3
Explanation: Assign worker 0 -> job 1 (cost 1) and worker 1 -> job 0 (cost 2).
Total = 3. The other assignment (0->0, 1->1) costs 4 + 3 = 7, so 3 is optimal.
```

### Example 3

```
Input:  cost = [[9, 11, 14],
                [6, 15, 13],
                [12, 13, 6]]
Output: 23
Explanation: Assign worker 0 -> job 1 (11), worker 1 -> job 0 (6),
worker 2 -> job 2 (6). Total = 11 + 6 + 6 = 23, the minimum-cost assignment.
```

## Hint

Trying all `n!` permutations is exponential. Use the **Hungarian Algorithm**
(Kuhn–Munkres) to solve the assignment problem in `O(n^3)` by working with
reduced costs (row/column potentials) and augmenting paths.
