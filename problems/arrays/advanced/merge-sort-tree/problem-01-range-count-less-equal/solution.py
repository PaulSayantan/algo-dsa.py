"""Range Count of Elements <= X using a Merge Sort Tree.

Fill in the implementation. Build a segment tree whose nodes store the sorted
elements of their range, then answer each (l, r, x) query by decomposing the
range into O(log n) nodes and binary searching for x inside each node's list.
"""

from typing import List


class RangeCountSolver:
    """Answer 'count of elements <= x in nums[l..r]' queries on a static array."""

    def __init__(self, nums: List[int]) -> None:
        """Preprocess the array (build the Merge Sort Tree).

        Args:
            nums: The static input array. Not modified after construction.
        """
        # TODO: implement (build the merge sort tree here)
        pass

    def count_at_most(self, l: int, r: int, x: int) -> int:
        """Count indices i with l <= i <= r and nums[i] <= x.

        Args:
            l: Left endpoint of the range, 0-based inclusive.
            r: Right endpoint of the range, 0-based inclusive.
            x: Threshold value.

        Returns:
            The number of elements in nums[l..r] that are <= x.
        """
        # TODO: implement
        pass


def range_count_queries(nums: List[int], queries: List[List[int]]) -> List[int]:
    """Answer a batch of (l, r, x) count-at-most queries.

    Args:
        nums: The static input array of length n.
        queries: A list of [l, r, x] triples (l, r are 0-based inclusive).

    Returns:
        A list of answers, one per query, in the same order.

    Example:
        >>> range_count_queries([2, 5, 1, 4, 3], [[0, 4, 3], [1, 3, 4], [2, 2, 0]])
        [3, 2, 0]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    sample_nums = [2, 5, 1, 4, 3]
    sample_queries = [[0, 4, 3], [1, 3, 4], [2, 2, 0]]
    print(range_count_queries(sample_nums, sample_queries))
    # Expected output: [3, 2, 0]
