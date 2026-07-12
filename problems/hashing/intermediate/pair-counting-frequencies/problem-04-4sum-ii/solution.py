"""4Sum II — LeetCode 454."""
from typing import List  # noqa: F401
from collections import Counter  # noqa: F401


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # TODO: hash all pair sums of the first two arrays; look up negatives from the last two
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))  # expected: 2
    print(sol.fourSumCount([0], [0], [0], [0]))  # expected: 1
    print(sol.fourSumCount([1, 1], [1, 1], [-2, -2], [0, 0]))  # expected: 16
    print(sol.fourSumCount([1], [-1], [1], [-1]))  # expected: 1
