from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """Return the length of the shortest subarray that, once sorted, sorts all.

        Args:
            nums: A list of integers.

        Returns:
            The length of the shortest continuous subarray that must be sorted
            so the entire array becomes non-decreasing; 0 if already sorted.

        Example:
            >>> Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
            5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))  # expected: 5
    print(sol.findUnsortedSubarray([1, 2, 3, 4]))             # expected: 0
    print(sol.findUnsortedSubarray([1, 3, 5, 4, 2]))          # expected: 4
