from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Return the minimum integer eating speed to finish all piles in ``h`` hours.

        At speed ``k``, clearing a pile of size ``p`` takes ``ceil(p / k)`` hours.
        Find the smallest ``k`` whose total hours over all piles is ``<= h``.

        Args:
            piles: List of pile sizes; ``piles[i]`` bananas in the i-th pile.
            h: The number of hours available (``h >= len(piles)``).

        Returns:
            The minimum integer speed ``k >= 1`` that lets Koko finish in time.

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
