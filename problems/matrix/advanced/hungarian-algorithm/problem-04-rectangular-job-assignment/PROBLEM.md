# Rectangular Job Assignment (More Jobs Than Workers)

**Difficulty:** Medium

**Source:** Classic unbalanced assignment problem (Operations Research; common competitive-programming variant of the Hungarian Algorithm).

## Description

A company has `n` workers and `m` jobs, with `n <= m`. Assigning **worker `i`**
to **job `j`** costs `cost[i][j]`. Each worker must be given **exactly one**
distinct job, and each job can be handled by **at most one** worker. Because
there may be more jobs than workers, some jobs may be left unassigned (that is
allowed and free — leftover jobs cost nothing).

Return the **minimum total cost** of assigning every worker to a distinct job.

## Constraints

- `1 <= n <= m <= 200`
- `cost.length == n`, `cost[i].length == m`
- `0 <= cost[i][j] <= 10^6`

## Examples

### Example 1

```
Input:  cost = [[9, 2, 7],
                [6, 4, 3]]
Output: 5
Explanation: There are 2 workers and 3 jobs. Assign worker 0 -> job 1 (cost 2)
and worker 1 -> job 2 (cost 3); job 0 is left unassigned. Total = 2 + 3 = 5.
No assignment of both workers to distinct jobs costs less.
```

### Example 2

```
Input:  cost = [[4, 1, 3],
                [2, 0, 5],
                [3, 2, 2]]
Output: 5
Explanation: A square case (3 workers, 3 jobs). Assign worker 0 -> job 1 (1),
worker 1 -> job 0 (2), worker 2 -> job 2 (2). Total = 1 + 2 + 2 = 5, which is
the minimum over all 6 assignments.
```

### Example 3

```
Input:  cost = [[8, 4, 7, 1],
                [5, 2, 3, 9]]
Output: 3
Explanation: 2 workers, 4 jobs. Assign worker 0 -> job 3 (cost 1) and worker 1
-> job 1 (cost 2); jobs 0 and 2 go unassigned. Total = 1 + 2 = 3, the minimum.
```

## Hint

The cost matrix is **rectangular** (`n <= m`). Make it square by padding with
`m - n` dummy worker rows whose costs are all `0` (a dummy worker "takes" a
leftover job for free), then run the standard **Hungarian Algorithm**.
Alternatively, use a Hungarian variant that natively handles `n <= m` rows and
columns without explicit padding.
