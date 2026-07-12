# Count Distinct Subtrees — Solution

## Optimal Approach

### Reference implementation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    n = len(vals)
    while q and i < n:
        node = q.popleft()
        if i < n:
            if vals[i] is not None:
                node.left = TreeNode(vals[i])
                q.append(node.left)
            i += 1
        if i < n:
            if vals[i] is not None:
                node.right = TreeNode(vals[i])
                q.append(node.right)
            i += 1
    return root


class Solution:
    def countDuplicateSubtrees(self, vals):
        root = build_tree(vals)
        counts = {}

        def serialize(node):
            if node is None:
                return "#"
            s = str(node.val) + "," + serialize(node.left) + "," + serialize(node.right)
            counts[s] = counts.get(s, 0) + 1
            return s

        serialize(root)
        return sum(1 for c in counts.values() if c >= 2)

    def countDistinctSubtrees(self, vals):
        root = build_tree(vals)
        seen = set()

        def serialize(node):
            if node is None:
                return "#"
            s = str(node.val) + "," + serialize(node.left) + "," + serialize(node.right)
            seen.add(s)
            return s

        serialize(root)
        return len(seen)

    def sameTree(self, vals_a, vals_b):
        def serialize(node):
            if node is None:
                return "#"
            return str(node.val) + "(" + serialize(node.left) + ")(" + serialize(node.right) + ")"

        return serialize(build_tree(vals_a)) == serialize(build_tree(vals_b))
```

## Key Insights & Edge Cases

In `[2,1,1]` the two leaves labeled `1` share one serialization, so there are only 2 distinct subtrees: the leaf `1` and the whole tree.
