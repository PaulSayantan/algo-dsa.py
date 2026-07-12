"""Rebuild fully-parenthesized infix from postfix via an expression tree."""
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def toInfix(self, postfix: List[str]) -> str:
        # TODO: build a subtree stack, then inorder-walk wrapping each operator
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.toInfix(["3", "4", "+", "2", "*"]))  # expected: '((3+4)*2)'
    print(sol.toInfix(["5", "1", "2", "+", "4", "*", "+", "3", "-"]))  # expected: '((5+((1+2)*4))-3)'
    print(sol.toInfix(["10", "2", "/"]))  # expected: '(10/2)'
    print(sol.toInfix(["7"]))  # expected: '7'
