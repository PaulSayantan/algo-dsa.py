"""LeetCode 338 - Counting Bits.

Fill in the body of `countBits`. Aim for a single O(n) pass using a DP
recurrence rather than an independent popcount per number.
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """Return popcounts for every integer in the range [0, n].

        Args:
            n: A non-negative integer upper bound.

        Returns:
            A list `ans` of length n + 1 where ans[i] is the number of set
            bits in the binary representation of i.

        Example:
            >>> Solution().countBits(5)
            [0, 1, 1, 2, 1, 2]
        """
        # TODO: implement using a DP recurrence, e.g.
        #   ans[i] = ans[i >> 1] + (i & 1)
        # or
        #   ans[i] = ans[i & (i - 1)] + 1
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(2))  # expected: [0, 1, 1]
    print(sol.countBits(5))  # expected: [0, 1, 1, 2, 1, 2]
    print(sol.countBits(0))  # expected: [0]
