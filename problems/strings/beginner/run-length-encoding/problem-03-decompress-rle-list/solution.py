"""Decompress Run-Length Encoded List (LeetCode 1313).

Given adjacent (frequency, value) pairs packed into a flat array, expand each
pair into `frequency` copies of `value` and concatenate the results.
"""

from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        """Expand an RLE-encoded (freq, val) pair array.

        Args:
            nums: A flat, even-length array where each pair
                (nums[2*i], nums[2*i+1]) is (frequency, value).

        Returns:
            The decompressed list: for each pair, `frequency` copies of `value`,
            concatenated in order.

        Example:
            >>> Solution().decompressRLElist([1, 2, 3, 4])
            [2, 4, 4, 4]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().decompressRLElist([1, 2, 3, 4]))  # expected: [2, 4, 4, 4]
    print(Solution().decompressRLElist([1, 1, 2, 3]))  # expected: [1, 3, 3]
    print(Solution().decompressRLElist([4, 5]))        # expected: [5, 5, 5, 5]
