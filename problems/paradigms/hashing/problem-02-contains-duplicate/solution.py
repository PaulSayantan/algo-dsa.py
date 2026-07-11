"""Contains Duplicate — empty solution template.

Fill in the body of `containsDuplicate` using a hash set.
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Return True if any value in `nums` appears at least twice.

        Args:
            nums: List of integers to inspect for repeats.

        Returns:
            True if some value occurs more than once, otherwise False.

        Example:
            >>> Solution().containsDuplicate([1, 2, 3, 1])
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))              # expected: True
    print(sol.containsDuplicate([1, 2, 3, 4]))              # expected: False
    print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2]))  # expected: True
