# Evaluate Division

**Difficulty:** Medium

**Source:** LeetCode 399

## Description

You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Aᵢ, Bᵢ]` and `values[i]` represent the equation `Aᵢ / Bᵢ = values[i]`. Each `Aᵢ` or `Bᵢ` is a string that represents a single variable.

You are also given some `queries`, where `queries[j] = [Cⱼ, Dⱼ]` represents the `j`-th query where you must find the answer for `Cⱼ / Dⱼ = ?`.

Return the answers to all queries. If a single answer **cannot be determined**, return `-1.0`.

**Note:** The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction. There may be variables in a query that do not appear in any equation — return `-1.0` for such queries.

## Constraints

- `1 <= equations.length <= 20`
- `equations[i].length == 2`
- `1 <= Aᵢ.length, Bᵢ.length <= 5`
- `values.length == equations.length`
- `0.0 < values[i] <= 20.0`
- `1 <= queries.length <= 20`
- `queries[i].length == 2`
- `1 <= Cⱼ.length, Dⱼ.length <= 5`
- `Aᵢ, Bᵢ, Cⱼ, Dⱼ` consist of lowercase English letters and digits.

## Examples

### Example 1

```
Input: equations = [["a","b"],["b","c"]], values = [2.0, 3.0],
       queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
```

**Explanation:** Given `a / b = 2.0` and `b / c = 3.0`:

- `a / c = (a / b) * (b / c) = 2.0 * 3.0 = 6.0`.
- `b / a = 1 / (a / b) = 1 / 2.0 = 0.5`.
- `a / e`: `e` never appears in any equation → `-1.0`.
- `a / a = 1.0` (a known variable divided by itself).
- `x / x`: `x` never appears → `-1.0` (an unknown variable, even divided by itself, is undetermined).

### Example 2

```
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5, 2.5, 5.0],
       queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000, 0.40000, 5.00000, 0.20000]
```

**Explanation:**

- `a / c = (a / b) * (b / c) = 1.5 * 2.5 = 3.75`.
- `c / b = 1 / (b / c) = 1 / 2.5 = 0.4`.
- `bc / cd = 5.0` (given directly).
- `cd / bc = 1 / 5.0 = 0.2`.

Note that `bc` and `cd` are distinct variables living in a separate connected component from `a`, `b`, `c`.

## Hint

Model variables as nodes and each equation `A / B = v` as edges `A → B` (weight `v`) and `B → A` (weight `1/v`). The ratio between any two variables is the **product** of edge weights along a connecting path. Run Floyd–Warshall with multiplication instead of addition to fill in every reachable ratio.
