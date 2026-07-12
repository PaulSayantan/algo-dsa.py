"""Replace the Substring for Balanced String — LeetCode 1234."""
from collections import Counter  # noqa: F401


class Solution:
    def balancedString(self, s: str) -> int:
        # TODO: find the shortest window whose removal leaves every letter count <= n/4
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.balancedString("QWER"))  # expected: 0
    print(sol.balancedString("QQWE"))  # expected: 1
    print(sol.balancedString("QQQW"))  # expected: 2
    print(sol.balancedString("QQQQ"))  # expected: 3
