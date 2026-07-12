"""Count substrings with exactly K distinct characters."""
from collections import defaultdict  # noqa: F401


class Solution:
    def countExactlyKDistinct(self, s: str, k: int) -> int:
        # TODO: exactly K = atMost(K) - atMost(K-1) over characters
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countExactlyKDistinct("pqpqs", 2))  # expected: 7
    print(sol.countExactlyKDistinct("aabab", 3))  # expected: 0
    print(sol.countExactlyKDistinct("abc", 2))  # expected: 2
    print(sol.countExactlyKDistinct("aaaa", 1))  # expected: 10
