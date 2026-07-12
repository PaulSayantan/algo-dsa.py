# Crawler Log Folder

**Difficulty:** Medium

**Source:** LeetCode 1598 — Crawler Log Folder

## Description

The file system logs a sequence of change-folder operations in `logs`. Each entry is one of:

- `"../"` — move to the parent folder (a no-op if already at the main folder),
- `"./"` — stay in the same folder,
- `"x/"` — move into the child folder named `x`.

Starting at the main folder, return the **minimum number of operations** needed to go back to the main folder after performing every operation in `logs` — i.e. the folder depth you end up at.

Constraints: `1 <= len(logs)`, each `logs[i]` is a valid folder-change string.

## Examples

### Example 1

```
Input:  logs = ["d1/","d2/","../","d21/","./"]
Output: 2
```

**Explanation:** Descend to `/d1/d2`, go up to `/d1`, descend to `/d1/d21`, stay. Depth 2, so 2 ops return to the main folder.

## Hint

Treat the folders like `simplify-unix-path`: push a real name, pop on `../`, skip `./`. The answer is the stack's final size.
