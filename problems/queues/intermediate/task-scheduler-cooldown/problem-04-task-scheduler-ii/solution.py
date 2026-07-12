"""Task Scheduler II — LeetCode 2365."""
from typing import List  # noqa: F401


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        # TODO: map each type -> its next-available day; advance day, skipping cooldown
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.taskSchedulerII([1, 2, 1, 2, 3, 1], 3))  # expected: 9
    print(sol.taskSchedulerII([5, 8, 8, 5], 2))  # expected: 6
    print(sol.taskSchedulerII([1, 1, 1], 0))  # expected: 3
    print(sol.taskSchedulerII([1], 5))  # expected: 1
