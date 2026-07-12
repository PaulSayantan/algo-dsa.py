# Jump Game IV

**Difficulty:** Medium

**Source:** LeetCode 1345 — Jump Game IV

## Description

Given an integer array `arr`, you start at index `0`. In one step, from index `i` you may jump to `i + 1`, to `i - 1`, or to any other index `j` such that `arr[i] == arr[j]` (both destinations must be within bounds). Return the minimum number of steps to reach the last index `len(arr) - 1`. A solution always exists.

The index graph is undirected — a step from `i` to `j` can be taken back from `j` to `i` — so the search can run from both ends and meet in the middle.

## Examples

### Example 1

```
Input:  arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
Output: 3
```

**Explanation:** `0 -> 4` (same value `100`) `-> 3` (adjacent index) `-> 9` (same value `404`) reaches the last index in 3 steps.

### Example 2

```
Input:  arr = [7, 6, 9, 6, 9, 6, 9, 7]
Output: 1
```

**Explanation:** Index `0` and the last index both hold `7`, so one value-jump reaches the end.

## Hint

Model indices as nodes: each `i` connects to `i-1`, `i+1`, and every index sharing its value. Run BFS from index `0` and from the last index at once, always expanding the smaller frontier; when the two frontiers touch, the accumulated step count is the answer. Clear each value-group after its first expansion so the shared indices are never rescanned.
