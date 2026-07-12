"""4Sum II — LeetCode 454. Count tuples (i,j,k,l) with the four sums equal to 0."""
from typing import List  # noqa: F401


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int],
                     nums3: List[int], nums4: List[int]) -> int:
        # TODO: count all a+b sums, then look up -(c+d) for every c,d pair
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))  # expected: 2
    print(sol.fourSumCount([0], [0], [0], [0]))  # expected: 1
    print(sol.fourSumCount([1], [-1], [1], [-1]))  # expected: 1
    print(sol.fourSumCount([1, 1], [1, 1], [-2], [0]))  # expected: 4
