"""LeetCode 136 - Single Number.

Fill in the body of `singleNumber`. Do not use extra data structures if you
want to satisfy the O(1) space requirement.
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Return the element that appears exactly once.

        Every other element in `nums` appears exactly twice.

        Args:
            nums: Non-empty list of integers where all values appear twice
                except one value that appears once.

        Returns:
            The single integer that appears exactly once.

        Example:
            >>> Solution().singleNumber([4, 1, 2, 1, 2])
            4
        """
        # TODO: implement using the XOR trick (constant space, linear time).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2, 2, 1]))        # expected: 1
    print(sol.singleNumber([4, 1, 2, 1, 2]))  # expected: 4
    print(sol.singleNumber([1]))              # expected: 1
