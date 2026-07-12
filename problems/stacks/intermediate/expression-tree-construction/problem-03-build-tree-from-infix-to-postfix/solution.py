"""Build an expression tree from infix (with precedence) and emit postfix."""
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def infixToPostfix(self, infix: List[str]) -> List[str]:
        # TODO: two stacks (operators + subtrees), then postorder-walk the root
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.infixToPostfix(["3", "+", "4", "*", "2"]))  # expected: ['3', '4', '2', '*', '+']
    print(sol.infixToPostfix(["(", "3", "+", "4", ")", "*", "2"]))  # expected: ['3', '4', '+', '2', '*']
    print(sol.infixToPostfix(["(", "1", "+", "2", ")", "*", "(", "3", "-", "4", ")"]))  # expected: ['1', '2', '+', '3', '4', '-', '*']
    print(sol.infixToPostfix(["7"]))  # expected: ['7']
