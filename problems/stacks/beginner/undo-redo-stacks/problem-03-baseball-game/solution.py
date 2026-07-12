"""Baseball Game: replay scored operations on a stack, 'C' undoes the last."""
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # TODO: push scores on a stack; 'C' pops, 'D' doubles top, '+' sums top two
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.calPoints(["5", "2", "C", "D", "+"]))            # expected: 30
    print(sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # expected: 27
    print(sol.calPoints(["1", "C"]))                           # expected: 0
    print(sol.calPoints(["7"]))                                # expected: 7
