# Are Two Rooted Trees Isomorphic?

**Difficulty:** Medium

**Source:** Classic — AHU tree isomorphism

## Description

Two rooted trees are given as parent arrays (`parent[i]` is the parent of node `i`, and the root has parent `-1`). They are **isomorphic** if one can be turned into the other by permuting the children of nodes (sibling order does not matter). Return whether the two rooted trees are isomorphic. Trees with different node counts are not isomorphic.

## Examples

### Example 1

```
Input:  a = [-1,0,0], b = [1,-1,1]
Output: True
```

**Explanation:** both are a root with two leaves

## Hint

Build each node's canonical signature from its children's SORTED signatures; compare the roots' signatures.
