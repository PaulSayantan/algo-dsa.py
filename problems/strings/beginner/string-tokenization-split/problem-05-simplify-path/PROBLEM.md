# Simplify Path

**Difficulty:** Medium

**Source:** LeetCode 71 — Simplify Path

## Description

You are given an **absolute** path for a Unix-style file system, which always
begins with a slash `'/'`. Transform this absolute path into its **simplified
canonical path**.

In a Unix-style file system, the rules are:

- A single period `'.'` denotes the current directory.
- A double period `'..'` denotes moving up one directory level (the parent).
- Multiple consecutive slashes such as `'//'` and `'///'` are treated as a single
  slash `'/'`.
- Any sequence of periods that is **not** `'.'` or `'..'` (for example `'...'` or
  `'....'`) is treated as a **valid directory or file name**.

The simplified canonical path must follow these rules:

- It starts with a single slash `'/'`.
- Directories within the path are separated by exactly one slash `'/'`.
- It does not end with a trailing `'/'` (unless it is the root `'/'`).
- It does not include any single or double periods used to denote the current or
  parent directory.

Return the **simplified canonical path**.

## Constraints

- `1 <= path.length <= 3000`
- `path` consists of English letters, digits, period `'.'`, slash `'/'`, or
  underscore `'_'`.
- `path` is a valid absolute Unix path.

## Examples

**Example 1**

```
Input:  path = "/home/"
Output: "/home"
Explanation: The trailing slash is removed.
```

**Example 2**

```
Input:  path = "/home//foo/"
Output: "/home/foo"
Explanation: Multiple consecutive slashes are collapsed into a single one.
```

**Example 3**

```
Input:  path = "/a/./b/../../c/"
Output: "/c"
Explanation: "." is ignored; the first ".." pops "b", the second ".." pops "a",
leaving only "c".
```

## Hint

Use **String Tokenization / Split**: split the path on `'/'`, then walk the tokens
with a stack — ignore empty tokens and `'.'`, pop on `'..'`, and push real
directory names.
