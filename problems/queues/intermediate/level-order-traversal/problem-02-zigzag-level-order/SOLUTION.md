# Binary Tree Zigzag Level Order Traversal — Solution

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
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        q = deque([root])
        left_to_right = True
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level if left_to_right else level[::-1])
            left_to_right = not left_to_right
        return res
```
