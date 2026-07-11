"""Range Minimum Query via a Sqrt Tree (op = min).

Fill in the implementation. Do NOT hard-code answers.
"""
from typing import List


class RangeMin:
    """O(1) range-minimum queries on a static array using a Sqrt Tree.

    Example:
        >>> rm = RangeMin([5, 2, 8, 1, 9, 3, 7])
        >>> rm.query(1, 4)
        1
        >>> rm.query(4, 6)
        3
    """

    def __init__(self, nums: List[int]) -> None:
        """Preprocess `nums` so range minima can be answered in O(1).

        Args:
            nums: Static integer array of length n (1 <= n <= 2e5).

        Build target: O(n log log n) time and space. Use op = min. Because the
        Sqrt Tree query never overlaps ranges, idempotence is not required —
        the exact same code will later serve non-idempotent operations.
        """
        # TODO: implement
        pass

    def query(self, l: int, r: int) -> int:
        """Return the minimum of nums[l..r] inclusive.

        Args:
            l: Left index, 0 <= l <= r.
            r: Right index, r < n.

        Returns:
            min(nums[l], ..., nums[r]).
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    rm = RangeMin([5, 2, 8, 1, 9, 3, 7])
    print(rm.query(1, 4))  # expected: 1
    print(rm.query(4, 6))  # expected: 3
    print(rm.query(0, 6))  # expected: 1
    print(rm.query(2, 2))  # expected: 8
