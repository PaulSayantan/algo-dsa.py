"""Two Sum II - Input Array Is Sorted (LeetCode 167).

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Return the 1-based indices of the two numbers that sum to target.

        The input array ``numbers`` is sorted in non-decreasing order and is
        guaranteed to contain exactly one valid pair. Use only O(1) extra space.

        Args:
            numbers: 1-indexed, non-decreasing sorted list of integers.
            target: The required sum of the two chosen numbers.

        Returns:
            A list ``[index1, index2]`` of 1-based indices with
            ``index1 < index2`` such that
            ``numbers[index1 - 1] + numbers[index2 - 1] == target``.

        Example:
            >>> Solution().twoSum([2, 7, 11, 15], 9)
            [1, 2]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # expected: [1, 2]
    print(sol.twoSum([2, 3, 4], 6))       # expected: [1, 3]
    print(sol.twoSum([-1, 0], -1))        # expected: [1, 2]
