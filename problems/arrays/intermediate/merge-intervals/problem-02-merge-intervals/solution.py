"""Merge Intervals (LeetCode 56).

Empty solution template — fill in the logic yourself.
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merge all overlapping intervals.

        Args:
            intervals: A list of closed intervals ``[start, end]`` in any order.

        Returns:
            A list of non-overlapping intervals covering exactly the same points,
            conventionally sorted by start.

        Example:
            >>> Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
            [[1, 6], [8, 10], [15, 18]]
            >>> Solution().merge([[1, 4], [4, 5]])
            [[1, 5]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # expected: [[1, 6], [8, 10], [15, 18]]
    print(sol.merge([[1, 4], [4, 5]]))                     # expected: [[1, 5]]
    print(sol.merge([[1, 4], [2, 3]]))                     # expected: [[1, 4]]
