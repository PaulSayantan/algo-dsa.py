from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """Return the length of the longest subarray with equal 0s and 1s.

        Args:
            nums: A binary list containing only 0s and 1s.

        Returns:
            The maximum length of a contiguous subarray that has an equal count
            of 0s and 1s, or 0 if none exists.

        Example:
            >>> Solution().findMaxLength([0, 1, 0])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    # Sample run — expected outputs shown as comments, not asserted.
    print(Solution().findMaxLength([0, 1]))                       # expected: 2
    print(Solution().findMaxLength([0, 1, 0]))                    # expected: 2
    print(Solution().findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))     # expected: 6
