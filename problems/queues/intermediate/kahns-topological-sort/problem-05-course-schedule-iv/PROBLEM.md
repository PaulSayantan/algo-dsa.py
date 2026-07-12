# Course Schedule IV

**Difficulty:** Medium

**Source:** LeetCode 1462 — Course Schedule IV

## Description

There are `numCourses` courses labeled `0..numCourses-1`. You are given a list
`prerequisites` where `prerequisites[i] = [a, b]` means course `a` must be taken
before course `b` (so `a` is a **direct** prerequisite of `b`). Prerequisites are
transitive: if `a` is a prerequisite of `b` and `b` is a prerequisite of `c`,
then `a` is a prerequisite of `c`. The graph is guaranteed to be a DAG.

You are also given `queries` where `queries[j] = [u, v]`. For each query answer
whether course `u` is a prerequisite of course `v` (directly or transitively).

Return a list of booleans, one per query, in the same order.

Constraints: `2 <= numCourses`, all prerequisite pairs are distinct, and the
graph is acyclic.

## Examples

### Example 1

```
Input:  numCourses = 4, prerequisites = [[0,1],[1,2],[2,3]], queries = [[0,3],[3,0],[0,1],[2,0]]
Output: [true, false, true, false]
```

**Explanation:** `0 -> 1 -> 2 -> 3` is a chain, so `0` reaches `3` and `1` but nothing reaches back.

### Example 2

```
Input:  numCourses = 3, prerequisites = [], queries = [[0,1],[1,2]]
Output: [false, false]
```

**Explanation:** With no prerequisites, no course precedes another.

## Hint

Process courses in Kahn's topological order and propagate each node's ancestor set forward to its neighbors; then a query `[u, v]` is just membership of `u` in `v`'s ancestor set.
