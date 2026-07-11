"""Jump Game — LeetCode 55.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Return whether the last index is reachable from index 0.

        From index i you may jump to any index j with i < j <= i + nums[i].

        Args:
            nums: Non-negative jump lengths; nums[i] is the max jump from index i.

        Returns:
            True if the last index can be reached, otherwise False.

        Example:
            >>> Solution().canJump([2, 3, 1, 1, 4])
            True
            >>> Solution().canJump([3, 2, 1, 0, 4])
            False
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([2, 3, 1, 1, 4]))  # expected: True
    print(sol.canJump([3, 2, 1, 0, 4]))  # expected: False
    print(sol.canJump([0]))              # expected: True
