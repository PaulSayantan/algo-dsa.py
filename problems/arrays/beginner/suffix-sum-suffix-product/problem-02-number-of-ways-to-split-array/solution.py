from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """Count valid split indices i (0 <= i < n - 1).

        A split at index i is valid when the sum of nums[0..i] is greater than
        or equal to the sum of nums[i+1..n-1].

        Args:
            nums: A list of integers (may contain negatives).

        Returns:
            The number of indices i with 0 <= i < len(nums) - 1 such that the
            left-part sum is >= the right-part sum.

        Example:
            >>> Solution().waysToSplitArray([10, 4, -8, 7])
            2
        """
        # TODO: implement (right side is a suffix sum = total - running left sum)
        pass


if __name__ == "__main__":
    # Sample runs — expected outputs shown as comments, not asserted.
    sol = Solution()
    print(sol.waysToSplitArray([10, 4, -8, 7]))  # expected: 2
    print(sol.waysToSplitArray([2, 3, 1, 0]))    # expected: 2
