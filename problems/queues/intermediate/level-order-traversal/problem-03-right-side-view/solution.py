"""Binary Tree Right Side View — LeetCode 199.

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # TODO: BFS per level; append the last node value of each level
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.rightSideView(build([1, 2, 3, None, 5, None, 4])))  # expected: [1, 3, 4]
    print(sol.rightSideView(build([1, None, 3])))  # expected: [1, 3]
    print(sol.rightSideView(build([])))  # expected: []
