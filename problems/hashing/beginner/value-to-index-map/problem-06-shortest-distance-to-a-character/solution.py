"""Shortest Distance to a Character — LeetCode 821. Distance to nearest c per index."""
from typing import List  # noqa: F401


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # TODO: track the most recent index of c on a left pass, then a right pass
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestToChar("loveleetcode", "e"))  # expected: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    print(sol.shortestToChar("aaab", "b"))  # expected: [3, 2, 1, 0]
    print(sol.shortestToChar("b", "b"))  # expected: [0]
    print(sol.shortestToChar("baa", "b"))  # expected: [0, 1, 2]
