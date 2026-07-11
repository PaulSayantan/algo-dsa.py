"""SPOJ KQUERY — count elements strictly greater than k in a range.

Fill in the implementation using a Merge Sort Tree. The count of elements > k in
a node equals (node size) - (count of elements <= k), where the latter is found by
binary searching the node's sorted list.
"""

from typing import List


class KQuerySolver:
    """Answer 'count of elements > k in nums[i..j]' queries on a static array."""

    def __init__(self, nums: List[int]) -> None:
        """Preprocess the array (build the Merge Sort Tree).

        Args:
            nums: The static input array. Not modified after construction.
        """
        # TODO: implement
        pass

    def count_greater(self, i: int, j: int, k: int) -> int:
        """Count indices p with i <= p <= j and nums[p] > k.

        Args:
            i: Left endpoint, 0-based inclusive.
            j: Right endpoint, 0-based inclusive.
            k: Threshold; count strictly-greater elements.

        Returns:
            Number of elements in nums[i..j] strictly greater than k.
        """
        # TODO: implement
        pass


def kquery(nums: List[int], queries: List[List[int]]) -> List[int]:
    """Answer a batch of (i, j, k) 'count greater than k' queries.

    Args:
        nums: The static input array of length n.
        queries: A list of [i, j, k] triples (i, j are 0-based inclusive).

    Returns:
        A list of answers, one per query, in order.

    Example:
        >>> kquery([5, 1, 2, 3, 4], [[0, 4, 2], [1, 3, 3]])
        [3, 0]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    sample_nums = [5, 1, 2, 3, 4]
    sample_queries = [[0, 4, 2], [1, 3, 3]]
    print(kquery(sample_nums, sample_queries))
    # Expected output: [3, 0]
