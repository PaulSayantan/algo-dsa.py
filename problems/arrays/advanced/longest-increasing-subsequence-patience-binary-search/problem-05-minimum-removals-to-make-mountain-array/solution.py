"""Minimum Number of Removals to Make Mountain Array (LeetCode 1671).

Empty solution template — fill in the logic yourself.
"""
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        """Return the minimum number of removals to turn nums into a mountain.

        A mountain array strictly increases to a single peak (not at either
        end) and then strictly decreases.

        Args:
            nums: The input integer array (length >= 3). A valid answer is
                guaranteed to exist.

        Returns:
            The minimum count of elements to remove so the remainder is a
            mountain array.

        Example:
            >>> Solution().minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1])
            3
            >>> Solution().minimumMountainRemovals([1, 3, 1])
            0
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumMountainRemovals([1, 3, 1]))                 # expected: 0
    print(sol.minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1]))  # expected: 3
    print(sol.minimumMountainRemovals([1, 2, 1, 2, 1]))           # expected: 2
