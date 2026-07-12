"""Task Dispatch Log: return the round-robin order tasks are picked to run."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def dispatchLog(self, work: List[int], quantum: int) -> List[int]:
        # TODO: FIFO queue of [task_id, work_left]; each slice pop the front, log its
        # id, run up to `quantum` units, and re-enqueue only if work still remains
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.dispatchLog([4, 2, 3], 2))  # expected: [0, 1, 2, 0, 2]
    print(sol.dispatchLog([1, 1, 1], 1))  # expected: [0, 1, 2]
    print(sol.dispatchLog([2, 1], 1))  # expected: [0, 1, 0]
    print(sol.dispatchLog([5], 2))  # expected: [0, 0, 0]
    print(sol.dispatchLog([3, 3], 3))  # expected: [0, 1]
