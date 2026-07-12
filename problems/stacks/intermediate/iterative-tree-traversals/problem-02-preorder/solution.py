"""Binary Tree Preorder Traversal — LeetCode 144.

`TreeNode` and `build` are provided. Implement the traversal method only.
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(vals):
    """Build a binary tree from a level-order list (None marks a missing child)."""
    if not vals:
        return None
    from collections import deque
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # TODO: iterative traversal with an explicit stack
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.preorderTraversal(build([1, None, 2, 3])))  # expected: [1, 2, 3]
    print(sol.preorderTraversal(build([])))  # expected: []
    print(sol.preorderTraversal(build([1, 2, 3, 4, 5])))  # expected: [1, 2, 4, 5, 3]
