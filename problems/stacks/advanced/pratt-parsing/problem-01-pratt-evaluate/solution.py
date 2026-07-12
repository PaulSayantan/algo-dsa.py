"""Pratt / precedence-climbing evaluator with right-assoc power."""


class Solution:
    def evaluate(self, s: str) -> int:
        # TODO: precedence-climbing parse + evaluate
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.evaluate("2 + 3 * 4"))  # expected: 14
    print(sol.evaluate("2 ^ 3 ^ 2"))  # expected: 512
    print(sol.evaluate("(2 + 3) * 4"))  # expected: 20
    print(sol.evaluate("2 * 3 ^ 2"))  # expected: 18
    print(sol.evaluate("100 - 2 ^ 2 ^ 2"))  # expected: 84
