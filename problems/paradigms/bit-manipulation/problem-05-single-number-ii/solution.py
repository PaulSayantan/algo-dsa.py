"""LeetCode 137 - Single Number II.

Every element appears three times except one, which appears once. Fill in the
body of `singleNumber` using O(1) space (no hash map / Counter).
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Return the element that appears exactly once.

        Every other element in `nums` appears exactly three times.

        Args:
            nums: Non-empty list of integers where all values appear three
                times except one value that appears once.

        Returns:
            The single integer that appears exactly once.

        Example:
            >>> Solution().singleNumber([0, 1, 0, 1, 0, 1, 99])
            99
        """
        # TODO: for each of 32 bit positions, sum the bits and take mod 3;
        # or use the two-mask (ones/twos) finite-state-machine trick.
        # Remember to handle negative numbers / 32-bit sign wraparound.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2, 2, 3, 2]))                                # expected: 3
    print(sol.singleNumber([0, 1, 0, 1, 0, 1, 99]))                      # expected: 99
    print(sol.singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -2, -4]))       # expected: -4
