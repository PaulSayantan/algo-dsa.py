from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Sort a singly linked list using Insertion Sort and return the new head.

        Rewire the ``next`` pointers of the existing nodes; do not sort a copied
        array of values.

        Args:
            head: Head of a singly linked list with 1..5000 nodes, each value in
                the range [-5000, 5000]. May be None for an empty list.

        Returns:
            The head of the list sorted in ascending order.

        Example:
            >>> # head = 4 -> 2 -> 1 -> 3
            >>> # returns 1 -> 2 -> 3 -> 4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    def build(values):
        dummy = ListNode()
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    def to_list(node):
        out = []
        while node:
            out.append(node.val)
            node = node.next
        return out

    sol = Solution()
    print(to_list(sol.insertionSortList(build([4, 2, 1, 3]))))       # expected: [1, 2, 3, 4]
    print(to_list(sol.insertionSortList(build([-1, 5, 3, 4, 0]))))   # expected: [-1, 0, 3, 4, 5]
    print(to_list(sol.insertionSortList(build([1]))))                # expected: [1]
