"""Build an expression tree from prefix (Polish) notation and evaluate it."""
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evalPrefix(self, prefix: List[str]) -> int:
        # TODO: scan right to left, build a subtree stack, then evaluate the root
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.evalPrefix(["*", "+", "3", "4", "2"]))  # expected: 14
    print(sol.evalPrefix(["-", "/", "10", "2", "3"]))  # expected: 2
    print(sol.evalPrefix(["+", "9", "*", "2", "3"]))  # expected: 15
    print(sol.evalPrefix(["42"]))  # expected: 42
