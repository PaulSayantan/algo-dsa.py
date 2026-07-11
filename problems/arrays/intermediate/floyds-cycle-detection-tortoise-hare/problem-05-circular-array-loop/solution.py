"""LeetCode 457 - Circular Array Loop.

Detect a single-direction cycle of length > 1 in a circular array, ideally in
O(n) time and O(1) extra space.
"""
from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        """Return True if a valid circular cycle (length > 1, one direction) exists.

        Movement rule: from index ``i`` go to ``(i + nums[i]) % n``. A valid
        cycle must have length greater than 1 and use values that are all
        positive or all negative.

        Args:
            nums: A list of non-zero integers describing forward/backward jumps
                on a circular array.

        Returns:
            ``True`` if at least one valid cycle exists, otherwise ``False``.

        Example:
            >>> Solution().circularArrayLoop([2, -1, 1, 2, 2])
            True
            >>> Solution().circularArrayLoop([-1, 2])
            False
        """
        # TODO: implement
        # For each start index, run tortoise & hare over next(i)=(i+nums[i])%n.
        # Break if the direction (sign) changes, and reject self-loops where
        # next(i) == i (length-1 cycle). Optionally mark dead indices to keep
        # the total work O(n).
        pass


if __name__ == "__main__":
    print(Solution().circularArrayLoop([2, -1, 1, 2, 2]))      # Expected: True
    print(Solution().circularArrayLoop([-1, 2]))               # Expected: False
    print(Solution().circularArrayLoop([-2, 1, -1, -2, -2]))   # Expected: False
