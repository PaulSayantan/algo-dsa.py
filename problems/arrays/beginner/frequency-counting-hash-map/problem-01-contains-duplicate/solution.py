"""Contains Duplicate (LeetCode 217).

Determine whether any value appears at least twice in the array.
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Return True if any value in ``nums`` appears at least twice.

        Args:
            nums: A list of integers that may contain duplicates.

        Returns:
            True if at least one value occurs more than once, otherwise False.

        Example:
            >>> Solution().containsDuplicate([1, 2, 3, 1])
            True
            >>> Solution().containsDuplicate([1, 2, 3, 4])
            False
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    solver = Solution()

    print(solver.containsDuplicate([1, 2, 3, 1]))  # expected: True
    print(solver.containsDuplicate([1, 2, 3, 4]))  # expected: False
    print(solver.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # expected: True
