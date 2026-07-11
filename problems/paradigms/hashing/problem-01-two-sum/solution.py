"""Two Sum — empty solution template.

Fill in the body of `twoSum` using a hash map.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Return the indices of the two numbers in `nums` that sum to `target`.

        Args:
            nums: List of integers. Exactly one valid pair is guaranteed.
            target: The desired sum of the two chosen numbers.

        Returns:
            A list of two distinct indices [i, j] such that
            nums[i] + nums[j] == target. Order does not matter.

        Example:
            >>> Solution().twoSum([2, 7, 11, 15], 9)
            [0, 1]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # expected: [0, 1]
    print(sol.twoSum([3, 2, 4], 6))       # expected: [1, 2]
    print(sol.twoSum([3, 3], 6))          # expected: [0, 1]
