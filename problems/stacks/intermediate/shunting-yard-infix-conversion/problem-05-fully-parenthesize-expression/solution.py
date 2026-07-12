"""Fully parenthesize an infix expression (Shunting-Yard, string rebuild)."""
from typing import List


class Solution:
    def fullyParenthesize(self, tokens: List[str]) -> str:
        # TODO: shunting-yard, but combine operand strings as "(a op b)"
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.fullyParenthesize(["a", "+", "b", "*", "c"]))  # expected: '(a+(b*c))'
    print(sol.fullyParenthesize(["a", "+", "b", "+", "c"]))  # expected: '((a+b)+c)'
    print(sol.fullyParenthesize(["(", "a", "+", "b", ")", "*", "c"]))  # expected: '((a+b)*c)'
    print(sol.fullyParenthesize(["a", "*", "b", "+", "c", "*", "d"]))  # expected: '((a*b)+(c*d))'
    print(sol.fullyParenthesize(["a"]))  # expected: 'a'
