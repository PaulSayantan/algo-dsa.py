# Minimum-Cost Cyclic Schedule of Exactly L Operations

**Difficulty:** Hard

**Source:** Competitive-programming pattern ("minimum-cost closed walk of fixed
length" / cyclic scheduling). This variant disguises a min-plus matrix power
inside an innocent-looking DP.

## Description

A machine operates in one of `c` **modes** labeled `0 .. c-1`. Reconfiguring the
machine from mode `i` to mode `j` costs `cost[i][j]` (a non-negative integer, or
`INF` if that reconfiguration is impossible). Every operation forces a genuine
mode change: you may **not** stay in the same mode from one operation to the next
(so `cost[i][i] = INF`).

You must run a **maintenance cycle** consisting of **exactly `L` operations**
that begins in some mode and, after all `L` reconfigurations, returns to that
same starting mode. You may pick the starting mode freely, and modes may repeat
during the cycle. Return the **minimum total reconfiguration cost** of such a
cycle, or `-1` if no valid cycle of exactly `L` operations exists.

At first glance this is a DP over `(operation index, current mode)`. But the
transition "extend the schedule by one operation" is exactly a **min-plus
(tropical) matrix product** of the cost matrix. The minimum-cost closed cycle of
length `L` is therefore

```
answer = min over i of ( C^{⊙L} )[i][i]
```

where `C` is the cost matrix and `C^{⊙L}` is its `L`-th tropical power. Since `L`
can be huge, use fast exponentiation.

## Constraints

- `2 <= c <= 200`
- `1 <= L <= 10^18`
- `cost[i][j]` is a non-negative integer with `0 <= cost[i][j] <= 10^6`, or `INF`
  when reconfiguration `i → j` is impossible.
- `cost[i][i] = INF` for all `i` (no-op operations are not allowed).
- A finite answer, if one exists, fits in a 64-bit signed integer.

## Examples

### Example 1

```
Input:
  c = 3
  cost = [[INF,   4,   1],
          [  2, INF,   3],
          [  5,   1, INF]]
  L = 2
Output: 4
Explanation:
  A 2-operation cycle returns to its start after two reconfigurations.
  The cheapest is  1 -> 2 -> 1  with cost cost[1][2] + cost[2][1] = 3 + 1 = 4.
  (Cycle 0 -> 1 -> 0 costs 4 + 2 = 6; 0 -> 2 -> 0 costs 1 + 5 = 6.)
```

### Example 2

```
Input:
  c = 3
  cost = same 3x3 matrix as Example 1
  L = 3
Output: 4
Explanation:
  The cheapest 3-operation cycle is  0 -> 2 -> 1 -> 0
  with cost cost[0][2] + cost[2][1] + cost[1][0] = 1 + 1 + 2 = 4.
```

### Example 3

```
Input:
  c = 3
  cost = same 3x3 matrix as Example 1
  L = 6
Output: 8
Explanation:
  The best long-run cycle repeats the length-3 cycle 0 -> 2 -> 1 -> 0 twice:
  0 -> 2 -> 1 -> 0 -> 2 -> 1 -> 0  with cost (1 + 1 + 2) * 2 = 8. With L up to
  10^18 you cannot chain L products, so exponentiate the matrix instead.
```

## Hint

Write the DP for "cheapest schedule of `e` operations ending in each mode" and
look at the transition: it is `min_t ( dp[e-1][t] + cost[t][j] )` — a
**Min-Plus (Tropical) Matrix Multiplication** of the cost matrix. A *cyclic*
schedule of length `L` is a closed walk, so the answer lives on the **diagonal**
of `C^{⊙L}`; with `L` huge, get that power by fast exponentiation.
