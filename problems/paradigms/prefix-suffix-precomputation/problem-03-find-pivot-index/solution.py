"""Find Pivot Index — LeetCode 724.

Fill in the body of `pivotIndex`. Do not change the signature.
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """Return the leftmost index where the left sum equals the right sum.

        The left sum is the sum of all elements strictly before the index; the
        right sum is the sum of all elements strictly after it. Elements at the
        edges have an empty (zero) sum on the missing side.

        Args:
            nums: A list of integers.

        Returns:
            The leftmost pivot index, or ``-1`` if none exists.

        Example:
            >>> Solution().pivotIndex([1, 7, 3, 6, 5, 6])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.pivotIndex([1, 7, 3, 6, 5, 6]))  # expected: 3
    print(sol.pivotIndex([1, 2, 3]))           # expected: -1
    print(sol.pivotIndex([2, 1, -1]))          # expected: 0
