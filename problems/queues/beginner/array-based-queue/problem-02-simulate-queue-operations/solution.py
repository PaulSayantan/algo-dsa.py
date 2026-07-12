"""Simulate a FIFO queue over an operation list; return the result of each query."""
from typing import List  # noqa: F401


class Solution:
    def runOps(self, ops: List[list]) -> List[object]:
        # TODO: process ["enqueue", v] / ["dequeue"] / ["front"] / ["empty"]
        # and append a result for every query op (dequeue/front/empty)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.runOps([["empty"], ["enqueue", 5], ["front"], ["enqueue", 6], ["dequeue"], ["front"], ["empty"]]))  # expected: [True, 5, 5, 6, False]
    print(sol.runOps([["enqueue", 1], ["enqueue", 2], ["dequeue"], ["dequeue"], ["empty"]]))  # expected: [1, 2, True]
