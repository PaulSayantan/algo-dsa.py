"""Build an expression tree from postfix and evaluate it."""
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evalTree(self, postfix: List[str]) -> int:
        # TODO: build with a stack of subtrees, then evaluate
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.evalTree(["3", "4", "+", "2", "*"]))  # expected: 14
    print(sol.evalTree(["5", "1", "2", "+", "4", "*", "+", "3", "-"]))  # expected: 14
    print(sol.evalTree(["7"]))  # expected: 7
