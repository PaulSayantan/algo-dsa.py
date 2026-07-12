"""Infix -> Prefix (Shunting-Yard, reversed pass)."""
from typing import List


class Solution:
    def toPrefix(self, tokens: List[str]) -> List[str]:
        # TODO: reverse + swap parens, shunting-yard, reverse the result
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.toPrefix(["a", "+", "b", "*", "c"]))  # expected: ['+', 'a', '*', 'b', 'c']
    print(sol.toPrefix(["(", "a", "+", "b", ")", "*", "c"]))  # expected: ['*', '+', 'a', 'b', 'c']
    print(sol.toPrefix(["a", "-", "b", "-", "c"]))  # expected: ['-', '-', 'a', 'b', 'c']
    print(sol.toPrefix(["a", "+", "b", "+", "c", "*", "d"]))  # expected: ['+', '+', 'a', 'b', '*', 'c', 'd']
