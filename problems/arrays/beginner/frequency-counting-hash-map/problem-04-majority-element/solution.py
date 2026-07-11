"""Majority Element (LeetCode 169).

Return the element that appears more than floor(n / 2) times.
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Return the value that appears more than ``len(nums) // 2`` times.

        The problem guarantees such a majority element always exists.

        Args:
            nums: A non-empty list of integers with a guaranteed majority value.

        Returns:
            The majority element.

        Example:
            >>> Solution().majorityElement([3, 2, 3])
            3
            >>> Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    solver = Solution()

    print(solver.majorityElement([3, 2, 3]))  # expected: 3
    print(solver.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # expected: 2
    print(solver.majorityElement([1]))  # expected: 1
