"""Round-robin scheduling: return the Gantt dispatch order of time slices."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def ganttOrder(self, burst: List[int], quantum: int) -> List[int]:
        # TODO: FIFO queue of (id, remaining); append id on each dispatch,
        # run min(quantum, remaining), requeue if work remains
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.ganttOrder([5, 3, 8], 3))  # expected: [0, 1, 2, 0, 2, 2]
    print(sol.ganttOrder([4, 4, 4], 2))  # expected: [0, 1, 2, 0, 1, 2]
    print(sol.ganttOrder([10], 3))  # expected: [0, 0, 0, 0]
    print(sol.ganttOrder([2, 1, 3, 1], 2))  # expected: [0, 1, 2, 3, 2]
