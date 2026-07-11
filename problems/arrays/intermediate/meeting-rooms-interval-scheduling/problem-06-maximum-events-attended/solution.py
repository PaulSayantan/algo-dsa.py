"""Maximum Number of Events That Can Be Attended (LeetCode 1353).

Attend at most one event per day; maximize the number of events attended.
"""
import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """Return the maximum number of events that can be attended.

        Args:
            events: A list of ``[startDay, endDay]`` pairs (both inclusive) with
                ``startDay <= endDay``. You may attend one event per day, on any day
                within its ``[startDay, endDay]`` range.

        Returns:
            The maximum number of events that can be attended.

        Example:
            >>> Solution().maxEvents([[1, 2], [2, 3], [3, 4]])
            3
            >>> Solution().maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]])
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxEvents([[1, 2], [2, 3], [3, 4]]))          # expected: 3
    print(sol.maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]]))  # expected: 4
    print(sol.maxEvents([[1, 1], [1, 1], [1, 1]]))          # expected: 1
