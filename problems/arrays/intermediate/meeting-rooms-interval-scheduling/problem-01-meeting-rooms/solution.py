"""Meeting Rooms (LeetCode 252).

Determine whether a single person can attend every meeting, i.e. whether no two
intervals overlap.
"""
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """Return True if none of the meetings overlap.

        Args:
            intervals: A list of ``[start, end]`` pairs with ``start < end``.
                Meetings that only touch at an endpoint (``prev_end == next_start``)
                do NOT count as overlapping.

        Returns:
            True if all meetings can be attended by one person, else False.

        Example:
            >>> Solution().canAttendMeetings([[0, 30], [5, 10], [15, 20]])
            False
            >>> Solution().canAttendMeetings([[7, 10], [2, 4]])
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))  # expected: False
    print(sol.canAttendMeetings([[7, 10], [2, 4]]))             # expected: True
    print(sol.canAttendMeetings([[1, 5], [5, 8]]))              # expected: True
