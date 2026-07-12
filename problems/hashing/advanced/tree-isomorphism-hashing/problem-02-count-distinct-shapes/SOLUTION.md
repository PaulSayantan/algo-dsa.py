# Count Distinct Rooted-Tree Shapes — Solution

## Optimal Approach

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

## Key Insights & Edge Cases

`[-1,0,0]` and `[1,-1,1]` are the same star shape with different labels, so they collapse to one canonical signature.
