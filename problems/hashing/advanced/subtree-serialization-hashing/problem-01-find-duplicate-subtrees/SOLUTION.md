# Find Duplicate Subtrees — Solution

## Optimal Approach

Post-order serialize each subtree into a canonical string and tally it in a dict; every serialization whose count reaches 2 is a duplicate class. The count of such classes is the answer.

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

### Complexity

O(n) nodes; serialization strings total O(n^2) worst case.

## Key Insights & Edge Cases

We return the COUNT of duplicate classes (a deterministic integer), not the node objects — node objects are not serializable literals.
