"""Open the Lock — LeetCode 752 (BFS with a visited set of hashed states)."""
from typing import List  # noqa: F401


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # TODO: BFS from "0000"; each wheel +/-1 (mod 10); skip deadends and
        # visited states; return the minimum turns (or -1)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))  # expected: 6
    print(sol.openLock(["8888"], "0009"))  # expected: 1
    print(sol.openLock(["0000"], "8888"))  # expected: -1
