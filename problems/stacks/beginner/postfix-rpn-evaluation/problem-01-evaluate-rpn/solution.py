"""Evaluate Reverse Polish Notation — LeetCode 150."""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # TODO: use a stack; truncate division toward zero with int(a / b)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(["2", "1", "+", "3", "*"]))  # expected: 9
    print(sol.evalRPN(["4", "13", "5", "/", "+"]))  # expected: 6
    print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # expected: 22
    print(sol.evalRPN(["3", "-4", "+"]))  # expected: -1
