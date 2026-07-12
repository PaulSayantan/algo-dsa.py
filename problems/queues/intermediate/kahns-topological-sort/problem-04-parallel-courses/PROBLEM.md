# Parallel Courses

**Difficulty:** Medium

**Source:** LeetCode 1136 — Parallel Courses

## Description

You are given an integer `n` (courses are labeled `1..n`) and an array
`relations` where `relations[i] = [a, b]` means course `a` must be taken
**before** course `b`.

In one semester you may take **any number** of courses, as long as every
prerequisite of each chosen course was completed in a **previous** semester.

Return the **minimum** number of semesters needed to complete all `n` courses.
If it is impossible (the prerequisite graph has a cycle), return `-1`.

Constraints: `1 <= n`, `1 <= a, b <= n`, `a != b`, no duplicate relations.

## Examples

### Example 1

```
Input:  n = 3, relations = [[1, 3], [2, 3]]
Output: 2
```

**Explanation:** Take courses `1` and `2` in semester 1, then course `3` in semester 2.

### Example 2

```
Input:  n = 3, relations = [[1, 2], [2, 3], [3, 1]]
Output: -1
```

**Explanation:** The three courses form a cycle, so they can never be finished.

## Hint

Run Kahn's algorithm level by level: each drained queue of in-degree-0 courses is one semester; the number of levels is the answer, and a leftover count means a cycle (`-1`).
