# Maximum Width of Binary Tree — Solution

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
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        max_width = 0
        q = deque([(root, 0)])
        while q:
            first = q[0][1]
            last = first
            for _ in range(len(q)):
                node, idx = q.popleft()
                idx -= first  # normalize per level to keep indices bounded
                last = idx
                if node.left:
                    q.append((node.left, 2 * idx))
                if node.right:
                    q.append((node.right, 2 * idx + 1))
            max_width = max(max_width, last + 1)
        return max_width
```
