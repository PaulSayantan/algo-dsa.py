"""Binary Tree Level Order Traversal — LeetCode 102.

`TreeNode` and `build` are provided; implement the traversal method only.
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(vals):
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
    def levelOrder(self, root: Optional[TreeNode]) -> List:
        # TODO: BFS level-order traversal with a queue
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.levelOrder(build([3, 9, 20, None, None, 15, 7])))  # expected: [[3], [9, 20], [15, 7]]
    print(sol.levelOrder(build([1])))  # expected: [[1]]
    print(sol.levelOrder(build([])))  # expected: []
