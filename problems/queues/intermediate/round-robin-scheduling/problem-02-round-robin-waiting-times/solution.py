"""Round-robin scheduling: return per-process waiting times."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def waitingTimes(self, burst: List[int], quantum: int) -> List[int]:
        # TODO: simulate the FIFO queue, track a global clock and completion times,
        # then waiting[i] = completion[i] - burst[i]
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.waitingTimes([5, 3, 8], 3))  # expected: [6, 3, 8]
    print(sol.waitingTimes([4, 4, 4], 2))  # expected: [4, 6, 8]
    print(sol.waitingTimes([10], 3))  # expected: [0]
    print(sol.waitingTimes([2, 1, 3, 1], 2))  # expected: [0, 2, 4, 5]
