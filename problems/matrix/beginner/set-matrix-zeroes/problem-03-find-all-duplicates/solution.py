"""LeetCode 442 — Find All Duplicates in an Array.

Fill in the body of `findDuplicates`. Aim for O(n) time and O(1) extra space by
sign-marking the slot each value points at.
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """Return every value that appears exactly twice in ``nums``.

        Each value ``v`` is in ``[1, n]`` and maps to index ``v - 1``. Use the
        sign of ``nums[v - 1]`` as a "visited" flag: the first visit negates the
        slot, and a second visit (slot already negative) proves ``v`` is a
        duplicate. Read magnitudes with ``abs()`` so flipped signs do not
        corrupt the index computation.

        Args:
            nums: A list of ``n`` integers in ``[1, n]``; each appears once or
                  twice.

        Returns:
            A list of the integers that appear twice. Order is not significant.

        Example:
            >>> Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
            [2, 3]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # expected: [2, 3]
    print(sol.findDuplicates([1, 1, 2]))                 # expected: [1]
    print(sol.findDuplicates([1]))                       # expected: []
