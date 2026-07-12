# Design File System Navigator

**Difficulty:** Medium

**Source:** Classic — shell `cd` / `pwd` working-directory simulator

## Description

Design a `FileSystemNavigator` that models a shell's current working directory. It starts at the root `/` and supports:

- `cd(path)` — change directory. If `path` is **absolute** (starts with `/`) the current location resets to root before applying it; otherwise it is **relative** to the current directory. Within `path`, empty parts and `.` are ignored, and `..` moves to the parent (a no-op at root).
- `pwd()` — return the canonical absolute path of the current directory (starts with `/`, no trailing slash except at root).

Constraints: every `path` is a valid Unix-style path string.

## Examples

### Example 1

```
Input:
  ["FileSystemNavigator","cd","pwd","cd","pwd"]
  [[],["/usr/local/bin"],[],["../../share"],[]]
Output:
  [null,null,"/usr/local/bin",null,"/usr/share"]
```

**Explanation:** Absolute `cd` sets `/usr/local/bin`; the relative `cd ../../share` pops `bin` and `local`, then pushes `share`.

## Hint

Keep the current directory as a `simplify-unix-path` component stack: reset it when `path` is absolute, then push names, skip `.`, and pop on `..`.
