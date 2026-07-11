"""LeetCode 448 — Find All Numbers Disappeared in an Array.

Fill in the body of `findDisappearedNumbers`. The goal is an in-place,
O(1) extra-space solution that uses the array itself as a set of flags by
negating the slot each value points at.
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """Return every integer in [1, n] that is absent from ``nums``.

        Each value ``v`` in ``nums`` lies in ``[1, n]`` and therefore maps to a
        valid index ``v - 1``. Mark visited indices in place (e.g. by negating
        the value stored there) so no extra data structure is required, then
        collect the indices that were never marked.

        Args:
            nums: A list of ``n`` integers, each in the range ``[1, n]``.
                  Values may repeat and some may be missing.

        Returns:
            A list of the integers in ``[1, n]`` that do not appear in ``nums``.
            Order of the returned values is not significant.

        Example:
            >>> Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
            [5, 6]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # expected: [5, 6]
    print(sol.findDisappearedNumbers([1, 1]))                    # expected: [2]
    print(sol.findDisappearedNumbers([1, 2, 3, 4]))              # expected: []
