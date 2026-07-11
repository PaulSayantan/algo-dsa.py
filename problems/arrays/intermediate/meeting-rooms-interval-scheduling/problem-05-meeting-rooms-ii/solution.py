"""Meeting Rooms II (LeetCode 253).

Return the minimum number of conference rooms needed to host all meetings, i.e. the
maximum number of meetings overlapping at any instant.
"""
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """Return the minimum number of rooms required.

        Args:
            intervals: A list of ``[start, end]`` pairs with ``start < end``.
                A meeting starting exactly when another ends may reuse the room.

        Returns:
            The minimum number of rooms (the peak count of concurrent meetings).

        Example:
            >>> Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]])
            2
            >>> Solution().minMeetingRooms([[7, 10], [2, 4]])
            1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))  # expected: 2
    print(sol.minMeetingRooms([[7, 10], [2, 4]]))             # expected: 1
    print(sol.minMeetingRooms([[1, 5], [5, 10], [2, 7]]))     # expected: 2
