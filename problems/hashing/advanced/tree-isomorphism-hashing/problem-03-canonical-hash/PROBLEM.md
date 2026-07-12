# Canonical Hash of a Rooted Tree

**Difficulty:** Medium

**Source:** Classic — AHU canonical form

## Description

Given a rooted tree as a parent array (root's parent is `-1`), return its **canonical AHU signature string**: each node maps to `(` followed by its children's canonical strings concatenated in sorted order, then `)`. A single node is `()`.

## Examples

### Example 1

```
Input:  parent = [-1,0,0]
Output: (()())
```

**Explanation:** root with two leaves

## Hint

Recurse: signature(u) = '(' + ''.join(sorted(signature(child) for child in children)) + ')'.
