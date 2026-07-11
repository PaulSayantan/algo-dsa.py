# Cheapest Flights Within K Stops

**Difficulty:** Medium

**Source:** LeetCode 787 — "Cheapest Flights Within K Stops."

## Description

There are `n` cities connected by some number of flights. You are given an array
`flights` where `flights[i] = [from_i, to_i, price_i]` indicates a flight from
city `from_i` to city `to_i` with cost `price_i`.

You are also given three integers `src`, `dst`, and `k`. Return the **cheapest
price** from `src` to `dst` such that the route uses **at most `k` stops**. If
there is no such route, return `-1`.

"At most `k` stops" means the route may use at most `k + 1` flights (edges): with
`k` intermediate stops you traverse `k + 1` legs.

The tropical framing: build the flight-cost matrix `M` but place a `0` on the
diagonal (a free "stay put" self-loop). A single min-plus product `M ⊙ M`
now yields the cheapest route using **at most 2** flights (a real flight, or a
free stay followed by a flight, etc.). Raising `M` to the `(k+1)`-th tropical
power gives the cheapest route using **at most `k + 1`** flights — exactly the
"at most `k` stops" answer.

## Constraints

- `1 <= n <= 100`
- `0 <= flights.length <= n * (n - 1)`
- `flights[i].length == 3`
- `0 <= from_i, to_i < n`
- `from_i != to_i`
- `1 <= price_i <= 10^4`
- There will not be any multiple flights between two cities.
- `0 <= src, dst, k < n`
- `src != dst`

## Examples

### Example 1

```
Input:
  n = 4
  flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
  src = 0, dst = 3, k = 1
Output: 700
Explanation:
  With at most 1 stop (so at most 2 flights), the cheapest route is
    0 -> 1 -> 3  with cost 100 + 600 = 700.
  The route 0 -> 1 -> 2 -> 3 (cost 400) uses 2 stops / 3 flights, which is not
  allowed, so 700 is the answer.
```

### Example 2

```
Input:
  n = 3
  flights = [[0,1,100],[1,2,100],[0,2,500]]
  src = 0, dst = 2, k = 1
Output: 200
Explanation:
  With at most 1 stop the route 0 -> 1 -> 2 costs 100 + 100 = 200, which beats
  the direct flight 0 -> 2 costing 500.
```

### Example 3

```
Input:
  n = 3
  flights = [[0,1,100],[1,2,100],[0,2,500]]
  src = 0, dst = 2, k = 0
Output: 500
Explanation:
  With 0 stops only the direct flight 0 -> 2 (cost 500) is allowed; the two-leg
  route is forbidden, so the answer is 500.
```

## Hint

"At most `k` stops" is "at most `k + 1` edges." Turn "at most" into "exactly"
by adding a free self-loop (`0` on the diagonal) and then apply **Min-Plus
(Tropical) Matrix Multiplication**: the answer is entry `(src, dst)` of the
`(k+1)`-th tropical power of the cost matrix.
