"""Find Largest Value in Each Tree Row — LeetCode 515.

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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # TODO: BFS per level; record the max value drained from each level
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestValues(build([1, 3, 2, 5, 3, None, 9])))  # expected: [1, 3, 9]
    print(sol.largestValues(build([1, 2, 3])))  # expected: [1, 3]
    print(sol.largestValues(build([-5])))  # expected: [-5]
    print(sol.largestValues(build([])))  # expected: []
