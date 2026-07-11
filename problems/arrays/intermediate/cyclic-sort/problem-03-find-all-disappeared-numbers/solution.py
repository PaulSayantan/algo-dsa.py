"""Find All Numbers Disappeared in an Array (LeetCode 448).

Fill in the body yourself. Do not add a working implementation elsewhere.
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """Return every value in [1, n] that does not appear in nums.

        Args:
            nums: A list of n integers, each in [1, n]; some values repeat and
                some are absent. May be mutated in place.

        Returns:
            A list of the integers in [1, n] missing from nums, in any order.

        Example:
            >>> Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
            [5, 6]
        """
        # TODO: implement using cyclic sort (place value v at index v - 1)
        pass


if __name__ == "__main__":
    print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # expected: [5, 6]
    print(Solution().findDisappearedNumbers([1, 1]))                    # expected: [2]
    print(Solution().findDisappearedNumbers([2, 2]))                    # expected: [1]
