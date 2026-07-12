# Simplify Path

**Difficulty:** Medium

**Source:** LeetCode 71 — Simplify Path

## Description

Given an absolute Unix-style `path`, return its canonical form: it starts with a single `/`, has no trailing `/` (unless it is the root), collapses multiple slashes, resolves `.` (current) and `..` (parent), and never goes above the root.

## Examples

### Example 1

```
Input:  path = "/a/./b/../../c/"
Output: "/c"
```

## Hint

Split on '/'; push names, skip '' and '.', pop on '..'. Join with '/' prefixed by root '/'.
