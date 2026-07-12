# Binary Search Tree Iterator — Solution

## Optimal Approach

Store only the left spine of the not-yet-visited subtree on an explicit stack.
The top of the stack is always the next-smallest node. On `next()`, pop it; if
it has a right child, push that child's own left spine. Each node is pushed and
popped exactly once, so `next()` is amortized `O(1)` and space is `O(h)`.

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


class BSTIterator:
    def __init__(self, root):
        self._stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self._stack.append(node)
            node = node.left

    def next(self):
        node = self._stack.pop()
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self):
        return bool(self._stack)
```
