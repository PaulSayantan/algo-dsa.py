"""Infix -> Postfix (Shunting-Yard)."""
from typing import List


class Solution:
    def toPostfix(self, tokens: List[str]) -> List[str]:
        # TODO: operator stack honoring precedence & associativity
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.toPostfix(["a", "+", "b", "*", "c"]))  # expected: ['a', 'b', 'c', '*', '+']
    print(sol.toPostfix(["(", "a", "+", "b", ")", "*", "c"]))  # expected: ['a', 'b', '+', 'c', '*']
    print(sol.toPostfix(["a", "+", "b", "-", "c"]))  # expected: ['a', 'b', '+', 'c', '-']
    print(sol.toPostfix(["a", "*", "b", "+", "c", "*", "d"]))  # expected: ['a', 'b', '*', 'c', 'd', '*', '+']
