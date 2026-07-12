"""Detect a duplicate operator subexpression in a postfix expression tree."""
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasDuplicateSubexpr(self, postfix: List[str]) -> bool:
        # TODO: build the tree, sign each subtree, flag a repeated operator signature
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.hasDuplicateSubexpr(["3", "4", "+", "3", "4", "+", "*"]))  # expected: True
    print(sol.hasDuplicateSubexpr(["3", "4", "+", "2", "*"]))  # expected: False
    print(sol.hasDuplicateSubexpr(["1", "2", "+", "3", "4", "+", "-"]))  # expected: False
    print(sol.hasDuplicateSubexpr(["2", "3", "*", "4", "+", "2", "3", "*", "4", "+", "-"]))  # expected: True
    print(sol.hasDuplicateSubexpr(["5"]))  # expected: False
