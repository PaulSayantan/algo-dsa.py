"""Static Range Sum Query via a Sqrt Tree.

Fill in the implementation. Do NOT hard-code answers.
"""
from typing import List


class RangeSum:
    """O(1) range-sum queries on a static array using a Sqrt Tree (op = addition).

    Example:
        >>> rs = RangeSum([1, 3, 5, 7, 9, 11])
        >>> rs.query(1, 3)   # 3 + 5 + 7
        15
        >>> rs.query(0, 5)
        36
    """

    def __init__(self, nums: List[int]) -> None:
        """Preprocess `nums` so that range sums can be answered in O(1).

        Args:
            nums: The static integer array. Length n, 1 <= n <= 1e5.

        Build target: O(n log log n) time and space (a Sqrt Tree). A prefix-sum
        array is also acceptable for addition, but the goal here is to practice
        the Sqrt Tree layout: per-block prefix, per-block suffix, and the
        between-blocks table.
        """
        # TODO: implement
        pass

    def query(self, l: int, r: int) -> int:
        """Return the sum of nums[l..r] inclusive.

        Args:
            l: Left index, 0 <= l <= r.
            r: Right index, r < n.

        Returns:
            The sum nums[l] + ... + nums[r].
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    rs = RangeSum([1, 3, 5, 7, 9, 11])
    print(rs.query(1, 3))   # expected: 15
    print(rs.query(0, 5))   # expected: 36

    rs2 = RangeSum([-2, 0, 3, -5, 2, -1])
    print(rs2.query(2, 5))  # expected: -1
    print(rs2.query(0, 2))  # expected: 1
