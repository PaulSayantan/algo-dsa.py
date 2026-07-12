# Are Two Rooted Trees Isomorphic? — Solution

## Optimal Approach

Canonicalize each tree bottom-up: a node's signature is the bracketed concatenation of its children's signatures in sorted order. The trees are isomorphic iff the two root signatures are equal.

### Reference implementation

```python
class Solution:
    def _canonical(self, parent):
        n = len(parent)
        children = [[] for _ in range(n)]
        root = -1
        for i, p in enumerate(parent):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        def dfs(u):
            parts = sorted(dfs(c) for c in children[u])
            return "(" + "".join(parts) + ")"

        return dfs(root)

    def canonicalHash(self, parent):
        return self._canonical(parent)

    def areIsomorphic(self, parent_a, parent_b):
        if len(parent_a) != len(parent_b):
            return False
        return self._canonical(parent_a) == self._canonical(parent_b)

    def countDistinctShapes(self, forest):
        shapes = set()
        for parent in forest:
            shapes.add(self._canonical(parent))
        return len(shapes)
```

### Complexity

O(n log n) per tree (sorting sibling signatures).

## Key Insights & Edge Cases

Sorting the child signatures is what makes the encoding independent of sibling order — the crux of rooted-tree isomorphism.
