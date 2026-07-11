"""Task Scheduler — LeetCode 621.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """Return the minimum time units to run all tasks respecting the cooldown.

        Each task takes one time unit. Two identical tasks must be separated by at
        least n units (running other tasks or idling in between).

        Args:
            tasks: Uppercase letters ('A'-'Z'); each is one unit of work.
            n: Required cooldown gap between two runs of the same task.

        Returns:
            The minimum number of time units (including any idle units) to finish.

        Example:
            >>> Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2)
            8
            >>> Solution().leastInterval(["A", "C", "A", "B", "D", "B"], 1)
            6
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # expected: 8
    print(sol.leastInterval(["A", "C", "A", "B", "D", "B"], 1))  # expected: 6
    print(sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0))  # expected: 6
