"""First Missing Positive (LeetCode 41).

Fill in the body yourself. Do not add a working implementation elsewhere.
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """Return the smallest positive integer not present in nums.

        Args:
            nums: An arbitrary list of integers (may contain negatives, zeros,
                duplicates, and values outside [1, n]). May be mutated in place.

        Returns:
            The smallest positive integer absent from nums, always in
            [1, len(nums) + 1].

        Example:
            >>> Solution().firstMissingPositive([3, 4, -1, 1])
            2
        """
        # TODO: implement using cyclic sort, placing only values in [1, n]
        pass


if __name__ == "__main__":
    print(Solution().firstMissingPositive([1, 2, 0]))            # expected: 3
    print(Solution().firstMissingPositive([3, 4, -1, 1]))        # expected: 2
    print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))    # expected: 1
