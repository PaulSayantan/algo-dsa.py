"""First unique character in a string — return its index (or -1)."""
from collections import deque  # noqa: F401


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # TODO: counts + a deque of candidate indices; front is the first unique
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("leetcode"))  # expected: 0
    print(sol.firstUniqChar("loveleetcode"))  # expected: 2
    print(sol.firstUniqChar("aabb"))  # expected: -1
    print(sol.firstUniqChar("z"))  # expected: 0
    print(sol.firstUniqChar(""))  # expected: -1
