from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Return the (inclusive) running/prefix sum of the input array.

        Args:
            nums: A list of integers.

        Returns:
            A new list where result[i] equals nums[0] + nums[1] + ... + nums[i].

        Example:
            >>> Solution().runningSum([1, 2, 3, 4])
            [1, 3, 6, 10]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    # Sample run — expected output shown as a comment, not asserted.
    print(Solution().runningSum([1, 2, 3, 4]))       # expected: [1, 3, 6, 10]
    print(Solution().runningSum([1, 1, 1, 1, 1]))    # expected: [1, 2, 3, 4, 5]
    print(Solution().runningSum([3, 1, 2, 10, 1]))   # expected: [3, 4, 6, 16, 17]
