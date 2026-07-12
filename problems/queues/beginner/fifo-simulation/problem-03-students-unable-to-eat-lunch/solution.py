"""Number of Students Unable to Eat Lunch — LeetCode 1700."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # TODO: FIFO queue of students; if the front matches the top sandwich pop
        # both, else rotate the student to the back. Stop after a full lap with no
        # taker and return how many students remain.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))  # expected: 0
    print(sol.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))  # expected: 3
    print(sol.countStudents([0, 0], [1, 1]))  # expected: 2
