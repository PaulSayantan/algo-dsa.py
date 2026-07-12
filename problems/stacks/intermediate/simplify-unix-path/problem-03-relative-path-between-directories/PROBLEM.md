# Relative Path Between Directories

**Difficulty:** Medium

**Source:** Classic — `os.path.relpath` for absolute Unix paths

## Description

Given two absolute Unix directory paths `from_path` and `to_path`, return the shortest **relative** path that navigates from `from_path` to `to_path` (like `os.path.relpath`).

Both inputs may contain `.`, `..`, empty parts, and redundant slashes and must first be canonicalized. The result uses `..` to climb out of the common prefix and then the remaining components of the destination, joined by `/`. If the two locations are identical, return `"."`.

Constraints: both paths are absolute (start with `/`).

## Examples

### Example 1

```
Input:  from_path = "/a/b/c", to_path = "/a/b/d/e"
Output: '../d/e'
```

**Explanation:** Canonical forms `/a/b/c` and `/a/b/d/e` share prefix `/a/b`. Climb one level (`..`), then descend into `d/e`.

## Hint

Canonicalize each path into a component stack via `simplify-unix-path`, drop the common prefix, emit one `..` per leftover source component, then append the leftover destination components.
