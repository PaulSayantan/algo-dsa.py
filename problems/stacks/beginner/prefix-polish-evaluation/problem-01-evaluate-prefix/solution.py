"""Evaluate a prefix (Polish notation) expression."""
from typing import List


class Solution:
    def evalPrefix(self, tokens: List[str]) -> int:
        # TODO: scan right-to-left with a stack
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.evalPrefix(["+", "2", "3"]))  # expected: 5
    print(sol.evalPrefix(["*", "+", "2", "3", "4"]))  # expected: 20
    print(sol.evalPrefix(["-", "9", "4"]))  # expected: 5
    print(sol.evalPrefix(["/", "10", "3"]))  # expected: 3
