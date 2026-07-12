"""Count Submatrices With All Ones — per-row histogram + monotonic stack."""
from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # TODO: build per-row heights; use a monotonic stack to sum subarray minima ending at each column
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubmat([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))  # expected: 13
    print(sol.numSubmat([[1, 1], [1, 1]]))  # expected: 9
    print(sol.numSubmat([[0, 0], [0, 0]]))  # expected: 0
    print(sol.numSubmat([[1]]))  # expected: 1
    print(sol.numSubmat([[1, 1, 1]]))  # expected: 6
