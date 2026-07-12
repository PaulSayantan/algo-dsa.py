"""Baseball Game. Maintain a stack of live scores and sum it at the end."""
from typing import List  # noqa: F401


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # TODO: use a stack; handle "C", "D", "+" against the top scores
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.calPoints(["5", "2", "C", "D", "+"]))  # expected: 30
    print(sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # expected: 27
    print(sol.calPoints(["1", "C"]))  # expected: 0
    print(sol.calPoints(["1", "2", "3"]))  # expected: 6
