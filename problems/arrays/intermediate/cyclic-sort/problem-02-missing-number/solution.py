"""Missing Number (LeetCode 268).

Fill in the body yourself. Do not add a working implementation elsewhere.
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Return the single number missing from the range [0, n].

        Args:
            nums: A list of n distinct integers, each in [0, n]. Exactly one
                value from that range is absent. May be mutated in place.

        Returns:
            The missing integer in [0, n].

        Example:
            >>> Solution().missingNumber([3, 0, 1])
            2
        """
        # TODO: implement using cyclic sort over the [0..n] range
        pass


if __name__ == "__main__":
    print(Solution().missingNumber([3, 0, 1]))                        # expected: 2
    print(Solution().missingNumber([0, 1]))                           # expected: 2
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))      # expected: 8
