"""Task Scheduler — LeetCode 621."""
from typing import List
from collections import Counter  # noqa: F401


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # TODO: frequency-based scheduling formula (or heap simulation)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # expected: 8
    print(sol.leastInterval(["A", "C", "A", "B", "D", "B"], 1))  # expected: 6
    print(sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0))  # expected: 6
