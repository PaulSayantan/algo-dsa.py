# Course Schedule

**Difficulty:** Medium

**Source:** LeetCode 207 — Course Schedule

## Description

There are `numCourses` courses `0..numCourses-1`. `prerequisites[i] = [a, b]` means you must take `b` before `a`. Return `True` if you can finish all courses (the dependency graph is acyclic), else `False`.

## Examples

### Example 1

```
Input:  numCourses = 2, prerequisites = [[1,0]]
Output: true
```

## Hint

Kahn's algorithm: if the topological order includes all courses, there's no cycle.
