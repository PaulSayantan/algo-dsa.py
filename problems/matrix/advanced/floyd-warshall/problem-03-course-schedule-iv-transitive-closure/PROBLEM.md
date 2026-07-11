# Course Schedule IV

**Difficulty:** Medium

**Source:** LeetCode 1462

## Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [aᵢ, bᵢ]` indicates that you **must** take course `aᵢ` first if you want to take course `bᵢ` (that is, `aᵢ` is a direct prerequisite of `bᵢ`).

Prerequisites can also be **indirect**: if `a` is a prerequisite of `b` and `b` is a prerequisite of `c`, then `a` is a prerequisite of `c`.

You are also given an array `queries` where `queries[j] = [uⱼ, vⱼ]`. For the `j`-th query, answer whether course `uⱼ` is a prerequisite (direct or indirect) of course `vⱼ`.

Return a boolean array `answer`, where `answer[j]` is the answer to the `j`-th query.

The graph of prerequisites is guaranteed to be a **DAG** (no cycles).

## Constraints

- `2 <= numCourses <= 100`
- `0 <= prerequisites.length <= (numCourses * (numCourses - 1)) / 2`
- `prerequisites[i].length == 2`
- `0 <= aᵢ, bᵢ <= numCourses - 1`
- `aᵢ != bᵢ`
- All the pairs `[aᵢ, bᵢ]` are **unique**.
- `1 <= queries.length <= 10^4`
- `0 <= uⱼ, vⱼ <= numCourses - 1`

## Examples

### Example 1

```
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false, true]
```

**Explanation:** The pair `[1, 0]` means course `1` must be taken before course `0`.

- Query `[0, 1]`: is `0` a prerequisite of `1`? No → `false`.
- Query `[1, 0]`: is `1` a prerequisite of `0`? Yes (given directly) → `true`.

### Example 2

```
Input: numCourses = 3, prerequisites = [[0,1],[1,2]], queries = [[0,2],[2,0]]
Output: [true, false]
```

**Explanation:** The chain is `0 → 1 → 2`.

- Query `[0, 2]`: `0` is an **indirect** prerequisite of `2` (via `1`) → `true`.
- Query `[2, 0]`: there is no path from `2` back to `0` → `false`.

### Example 3

```
Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true, true]
```

**Explanation:** Course `1` is a direct prerequisite of both `0` and `2`, and course `2` is a direct prerequisite of `0`.

- Query `[1, 0]`: `1` is a prerequisite of `0` (directly, and also via `1 → 2 → 0`) → `true`.
- Query `[1, 2]`: `1` is a direct prerequisite of `2` → `true`.

## Hint

You need the reachability relation "can I get from `u` to `v`?" for every pair of courses. Run Floyd–Warshall with boolean OR/AND instead of min/plus to compute the transitive closure of the prerequisite graph, then each query is an `O(1)` matrix lookup.
