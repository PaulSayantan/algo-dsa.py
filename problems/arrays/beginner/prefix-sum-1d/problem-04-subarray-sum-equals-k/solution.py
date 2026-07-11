from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """Count the contiguous subarrays whose elements sum to k.

        Args:
            nums: A list of integers (may include negatives and zeros).
            k: The target subarray sum.

        Returns:
            The number of contiguous, non-empty subarrays summing to k.

        Example:
            >>> Solution().subarraySum([1, 1, 1], 2)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    # Sample run — expected outputs shown as comments, not asserted.
    print(Solution().subarraySum([1, 1, 1], 2))   # expected: 2
    print(Solution().subarraySum([1, 2, 3], 3))   # expected: 2
    print(Solution().subarraySum([1, -1, 0], 0))  # expected: 3
