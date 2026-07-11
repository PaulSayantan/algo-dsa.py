"""The K Weakest Rows in a Matrix — partial Selection Sort (LeetCode 1337).

Return the indices of the k weakest rows, weakest first, by selecting the k
smallest (soldier_count, row_index) keys.
"""
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """Return the indices of the k weakest rows, ordered weakest to strongest.

        A row is weaker if it has fewer 1s, breaking ties by smaller row index.

        Args:
            mat: An m x n binary matrix where each row has all 1s before all 0s.
            k: How many weakest row indices to return; 1 <= k <= len(mat).

        Returns:
            A list of k row indices, ordered from weakest to strongest by the
            (soldier_count, row_index) key.

        Example:
            >>> Solution().kWeakestRows(
            ...     [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0]], 3)
            [2, 0, 3]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kWeakestRows(
        [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]], 3))
    # expected: [2, 0, 3]
    print(sol.kWeakestRows(
        [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2))
    # expected: [0, 2]
    print(sol.kWeakestRows([[1, 1], [1, 0]], 1))
    # expected: [1]
