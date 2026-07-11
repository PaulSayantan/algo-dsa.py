"""Number of Ways to Wear Different Hats to Each Other (LeetCode 1434).

Count the assignments of one liked hat per person with no shared hat type,
modulo 1e9 + 7.

Solve this with Bitmask DP. Because there are at most 10 people but up to 40
hats, the mask ranges over PEOPLE: `dp[mask]` = number of ways to have given
hats (from those processed so far) to exactly the set of people in `mask`.
Iterate hat types 1..40 one at a time; each hat is either unused or worn by one
of the people who like it and is not yet covered.
"""

from __future__ import annotations

from typing import List


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        """Return the number of valid hat assignments modulo 1e9 + 7.

        Args:
            hats: hats[i] is the list of distinct hat types (1..40) that
                person i is willing to wear. 1 <= len(hats) <= 10.

        Returns:
            The count, modulo 10**9 + 7, of ways to assign each person exactly
            one liked hat so that no hat type is worn by two people.

        Example:
            >>> Solution().numberWays([[3, 5, 1], [3, 5]])
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberWays([[3, 4], [4, 5], [5]]))       # expected: 1
    print(sol.numberWays([[3, 5, 1], [3, 5]]))          # expected: 4
    print(sol.numberWays(
        [[1, 2, 3], [2, 3, 5, 6], [1, 3, 7, 9], [1, 8, 9], [2, 5, 7]]
    ))                                                  # expected: 111
