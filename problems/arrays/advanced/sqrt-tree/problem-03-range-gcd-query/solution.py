"""Range GCD Query via a Sqrt Tree (op = gcd).

Fill in the implementation. Do NOT hard-code answers.
"""
from typing import List


class RangeGCD:
    """O(1) range-gcd queries on a static array using a Sqrt Tree.

    Example:
        >>> rg = RangeGCD([12, 18, 6, 9, 24, 36])
        >>> rg.query(0, 2)
        6
        >>> rg.query(3, 5)
        3
    """

    def __init__(self, nums: List[int]) -> None:
        """Preprocess `nums` so range gcds can be answered in O(1).

        Args:
            nums: Static array of positive integers, length n (1 <= n <= 1e5).

        Build target: O(n log log n) time and space. Use op = math.gcd. gcd is
        associative but NOT invertible, so a prefix-gcd array cannot answer
        arbitrary ranges — the Sqrt Tree (or a sparse table) is required.
        """
        # TODO: implement
        pass

    def query(self, l: int, r: int) -> int:
        """Return gcd(nums[l..r]) inclusive.

        Args:
            l: Left index, 0 <= l <= r.
            r: Right index, r < n.

        Returns:
            The greatest common divisor of nums[l], ..., nums[r].
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    rg = RangeGCD([12, 18, 6, 9, 24, 36])
    print(rg.query(0, 2))  # expected: 6
    print(rg.query(3, 5))  # expected: 3
    print(rg.query(0, 5))  # expected: 3
    print(rg.query(4, 5))  # expected: 12
