"""LeetCode 41 — First Missing Positive.

Fill in the body of `firstMissingPositive`. Aim for O(n) time and O(1) extra
space by placing each value into its "home" index (cyclic sort) inside the
array itself.
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """Return the smallest positive integer missing from ``nums``.

        The answer must lie in ``[1, n + 1]`` where ``n = len(nums)``, so the
        array can act as an in-place hash table: value ``v`` belongs at index
        ``v - 1``. Place each in-range value into its home slot by swapping,
        ignoring values that are <= 0 or > n, then the first index whose value
        is not ``index + 1`` gives the answer (``n + 1`` if all slots match).

        Args:
            nums: A list of arbitrary integers (may include negatives, zeros,
                  and values larger than the length). Modified in place.

        Returns:
            The smallest positive integer not present in ``nums``.

        Example:
            >>> Solution().firstMissingPositive([3, 4, -1, 1])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstMissingPositive([1, 2, 0]))            # expected: 3
    print(sol.firstMissingPositive([3, 4, -1, 1]))        # expected: 2
    print(sol.firstMissingPositive([7, 8, 9, 11, 12]))    # expected: 1
