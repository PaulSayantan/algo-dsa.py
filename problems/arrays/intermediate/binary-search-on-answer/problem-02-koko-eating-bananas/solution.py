"""Koko Eating Bananas — LeetCode 875.

Find the minimum constant eating speed k (bananas/hour) so that Koko can
finish all piles within h hours. Solve with Binary Search on Answer over
the speed range [1, max(piles)].
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Return the smallest integer eating speed that finishes within h hours.

        Args:
            piles: piles[i] is the number of bananas in the i-th pile.
            h: The number of hours before the guards return.

        Returns:
            The minimum speed k such that sum(ceil(pile / k)) <= h.

        Example:
            >>> Solution().minEatingSpeed([3, 6, 7, 11], 8)
            4
        """
        # TODO: implement using Binary Search on Answer over [1, max(piles)].
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed([3, 6, 7, 11], 8))            # expected: 4
    print(sol.minEatingSpeed([30, 11, 23, 4, 20], 5))      # expected: 30
    print(sol.minEatingSpeed([30, 11, 23, 4, 20], 6))      # expected: 23
