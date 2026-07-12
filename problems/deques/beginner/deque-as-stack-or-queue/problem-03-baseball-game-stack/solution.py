"""Baseball Game: run integer/`+`/`D`/`C` ops on a deque used as a stack."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # TODO: push ints, dq[-1]/dq[-2] for 'D'/'+', pop for 'C'; return sum
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.calPoints(["5", "2", "C", "D", "+"]))  # expected: 30
    print(sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # expected: 27
    print(sol.calPoints(["1", "C"]))  # expected: 0
