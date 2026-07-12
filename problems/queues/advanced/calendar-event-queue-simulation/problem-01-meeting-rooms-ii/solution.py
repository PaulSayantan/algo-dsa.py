"""Meeting Rooms II — LeetCode 253."""
from typing import List
import heapq  # noqa: F401


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # TODO: sort by start; min-heap of end times
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))  # expected: 2
    print(sol.minMeetingRooms([[7, 10], [2, 4]]))  # expected: 1
    print(sol.minMeetingRooms([[1, 5], [2, 6], [3, 7], [4, 8]]))  # expected: 4
