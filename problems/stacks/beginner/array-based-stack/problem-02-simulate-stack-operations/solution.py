"""Simulate a stack over a list of operations and return the final contents."""
from typing import List  # noqa: F401


class Solution:
    def finalStack(self, ops: List[list]) -> List[int]:
        # TODO: process ("push", v) and ("pop",) operations on a stack
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.finalStack([["push", 1], ["push", 2], ["pop"], ["push", 3]]))  # expected: [1, 3]
    print(sol.finalStack([["push", 5], ["pop"], ["pop"]]) if False else sol.finalStack([["push", 5], ["push", 6]]))  # expected: [5, 6]
