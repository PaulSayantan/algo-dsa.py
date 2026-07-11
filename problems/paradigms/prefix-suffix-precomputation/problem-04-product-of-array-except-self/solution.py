"""Product of Array Except Self — LeetCode 238.

Fill in the body of `productExceptSelf`. Do not change the signature.
Constraints: O(n) time, and no division operation.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Return an array where answer[i] is the product of all nums except nums[i].

        Must run in O(n) time and must not use division.

        Args:
            nums: A list of integers with length >= 2.

        Returns:
            A list ``answer`` of the same length where ``answer[i]`` equals the
            product of every element of ``nums`` other than ``nums[i]``.

        Example:
            >>> Solution().productExceptSelf([1, 2, 3, 4])
            [24, 12, 8, 6]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))          # expected: [24, 12, 8, 6]
    print(sol.productExceptSelf([-1, 1, 0, -3, 3]))     # expected: [0, 0, 9, 0, 0]
