"""LeetCode 287 - Find the Duplicate Number.

Find the single repeated value in an array of n + 1 integers in range [1, n],
without modifying the array and using O(1) extra space.
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Return the duplicated value in ``nums``.

        Treat ``nums`` as a functional graph where index ``i`` points to index
        ``nums[i]``. The duplicate value is the entrance of the resulting cycle.

        Args:
            nums: A list of ``n + 1`` integers, each in ``[1, n]``, containing
                exactly one value that repeats (one or more extra times).

        Returns:
            The integer value that appears more than once.

        Example:
            >>> Solution().findDuplicate([1, 3, 4, 2, 2])
            2
            >>> Solution().findDuplicate([3, 1, 3, 4, 2])
            3
        """
        # TODO: implement
        # Phase 1: advance slow = nums[slow], fast = nums[nums[fast]] until they
        #          meet inside the cycle.
        # Phase 2: reset one pointer to the start, advance both by one step until
        #          they meet again -> that value is the cycle entrance / duplicate.
        pass


if __name__ == "__main__":
    print(Solution().findDuplicate([1, 3, 4, 2, 2]))  # Expected: 2
    print(Solution().findDuplicate([3, 1, 3, 4, 2]))  # Expected: 3
    print(Solution().findDuplicate([2, 2, 2, 2, 2]))  # Expected: 2
