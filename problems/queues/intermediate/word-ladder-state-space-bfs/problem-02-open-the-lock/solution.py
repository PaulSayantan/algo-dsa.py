"""Open the Lock — LeetCode 752."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # TODO: state-space BFS over "0000"; neighbors turn one wheel +/-1 mod 10
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))  # expected: 6
    print(sol.openLock(["8888"], "0009"))  # expected: 1
    print(sol.openLock(
        ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"
    ))  # expected: -1
    print(sol.openLock([], "0000"))  # expected: 0
