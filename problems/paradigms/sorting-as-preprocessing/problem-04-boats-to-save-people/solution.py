"""Boats to Save People — LeetCode 881.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """Return the minimum number of boats to carry everyone.

        Each boat holds at most two people whose combined weight is <= limit.

        Args:
            people: Weights of the people to transport.
            limit: Maximum total weight a single boat can carry.

        Returns:
            The minimum number of boats required.

        Example:
            >>> Solution().numRescueBoats([1, 2], 3)
            1
            >>> Solution().numRescueBoats([3, 2, 2, 1], 3)
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numRescueBoats([1, 2], 3))          # expected: 1
    print(sol.numRescueBoats([3, 2, 2, 1], 3))    # expected: 3
    print(sol.numRescueBoats([3, 5, 3, 4], 5))    # expected: 4
