"""Range GCD Queries via a Sparse Table.

Fill in the SparseTableGCD class so that each query runs in O(1) after an
O(n log n) build. The gcd operation is idempotent, so overlapping query
blocks are safe.
"""

from typing import List


class SparseTableGCD:
    """A static structure for O(1) range-gcd queries.

    Args:
        nums: The immutable positive-integer array to index over.

    Example:
        >>> st = SparseTableGCD([12, 6, 9, 18, 24])
        >>> st.query(0, 1)   # gcd(12, 6)
        6
        >>> st.query(2, 4)   # gcd(9, 18, 24)
        3
    """

    def __init__(self, nums: List[int]) -> None:
        # TODO: implement
        pass

    def query(self, left: int, right: int) -> int:
        """Return gcd(nums[left..right]) inclusive, in O(1).

        Args:
            left: Left index (0-indexed, inclusive).
            right: Right index (0-indexed, inclusive).

        Returns:
            The gcd of nums[left..right].
        """
        # TODO: implement
        pass


def range_gcd_queries(nums: List[int], queries: List[List[int]]) -> List[int]:
    """Answer every (l, r) range-gcd query on an immutable array.

    Args:
        nums: The immutable positive-integer array.
        queries: A list of [l, r] index pairs (0-indexed, inclusive).

    Returns:
        A list with gcd(nums[l..r]) for each query, in order.

    Example:
        >>> range_gcd_queries([12, 6, 9, 18, 24], [[0, 1], [2, 4], [0, 4]])
        [6, 3, 3]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    sample_nums = [12, 6, 9, 18, 24]
    sample_queries = [[0, 1], [2, 4], [0, 4]]
    print(range_gcd_queries(sample_nums, sample_queries))
    # Expected: [6, 3, 3]
