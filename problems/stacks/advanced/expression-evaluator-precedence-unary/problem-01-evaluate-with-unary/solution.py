"""Full infix evaluator with unary minus (two-stack)."""


class Solution:
    def evaluate(self, s: str) -> int:
        # TODO: operand + operator stacks; handle unary minus
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.evaluate("-3 + 4 * 2"))  # expected: 5
    print(sol.evaluate("2*(-4)"))  # expected: -8
    print(sol.evaluate("-(3 + 4)"))  # expected: -7
    print(sol.evaluate("3 + 5 * 2 - 8 / 4"))  # expected: 11
    print(sol.evaluate("2 * (3 + -4)"))  # expected: -2
