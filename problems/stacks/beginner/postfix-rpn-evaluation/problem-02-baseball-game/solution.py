"""Baseball Game — LeetCode 682."""
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # TODO: use a stack; on '+'/'D' push a combination of the top scores, on 'C' pop
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.calPoints(["5", "2", "C", "D", "+"]))  # expected: 30
    print(sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # expected: 27
    print(sol.calPoints(["1", "C"]))  # expected: 0
    print(sol.calPoints(["-3", "D", "5", "C", "+"]))  # expected: -18
