"""Return the first n positive integers whose digits are only 1 and 2, using a queue."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def firstNumbers(self, n: int) -> List[int]:
        # TODO: BFS with a queue seeded with "1","2"; dequeue s, record int(s), enqueue s+"1", s+"2"
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstNumbers(7))  # expected: [1, 2, 11, 12, 21, 22, 111]
    print(sol.firstNumbers(1))  # expected: [1]
    print(sol.firstNumbers(3))  # expected: [1, 2, 11]
    print(sol.firstNumbers(10))  # expected: [1, 2, 11, 12, 21, 22, 111, 112, 121, 122]
