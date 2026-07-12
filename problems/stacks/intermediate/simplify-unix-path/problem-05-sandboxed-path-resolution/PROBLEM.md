# Sandboxed Path Resolution

**Difficulty:** Medium

**Source:** Classic — path-traversal (directory jail) resolution

## Description

A server serves files from an absolute `root` directory (e.g. `/var/www`). A client supplies a `user_path` (may be relative or contain `.`, `..`, empty parts, and redundant slashes). Resolve `user_path` **against** `root` and return the canonical absolute path.

For security, the resolved path must stay **inside** `root`: if resolving the `..` components would ever escape above `root`, reject the request by returning the empty string `""`. A `user_path` that resolves exactly to `root` is allowed.

Constraints: `root` is an absolute path; `user_path` is a valid path string.

## Examples

### Example 1

```
Input:  root = "/var/www", user_path = "images/logo.png"
Output: '/var/www/images/logo.png'
```

**Explanation:** Resolving `images/logo.png` under `/var/www` stays inside the jail.

## Hint

Seed the `simplify-unix-path` stack with `root`'s components, fold in `user_path`, and after resolving verify the stack still begins with `root`'s components — otherwise it escaped the jail.
