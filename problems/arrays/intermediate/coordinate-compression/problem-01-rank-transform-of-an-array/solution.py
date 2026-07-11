"""Rank Transform of an Array (LeetCode 1331).

Fill in the body of `arrayRankTransform`. Do NOT look at SOLUTION.md until you
have made a genuine attempt.
"""

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """Replace every element of ``arr`` with its 1-based rank.

        The rank of a value is its position (starting at 1) in the sorted list of
        distinct values of ``arr``. Equal values receive equal ranks, and ranks are
        assigned with no gaps.

        Args:
            arr: The input array of integers. May be empty.

        Returns:
            A new list of the same length where each element is replaced by its rank.

        Example:
            >>> Solution().arrayRankTransform([40, 10, 20, 30])
            [4, 1, 2, 3]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.arrayRankTransform([40, 10, 20, 30]))            # expected: [4, 1, 2, 3]
    print(sol.arrayRankTransform([100, 100, 100]))             # expected: [1, 1, 1]
    print(sol.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))
    # expected: [5, 3, 4, 2, 8, 6, 7, 1, 3]
    print(sol.arrayRankTransform([]))                          # expected: []
