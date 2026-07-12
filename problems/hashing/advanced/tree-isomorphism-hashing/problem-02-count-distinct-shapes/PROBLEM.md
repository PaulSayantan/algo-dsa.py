# Count Distinct Rooted-Tree Shapes

**Difficulty:** Medium

**Source:** Classic — canonical tree hashing

## Description

Given a **forest** (a list of rooted trees, each a parent array with a single `-1` root), return the number of distinct tree shapes up to isomorphism — i.e. the number of distinct AHU canonical signatures.

## Examples

### Example 1

```
Input:  forest = [[-1,0,0],[1,-1,1],[-1,0,1],[-1]]
Output: 3
```

**Explanation:** two-leaf star (x2, same shape), a 3-path, and a single node

## Hint

Canonicalize each tree and insert the signature into a set; return the set size.
