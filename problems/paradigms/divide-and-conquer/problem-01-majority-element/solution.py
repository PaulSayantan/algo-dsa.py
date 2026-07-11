"""Majority Element — LeetCode 169.

Empty solution template. Fill in the body yourself using Divide and Conquer.
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Return the element that appears more than floor(n / 2) times.

        A majority element is guaranteed to exist. Solve it with Divide and
        Conquer: find the majority of each half, then resolve the two
        candidates by counting occurrences over the current range.

        Args:
            nums: List of integers containing a guaranteed majority element.

        Returns:
            The majority element of nums.

        Example:
            >>> Solution().majorityElement([3, 2, 3])
            3
            >>> Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3, 2, 3]))                    # expected: 3
    print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))        # expected: 2
    print(sol.majorityElement([7]))                          # expected: 7
