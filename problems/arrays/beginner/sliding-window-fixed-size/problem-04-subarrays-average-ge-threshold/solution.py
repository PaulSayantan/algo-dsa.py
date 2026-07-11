from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """Count length-``k`` subarrays whose average is at least ``threshold``.

        Args:
            arr: A list of positive integers.
            k: The fixed window size, with ``1 <= k <= len(arr)``.
            threshold: The minimum average a window must reach to be counted.

        Returns:
            The number of contiguous subarrays of length exactly ``k`` whose
            average value is greater than or equal to ``threshold``.

        Example:
            >>> Solution().numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4)
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))               # expected: 3
    print(sol.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))    # expected: 6
    print(sol.numOfSubarrays([1, 1, 1, 1, 1], 2, 3))                         # expected: 0
