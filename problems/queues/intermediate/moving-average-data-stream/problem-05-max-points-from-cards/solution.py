"""Maximum Points You Can Obtain from Cards — LeetCode 1423."""
from typing import List  # noqa: F401


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # TODO: total minus the min-sum contiguous window of size n-k
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxScore([1, 2, 3, 4, 5, 6, 1], 3))  # expected: 12
    print(sol.maxScore([2, 2, 2], 2))  # expected: 4
    print(sol.maxScore([9, 7, 7, 9, 7, 7, 9], 7))  # expected: 55
    print(sol.maxScore([100], 1))  # expected: 100
