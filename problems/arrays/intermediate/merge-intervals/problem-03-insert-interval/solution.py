"""Insert Interval (LeetCode 57).

Empty solution template — fill in the logic yourself.
"""
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """Insert ``newInterval`` into a sorted, non-overlapping ``intervals``.

        Args:
            intervals: Existing intervals, sorted by start and pairwise disjoint.
            newInterval: The interval ``[start, end]`` to insert.

        Returns:
            The resulting sorted, non-overlapping list of intervals with
            ``newInterval`` merged in.

        Example:
            >>> Solution().insert([[1, 3], [6, 9]], [2, 5])
            [[1, 5], [6, 9]]
            >>> Solution().insert([], [5, 7])
            [[5, 7]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1, 3], [6, 9]], [2, 5]))                        # expected: [[1, 5], [6, 9]]
    print(sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # expected: [[1, 2], [3, 10], [12, 16]]
    print(sol.insert([], [5, 7]))                                      # expected: [[5, 7]]
