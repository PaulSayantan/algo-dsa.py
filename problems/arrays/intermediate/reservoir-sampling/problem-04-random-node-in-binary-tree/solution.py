"""Random Node in a Binary Tree (reservoir sampling, k = 1).

Fill in `Solution.get_random` so it returns a uniformly random node value using a
single traversal and O(1) extra space, without precomputing the node count.
"""
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "Optional[TreeNode]" = None,
        right: "Optional[TreeNode]" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self, root: Optional[TreeNode]) -> None:
        """Initialize with the root of the binary tree.

        Args:
            root: The root node (guaranteed non-empty per constraints).
        """
        # TODO: store the root; do NOT precompute the number of nodes
        pass

    def get_random(self) -> int:
        """Return the value of a uniformly random node in the tree.

        Each of the n nodes is returned with probability 1/n. Use one traversal
        (DFS or BFS) and O(1) extra space, without knowing n in advance.

        Returns:
            The value stored in the randomly selected node.

        Example:
            >>> root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
            >>> s = Solution(root)
            >>> s.get_random() in (1, 2, 3, 4)
            True
        """
        # TODO: implement using Reservoir Sampling with k = 1 during the traversal
        pass


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    s = Solution(root)
    print(s.get_random())  # expected: one of 1, 2, 3, 4 (uniformly at random)

    single = Solution(TreeNode(42))
    print(single.get_random())  # expected: 42 (only node)
