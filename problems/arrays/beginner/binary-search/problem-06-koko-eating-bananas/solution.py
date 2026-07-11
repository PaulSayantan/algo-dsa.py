"""LeetCode 875 - Koko Eating Bananas.

Find the minimum integer eating speed k such that all piles can be eaten within
h hours. This is a "binary search on the answer" problem.
"""
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Return the minimum eating speed to finish all piles within `h` hours.

        Eating a pile of size p at speed k takes ceil(p / k) hours (Koko cannot
        combine leftovers from different piles in the same hour).

        Args:
            piles: The number of bananas in each pile.
            h: The number of hours available (h >= len(piles)).

        Returns:
            The smallest integer speed k (bananas per hour) that lets Koko eat
            every pile within `h` hours.

        Example:
            >>> Solution().minEatingSpeed([3, 6, 7, 11], 8)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed([3, 6, 7, 11], 8))          # expected: 4
    print(sol.minEatingSpeed([30, 11, 23, 4, 20], 5))    # expected: 30
    print(sol.minEatingSpeed([30, 11, 23, 4, 20], 6))    # expected: 23
