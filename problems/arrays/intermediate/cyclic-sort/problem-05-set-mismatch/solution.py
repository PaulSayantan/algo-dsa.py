"""Set Mismatch (LeetCode 645).

Fill in the body yourself. Do not add a working implementation elsewhere.
"""

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """Return [duplicated, missing] for a corrupted 1..n set.

        Args:
            nums: A list of n integers in [1, n] where exactly one value is
                duplicated and exactly one value is missing. May be mutated
                in place.

        Returns:
            A two-element list: the duplicated value followed by the missing
            value.

        Example:
            >>> Solution().findErrorNums([1, 2, 2, 4])
            [2, 3]
        """
        # TODO: implement using cyclic sort (place value v at index v - 1)
        pass


if __name__ == "__main__":
    print(Solution().findErrorNums([1, 2, 2, 4]))          # expected: [2, 3]
    print(Solution().findErrorNums([1, 1]))                # expected: [1, 2]
    print(Solution().findErrorNums([3, 2, 3, 4, 6, 5]))    # expected: [3, 1]
