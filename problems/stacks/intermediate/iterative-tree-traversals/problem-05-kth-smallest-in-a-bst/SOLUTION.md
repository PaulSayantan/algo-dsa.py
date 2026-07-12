# Kth Smallest Element in a BST — Solution

## Optimal Approach

Run the classic iterative in-order walk with an explicit stack: push the whole
left spine, then repeatedly pop-visit-and-go-right. Because an in-order traversal
of a BST visits values in ascending order, the value produced on the `k`-th pop
is the answer — so we can return immediately and skip the rest of the tree. This
touches only `O(h + k)` nodes and uses `O(h)` stack space.

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
    def kthSmallest(self, root, k):
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
        return -1
```
