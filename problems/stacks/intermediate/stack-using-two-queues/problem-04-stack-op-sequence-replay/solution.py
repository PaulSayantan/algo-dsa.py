"""Replay a sequence of stack operations using a queue-backed stack."""
from typing import List, Tuple, Union
from collections import deque  # noqa: F401


class Solution:
    def simulateStack(self, ops: List[Tuple]) -> List[Union[int, bool]]:
        # TODO: back the stack with a queue (rotate on push); dispatch on each op
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.simulateStack([("push", 1), ("push", 2), ("top",), ("pop",), ("top",), ("empty",), ("pop",), ("empty",)]))  # expected: [2, 2, 1, False, 1, True]
    print(sol.simulateStack([("push", 9), ("empty",)]))  # expected: [False]
    print(sol.simulateStack([("empty",)]))  # expected: [True]
    print(sol.simulateStack([("push", 4), ("push", 5), ("push", 6), ("pop",), ("pop",), ("top",)]))  # expected: [6, 5, 4]
