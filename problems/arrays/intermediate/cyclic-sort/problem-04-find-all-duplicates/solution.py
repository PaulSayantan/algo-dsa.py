"""Find All Duplicates in an Array (LeetCode 442).

Fill in the body yourself. Do not add a working implementation elsewhere.
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """Return every value in [1, n] that appears exactly twice in nums.

        Args:
            nums: A list of n integers, each in [1, n]; every value appears
                once or twice. May be mutated in place.

        Returns:
            A list of the values appearing twice, in any order.

        Example:
            >>> Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
            [2, 3]
        """
        # TODO: implement using cyclic sort (place value v at index v - 1)
        pass


if __name__ == "__main__":
    print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # expected: [2, 3]
    print(Solution().findDuplicates([1, 1, 2]))                 # expected: [1]
    print(Solution().findDuplicates([1, 2, 3, 4]))              # expected: []
