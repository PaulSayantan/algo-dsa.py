"""LeetCode 710 - Random Pick with Blacklist.

Pick a uniformly random integer in [0, n-1] that is not blacklisted.
Use a Fisher-Yates-style remap into a hash map so pick() is O(1).
"""
from typing import List


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        """Initialize with the range size and the blacklisted values.

        Args:
            n: Values are drawn from [0, n - 1].
            blacklist: Unique integers in [0, n - 1] that must never be returned.
        """
        # TODO: implement
        # Hint: let m = n - len(blacklist). Every pick will draw from [0, m).
        # Build a map that redirects each blacklisted index < m to a distinct
        # allowed index in [m, n).
        pass

    def pick(self) -> int:
        """Return a uniformly random non-blacklisted integer in [0, n - 1].

        Returns:
            An allowed integer; each allowed value is equally likely.

        Example:
            >>> obj = Solution(7, [2, 3, 5])
            >>> obj.pick() in {0, 1, 4, 6}
            True
        """
        # TODO: implement
        # Hint: draw x = random.randrange(m); return the remap of x if present,
        # else x.
        pass


if __name__ == "__main__":
    obj = Solution(7, [2, 3, 5])
    print(obj.pick() in {0, 1, 4, 6})   # expected: True
    print(obj.pick() in {0, 1, 4, 6})   # expected: True

    obj2 = Solution(4, [0])
    print(obj2.pick() in {1, 2, 3})     # expected: True
