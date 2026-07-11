"""Maximum Students Taking Exam (LeetCode 1349).

Seat as many students as possible with no left/right neighbour and no
upper-left / upper-right (diagonal-front) neighbour, avoiding broken seats.

Solve this with row-by-row Bitmask DP ("profile DP"). Represent each row's
seating as an n-bit mask (bit c set = a student sits in column c). A mask is
valid for a row if it uses only working seats and has no two horizontally
adjacent students. Two masks in consecutive rows are compatible if no student in
the lower row sits diagonally in front of a student in the upper row.
"""

from __future__ import annotations

from typing import List


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        """Return the maximum number of students that can be seated.

        Args:
            seats: An m x n grid of '.' (good seat) and '#' (broken seat),
                with 1 <= m, n <= 8.

        Returns:
            The largest number of students placeable in good seats such that no
            two are horizontally adjacent and no student sits in the upper-left
            or upper-right seat of another.

        Example:
            >>> Solution().maxStudents([[".", "#"], ["#", "#"], ["#", "."],
            ...                         ["#", "#"], [".", "#"]])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxStudents([["#", ".", "#", "#", ".", "#"],
                           [".", "#", "#", "#", "#", "."],
                           ["#", ".", "#", "#", ".", "#"]]))  # expected: 4
    print(sol.maxStudents([[".", "#"], ["#", "#"], ["#", "."],
                           ["#", "#"], [".", "#"]]))          # expected: 3
    print(sol.maxStudents([["#", ".", ".", ".", "#"],
                           [".", "#", ".", "#", "."],
                           [".", ".", "#", ".", "."],
                           [".", "#", ".", "#", "."],
                           ["#", ".", ".", ".", "#"]]))       # expected: 10
