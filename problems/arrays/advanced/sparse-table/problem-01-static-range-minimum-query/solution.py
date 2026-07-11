"""Static Range Minimum Query (RMQ) via a Sparse Table.

Fill in the SparseTable class so that each query runs in O(1) after an
O(n log n) build.
"""

from typing import List


class SparseTable:
    """A static structure for O(1) range-minimum queries.

    Args:
        nums: The immutable integer array to index over.

    Example:
        >>> st = SparseTable([1, 3, 2, 7, 9, 11, 3, 5])
        >>> st.query(1, 3)   # min(3, 2, 7)
        2
        >>> st.query(0, 7)   # min of whole array
        1
    """

    def __init__(self, nums: List[int]) -> None:
        # TODO: implement
        pass

    def query(self, left: int, right: int) -> int:
        """Return the minimum of nums[left..right] (inclusive) in O(1).

        Args:
            left: Left index of the range (0-indexed, inclusive).
            right: Right index of the range (0-indexed, inclusive).

        Returns:
            The minimum value in nums[left..right].
        """
        # TODO: implement
        pass


def range_min_queries(nums: List[int], queries: List[List[int]]) -> List[int]:
    """Answer every (l, r) range-minimum query on an immutable array.

    Args:
        nums: The immutable integer array.
        queries: A list of [l, r] index pairs (0-indexed, inclusive).

    Returns:
        A list with the minimum of nums[l..r] for each query, in order.

    Example:
        >>> range_min_queries([1, 3, 2, 7, 9, 11, 3, 5], [[1, 3], [4, 6], [0, 7]])
        [2, 3, 1]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    sample_nums = [1, 3, 2, 7, 9, 11, 3, 5]
    sample_queries = [[1, 3], [4, 6], [0, 7]]
    print(range_min_queries(sample_nums, sample_queries))
    # Expected: [2, 3, 1]
