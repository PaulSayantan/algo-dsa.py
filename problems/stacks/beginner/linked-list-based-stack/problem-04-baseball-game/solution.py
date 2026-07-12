"""Baseball Game — LeetCode 682."""
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # TODO: treat the record as a stack; push/pop/peek per operation
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.calPoints(["5", "2", "C", "D", "+"]))  # expected: 30
    print(sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # expected: 27
    print(sol.calPoints(["1", "C"]))  # expected: 0
    print(sol.calPoints(["1", "2", "3", "4", "5"]))  # expected: 15
