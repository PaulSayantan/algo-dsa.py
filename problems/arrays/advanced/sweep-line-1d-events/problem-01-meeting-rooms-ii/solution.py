"""Meeting Rooms II (LeetCode 253).

Fill in `Solution.minMeetingRooms` using a 1D sweep line over start/end events.
This file is an intentionally empty template — no working solution is provided.
"""

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """Return the minimum number of rooms needed for all meetings.

        A meeting occupies a room for the half-open interval [start, end):
        a meeting ending exactly when another starts may reuse the same room.
        The answer equals the maximum number of meetings simultaneously in
        progress (the peak of a +1/-1 sweep-line counter).

        Args:
            intervals: List of [start, end] pairs with start < end.

        Returns:
            The minimum number of conference rooms required.

        Example:
            >>> Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))  # expected: 2
    print(sol.minMeetingRooms([[7, 10], [2, 4]]))              # expected: 1
    print(sol.minMeetingRooms([[1, 5], [5, 9], [9, 12]]))      # expected: 1
