"""Binary Search Tree Iterator — LeetCode 173 (design).

`TreeNode` and `build` are provided. Implement the iterator methods only.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(vals):
    """Build a binary tree from a level-order list (None marks a missing child)."""
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


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]) -> None:
        # TODO: push the root's left spine onto an explicit stack
        pass

    def next(self) -> int:
        # TODO: pop the next-smallest node; push its right child's left spine
        pass

    def hasNext(self) -> bool:
        # TODO: True while the stack is non-empty
        pass


if __name__ == "__main__":
    bst = BSTIterator(build([7, 3, 15, None, None, 9, 20]))
    print(bst.next())  # expected: 3
    print(bst.next())  # expected: 7
    print(bst.hasNext())  # expected: True
    print(bst.next())  # expected: 9
    print(bst.next())  # expected: 15
    print(bst.hasNext())  # expected: True
    print(bst.next())  # expected: 20
    print(bst.hasNext())  # expected: False
