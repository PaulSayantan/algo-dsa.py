from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        """Return the maximum achievable minimum pairwise distance for ``m`` balls.

        Place ``m`` balls into ``m`` distinct baskets so that the smallest gap
        between any two chosen baskets is as large as possible, and return that
        largest-possible smallest gap.

        Args:
            position: Distinct basket positions (unsorted is fine).
            m: Number of balls to place (``2 <= m <= len(position)``).

        Returns:
            The maximized minimum pairwise distance.

        Example:
            >>> Solution().maxDistance([1, 2, 3, 4, 7], 3)
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDistance([1, 2, 3, 4, 7], 3))              # expected: 3
    print(sol.maxDistance([5, 4, 3, 2, 1, 1000000000], 2))  # expected: 999999999
