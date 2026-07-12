"""Subtree serialization hashing: map a canonical serialization -> count.

Serialize each subtree to a canonical string (value + left + right) and use that
STRING as a dict key (never the salted built-in hash()).
"""
from typing import List, Optional  # noqa: F401
from collections import deque  # noqa: F401


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):
    """Build a binary tree from a LeetCode-style level-order list (None = missing)."""
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    n = len(vals)
    while q and i < n:
        node = q.popleft()
        if i < n:
            if vals[i] is not None:
                node.left = TreeNode(vals[i])
                q.append(node.left)
            i += 1
        if i < n:
            if vals[i] is not None:
                node.right = TreeNode(vals[i])
                q.append(node.right)
            i += 1
    return root


class Solution:
    def countDuplicateSubtrees(self, vals: List[Optional[int]]) -> int:
        # TODO: serialize each subtree; count serialization classes seen >= 2 times
        pass

    def countDistinctSubtrees(self, vals: List[Optional[int]]) -> int:
        # TODO: number of distinct subtree serializations
        pass

    def sameTree(self, vals_a: List[Optional[int]], vals_b: List[Optional[int]]) -> bool:
        # TODO: compare the two trees' serialization strings
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sameTree([1, 2, 3], [1, 2, 3]))  # expected: True
    print(sol.sameTree([1, 2, 3], [1, 2, None]))  # expected: False
    print(sol.sameTree([1, 2], [1, None, 2]))  # expected: False
    print(sol.sameTree([], []))  # expected: True
