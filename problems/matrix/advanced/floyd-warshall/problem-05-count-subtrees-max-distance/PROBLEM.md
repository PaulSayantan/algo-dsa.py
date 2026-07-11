# Count Subtrees With Max Distance Between Cities

**Difficulty:** Hard

**Source:** LeetCode 1617

## Description

There are `n` cities numbered from `1` to `n`. You are given `edges` of size `n - 1`, where `edges[i] = [uᵢ, vᵢ]` represents a bidirectional edge between cities `uᵢ` and `vᵢ`. There exists a unique path between each pair of cities — in other words, the cities form a **tree**.

A **subtree** is a subset `T` of cities such that every two cities in the subset are reachable from each other **using edges that connect only cities within `T`** (that is, the induced subgraph on `T` must be connected). Note that a subtree must contain at least two cities.

For each `d` from `1` to `n - 1`, define the *distance* of a subtree as the **maximum** distance (number of edges on the unique tree path) between any two of its cities. 

Return an array of size `n - 1` where the `d`-th element (1-indexed) is the **number of subtrees** whose maximum inter-city distance is exactly equal to `d`.

## Constraints

- `2 <= n <= 15`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `1 <= uᵢ, vᵢ <= n`
- All pairs `(uᵢ, vᵢ)` are distinct.
- The given edges form a valid tree.

## Examples

### Example 1

```
Input: n = 4, edges = [[1,2],[2,3],[2,4]]
Output: [3, 4, 0]
```

**Explanation:** The tree is a "star" centered at city 2 (2 is connected to 1, 3, and 4).

- Subtrees with max distance **1** (a single edge, 2 cities each): `{1,2}`, `{2,3}`, `{2,4}` → **3**.
- Subtrees with max distance **2**: `{1,2,3}`, `{1,2,4}`, `{2,3,4}`, `{1,2,3,4}` → **4**.
- Subtrees with max distance **3**: none (the tree's diameter is only 2) → **0**.

So the answer is `[3, 4, 0]`.

### Example 2

```
Input: n = 2, edges = [[1,2]]
Output: [1]
```

**Explanation:** There is exactly one subtree, `{1, 2}`, with a maximum distance of `1`. The result has size `n - 1 = 1`.

### Example 3

```
Input: n = 3, edges = [[1,2],[2,3]]
Output: [2, 1]
```

**Explanation:** The tree is a path `1 - 2 - 3`.

- Max distance 1: `{1,2}` and `{2,3}` → **2**.
- Max distance 2: `{1,2,3}` (the whole path, distance between 1 and 3 is 2) → **1**.

So the answer is `[2, 1]`.

## Hint

With `n <= 15` you can enumerate all `2^n` subsets of cities. For each subset, check whether the induced subgraph is connected and, if so, find its diameter — the maximum pairwise distance. Precompute every pairwise tree distance once with Floyd–Warshall so each subset's diameter is a fast lookup.

## Bonus

`n <= 15` also invites a tree-DP over edges/pairs approach, but the Floyd–Warshall + subset-enumeration solution is the most direct.
