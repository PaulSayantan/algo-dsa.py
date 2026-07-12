"""Evaluate an infix arithmetic expression (Shunting-Yard, two stacks)."""


class Solution:
    def evaluate(self, expr: str) -> int:
        # TODO: value stack + operator stack; apply on pop by precedence
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.evaluate("3+4*2"))  # expected: 11
    print(sol.evaluate("(3+4)*2"))  # expected: 14
    print(sol.evaluate("10 - 2 - 3"))  # expected: 5
    print(sol.evaluate("100/(2+3)"))  # expected: 20
    print(sol.evaluate("2*3+4*5"))  # expected: 26
