# Find the City With the Smallest Number of Neighbors at a Threshold Distance

**Difficulty:** Medium

**Source:** LeetCode 1334

## Description

There are `n` cities numbered from `0` to `n - 1`. You are given an array `edges` where `edges[i] = [fromᵢ, toᵢ, weightᵢ]` represents a bidirectional and weighted edge between cities `fromᵢ` and `toᵢ`, and given an integer `distanceThreshold`.

Return the city with the **smallest number of cities** that are reachable through some path whose total edge weight is at most `distanceThreshold`. If there are multiple such cities, return the city with the **greatest number** (the largest index).

Note that the distance of a path connecting cities `i` and `j` is equal to the sum of the edge weights along that path.

## Constraints

- `2 <= n <= 100`
- `1 <= edges.length <= n * (n - 1) / 2`
- `edges[i].length == 3`
- `0 <= fromᵢ < toᵢ < n`
- `1 <= weightᵢ, distanceThreshold <= 10^4`
- All pairs `(fromᵢ, toᵢ)` are distinct.

## Examples

### Example 1

```
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
```

**Explanation:** With threshold 4, the neighbors reachable from each city are:

- City 0 → {1 (3), 2 (4)} = 2 cities
- City 1 → {0 (3), 2 (1), 3 (4)} = 3 cities
- City 2 → {0 (4), 1 (1), 3 (1)} = 3 cities
- City 3 → {1 (4), 2 (1)} = 2 cities

Cities 0 and 3 tie with 2 reachable neighbors. We return the greater index, `3`.

### Example 2

```
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
```

**Explanation:** Reachable-neighbor counts within distance 2 (note that some shortest paths use multiple edges, e.g. `2 → 3 → 4` has total weight 2):

- City 0 → {1 (2)} = 1 city
- City 1 → {0 (2), 4 (2)} = 2 cities
- City 2 → {3 (1), 4 (2)} = 2 cities
- City 3 → {2 (1), 4 (1)} = 2 cities
- City 4 → {1 (2), 2 (2), 3 (1)} = 3 cities

City 0 has the smallest count (1 neighbor), so the answer is `0`.

## Hint

Build the full all-pairs shortest-distance matrix first, then for each city count how many others fall within the threshold. Floyd–Warshall gives you every pairwise distance in one `O(V³)` sweep.
