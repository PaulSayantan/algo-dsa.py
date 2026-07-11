"""LeetCode 2326 - Spiral Matrix IV.

Fill an m x n grid with the values of a linked list in clockwise spiral
order, padding any leftover cells with -1.
"""

from typing import List, Optional


class ListNode:
    """A node of a singly linked list."""

    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(
        self, m: int, n: int, head: Optional[ListNode]
    ) -> List[List[int]]:
        """Place linked-list values into an m x n grid along a spiral.

        The values are written in clockwise spiral order starting at the
        top-left cell. Cells left over after the list is exhausted are
        filled with -1.

        Args:
            m: Number of rows in the output matrix (m >= 1).
            n: Number of columns in the output matrix (n >= 1).
            head: Head node of the singly linked list (may be None only if
                the list is empty; per constraints it has 1..m*n nodes).

        Returns:
            An m x n list of lists holding the list values in spiral order,
            with -1 padding any unfilled cells.

        Example:
            >>> # head = 1 -> 2 -> 3 -> 4, m = 2, n = 2
            >>> # Solution().spiralMatrix(2, 2, head) == [[1, 2], [4, 3]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    # Build linked list 1 -> 2 -> 3 -> 4
    nodes = [ListNode(v) for v in (1, 2, 3, 4)]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    print(Solution().spiralMatrix(2, 2, nodes[0]))
    # Expected: [[1, 2], [4, 3]]
