# Find Largest Value in Each Tree Row — Solution

## Optimal Approach

### Reference implementation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(vals):
    if not vals:
        return None
    it = iter(vals)
    root = TreeNode(next(it))
    q = deque([root])
    while q:
        node = q.popleft()
        try:
            lv = next(it)
        except StopIteration:
            break
        if lv is not None:
            node.left = TreeNode(lv)
            q.append(node.left)
        try:
            rv = next(it)
        except StopIteration:
            break
        if rv is not None:
            node.right = TreeNode(rv)
            q.append(node.right)
    return root


class Solution:
    def largestValues(self, root):
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            best = None
            for _ in range(len(q)):
                node = q.popleft()
                if best is None or node.val > best:
                    best = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(best)
        return res
```
