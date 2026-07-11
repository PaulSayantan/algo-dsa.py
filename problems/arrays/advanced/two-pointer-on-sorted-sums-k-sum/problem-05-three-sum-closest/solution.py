"""3Sum Closest (LeetCode 16).

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """Return the triplet sum closest to target.

        Args:
            nums: List of integers with at least three elements (unsorted; you may
                sort in place).
            target: The value the triplet sum should be closest to.

        Returns:
            The sum ``nums[i] + nums[j] + nums[k]`` (from three distinct indices)
            whose absolute difference from ``target`` is minimal. Exactly one such
            closest sum is guaranteed.

        Example:
            >>> Solution().threeSumClosest([-1, 2, 1, -4], 1)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))    # expected: 2
    print(sol.threeSumClosest([0, 0, 0], 1))         # expected: 0
    print(sol.threeSumClosest([1, 1, 1, 0], -100))   # expected: 2
