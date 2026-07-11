from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """Count contiguous subarrays whose sum is divisible by k.

        Args:
            nums: A list of integers (may include negatives).
            k: The divisor (k >= 2).

        Returns:
            The number of non-empty contiguous subarrays whose sum is
            divisible by k.

        Example:
            >>> Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5)
            7
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    # Sample run — expected outputs shown as comments, not asserted.
    print(Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5))  # expected: 7
    print(Solution().subarraysDivByK([5], 9))                    # expected: 0
    print(Solution().subarraysDivByK([1, 2, 3], 3))              # expected: 3
