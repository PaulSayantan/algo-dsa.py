"""Beautiful Arrangement (LeetCode 526).

Count the number of beautiful arrangements of the integers 1..n.

Solve this with Bitmask DP: let `mask` encode the set of numbers already
placed. The number of bits set in `mask` equals how many positions are filled,
so the next position to fill is `popcount(mask) + 1`.
"""

from __future__ import annotations


class Solution:
    def countArrangement(self, n: int) -> int:
        """Return the number of beautiful arrangements of 1..n.

        Args:
            n: The number of integers to arrange (1 <= n <= 15). Numbers
                1 through n are placed into positions 1 through n.

        Returns:
            The count of permutations `perm` (1-indexed) such that for every
            position i, either `perm[i] % i == 0` or `i % perm[i] == 0`.

        Example:
            >>> Solution().countArrangement(2)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countArrangement(2))  # expected: 2
    print(sol.countArrangement(3))  # expected: 3
    print(sol.countArrangement(1))  # expected: 1
