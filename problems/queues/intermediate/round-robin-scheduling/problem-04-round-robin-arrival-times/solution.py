"""Round-robin scheduling with arrival times: return per-process completion times."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def completionTimes(self, arrival: List[int], burst: List[int], quantum: int) -> List[int]:
        # TODO: enqueue by arrival <= clock (arrivals first, then requeue the
        # running process); idle-jump the clock to the next arrival when empty
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.completionTimes([0, 1, 2], [5, 3, 8], 3))  # expected: [11, 6, 16]
    print(sol.completionTimes([0, 0, 0], [4, 4, 4], 2))  # expected: [8, 10, 12]
    print(sol.completionTimes([0, 2, 4], [3, 1, 2], 2))  # expected: [4, 3, 6]
    print(sol.completionTimes([5], [4], 2))  # expected: [9]
    print(sol.completionTimes([0, 1, 2, 3], [4, 3, 1, 2], 2))  # expected: [7, 10, 5, 9]
