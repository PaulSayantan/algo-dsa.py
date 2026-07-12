# Course Schedule II (Lexicographically Smallest Order)

**Difficulty:** Medium

**Source:** LeetCode 210 — Course Schedule II (lex-smallest variant)

## Description

Given `numCourses` and `prerequisites` (`[a, b]` = `b` before `a`), return the **lexicographically smallest** valid ordering of all courses, or an empty list if impossible (a cycle exists).

## Hint

Kahn's algorithm but pull from a min-heap of in-degree-0 nodes to get the smallest order.
