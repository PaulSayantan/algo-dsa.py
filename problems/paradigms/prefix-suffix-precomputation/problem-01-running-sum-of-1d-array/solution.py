"""Running Sum of 1d Array — LeetCode 1480.

Fill in the body of `runningSum`. Do not change the signature.
"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Return the running (prefix) sum of ``nums``.

        Args:
            nums: A list of integers.

        Returns:
            A list ``out`` of the same length where
            ``out[i] == nums[0] + nums[1] + ... + nums[i]``.

        Example:
            >>> Solution().runningSum([1, 2, 3, 4])
            [1, 3, 6, 10]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.runningSum([1, 2, 3, 4]))       # expected: [1, 3, 6, 10]
    print(sol.runningSum([1, 1, 1, 1, 1]))    # expected: [1, 2, 3, 4, 5]
    print(sol.runningSum([3, 1, 2, 10, 1]))   # expected: [3, 4, 6, 16, 17]
