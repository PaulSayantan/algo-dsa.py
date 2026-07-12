"""Maximum Number of Balloons — LeetCode 1189."""
from collections import Counter  # noqa: F401


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # TODO: for each letter of "balloon", divide its supply by its demand; take the min
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxNumberOfBalloons("nlaebolko"))  # expected: 1
    print(sol.maxNumberOfBalloons("loonbalxballpoon"))  # expected: 2
    print(sol.maxNumberOfBalloons("leetcode"))  # expected: 0
