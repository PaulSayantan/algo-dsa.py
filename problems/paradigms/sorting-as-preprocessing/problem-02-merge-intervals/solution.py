"""Merge Intervals — LeetCode 56.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merge all overlapping intervals.

        Two intervals overlap when the later one starts at or before the earlier
        one ends (touching intervals like [1,4] and [4,5] count as overlapping).

        Args:
            intervals: A list of [start, end] closed intervals.

        Returns:
            A list of non-overlapping intervals that cover exactly the same points
            as the input, conventionally sorted by start.

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
    print(sol.merge([[1, 4], [4, 5]]))                      # expected: [[1, 5]]
    print(sol.merge([[1, 4], [2, 3]]))                      # expected: [[1, 4]]
