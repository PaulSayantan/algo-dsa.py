"""Maximum Width of Binary Tree — LeetCode 662.

`TreeNode` and `build` are provided; implement the traversal method only.
"""
from typing import Optional


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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # TODO: BFS carrying positional indices; width = last_index - first_index + 1
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.widthOfBinaryTree(build([1, 3, 2, 5, 3, None, 9])))  # expected: 4
    print(sol.widthOfBinaryTree(build([1, 3, 2, 5, None, None, 9, 6, None, 7])))  # expected: 7
    print(sol.widthOfBinaryTree(build([1, 3, 2, 5])))  # expected: 2
    print(sol.widthOfBinaryTree(build([1])))  # expected: 1
    print(sol.widthOfBinaryTree(build([])))  # expected: 0
