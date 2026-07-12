"""Round-robin print spooler: return the order in which jobs finish printing."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def printOrder(self, jobs: List[list], quantum: int) -> List[int]:
        # TODO: FIFO queue of [job_id, pages_left]; each turn prints up to `quantum`
        # pages, then re-enqueues the job if pages remain, else records it as finished
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.printOrder([[1, 3], [2, 1], [3, 2]], 1))  # expected: [2, 3, 1]
    print(sol.printOrder([[1, 2], [2, 2]], 2))  # expected: [1, 2]
    print(sol.printOrder([[10, 1]], 5))  # expected: [10]
