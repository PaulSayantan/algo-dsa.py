"""Generate the first n binary numbers ("1","10","11",...) using a queue."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def generate(self, n: int) -> List[str]:
        # TODO: BFS with a queue seeded with "1"; each dequeue emits s and enqueues s+"0", s+"1"
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(5))  # expected: ['1', '10', '11', '100', '101']
    print(sol.generate(1))  # expected: ['1']
    print(sol.generate(0))  # expected: []
