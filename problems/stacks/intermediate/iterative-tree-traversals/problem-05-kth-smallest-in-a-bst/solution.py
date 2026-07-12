"""Kth Smallest Element in a BST — LeetCode 230.

`TreeNode` and `build` are provided. Implement the traversal method only.
"""
from typing import Optional


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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # TODO: iterative in-order walk; return the value on the k-th pop
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kthSmallest(build([3, 1, 4, None, 2]), 1))  # expected: 1
    print(sol.kthSmallest(build([5, 3, 6, 2, 4, None, None, 1]), 3))  # expected: 3
    print(sol.kthSmallest(build([2, 1, 3]), 2))  # expected: 2
    print(sol.kthSmallest(build([1]), 1))  # expected: 1
