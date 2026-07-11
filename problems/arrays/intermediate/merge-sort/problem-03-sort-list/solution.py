from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Sort a singly linked list in ascending order using merge sort.

        Target O(n log n) time and O(1) auxiliary space (excluding the
        recursion stack).

        Args:
            head: Head node of the singly linked list (may be None).

        Returns:
            The head node of the sorted list.

        Example:
            Input list  4 -> 2 -> 1 -> 3
            Output list 1 -> 2 -> 3 -> 4
        """
        # TODO: implement
        pass


def _build(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def _to_list(head: Optional[ListNode]) -> list[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    s = Solution()
    print(_to_list(s.sortList(_build([4, 2, 1, 3]))))     # expected: [1, 2, 3, 4]
    print(_to_list(s.sortList(_build([-1, 5, 3, 4, 0])))) # expected: [-1, 0, 3, 4, 5]
    print(_to_list(s.sortList(_build([]))))               # expected: []
