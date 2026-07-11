from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Merge ``k`` ascending sorted linked lists into one sorted list.

        Suggested approach (min-heap over fronts):
          - seed a min-heap with the head node of every non-empty list,
          - repeatedly pop the smallest node, append it to the result, and
            push its ``next`` if present,
          - continue until the heap is empty.

        Because ``ListNode`` is not orderable, push tuples such as
        ``(node.val, unique_tiebreaker, node)`` so the heap never has to
        compare two nodes directly.

        Args:
            lists: List of ``k`` sorted linked-list heads (each may be None).

        Returns:
            The head of the merged sorted linked list, or None if empty.

        Example:
            lists = [1->4->5, 1->3->4, 2->6]
            returns 1->1->2->3->4->4->5->6
        """
        # TODO: implement
        pass


def build(values: List[int]) -> Optional[ListNode]:
    """Helper: build a linked list from a Python list of ints."""
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(node: Optional[ListNode]) -> List[int]:
    """Helper: convert a linked list back to a Python list of ints."""
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    s = Solution()
    lists = [build([1, 4, 5]), build([1, 3, 4]), build([2, 6])]
    print(to_list(s.mergeKLists(lists)))   # expected: [1, 1, 2, 3, 4, 4, 5, 6]
    print(to_list(s.mergeKLists([])))      # expected: []
    print(to_list(s.mergeKLists([None])))  # expected: []
