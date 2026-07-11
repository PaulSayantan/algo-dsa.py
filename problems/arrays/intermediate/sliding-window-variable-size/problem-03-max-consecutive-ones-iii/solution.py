"""Max Consecutive Ones III — empty solution template.

Fill in the body of `longestOnes`. Do not hard-code answers.
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """Return the longest run of 1s achievable by flipping at most k zeros.

        Args:
            nums: A binary list containing only 0s and 1s.
            k: The maximum number of 0s allowed to be flipped to 1.

        Returns:
            The length of the longest contiguous subarray containing at most k
            zeros.

        Example:
            >>> Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
            6
        """
        # TODO: implement using a variable-size sliding window
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))  # expected: 6
    print(sol.longestOnes(
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
    ))  # expected: 10
    print(sol.longestOnes([0, 0, 0, 0], 0))  # expected: 0
