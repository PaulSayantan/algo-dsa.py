"""K-th Smallest Number in Range, via a Merge Sort Tree.

Fill in the implementation. Build a Merge Sort Tree that can answer
"count of elements <= v in nums[l..r]". Then binary search on the value v to find
the smallest v whose in-range count is >= k; that v is the k-th smallest.
"""

from typing import List


class KthSmallestSolver:
    """Answer 'k-th smallest value in nums[l..r]' queries on a static array."""

    def __init__(self, nums: List[int]) -> None:
        """Preprocess the array (build the Merge Sort Tree).

        Args:
            nums: The static input array. Not modified after construction.
        """
        # TODO: implement
        pass

    def kth_smallest(self, l: int, r: int, k: int) -> int:
        """Return the k-th smallest element (1-indexed) of nums[l..r].

        Args:
            l: Left endpoint, 0-based inclusive.
            r: Right endpoint, 0-based inclusive.
            k: 1-based rank; guaranteed 1 <= k <= r - l + 1.

        Returns:
            The value that would appear at position k (1-indexed) if nums[l..r]
            were sorted in non-decreasing order.
        """
        # TODO: implement
        pass


def kth_smallest_queries(nums: List[int], queries: List[List[int]]) -> List[int]:
    """Answer a batch of (l, r, k) k-th smallest queries.

    Args:
        nums: The static input array of length n.
        queries: A list of [l, r, k] triples (l, r 0-based inclusive; k 1-based).

    Returns:
        A list of answers, one per query, in order.

    Example:
        >>> kth_smallest_queries([1, 5, 2, 6, 3, 7, 4], [[1, 5, 3], [0, 6, 1], [2, 4, 2]])
        [5, 1, 3]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    sample_nums = [1, 5, 2, 6, 3, 7, 4]
    sample_queries = [[1, 5, 3], [0, 6, 1], [2, 4, 2]]
    print(kth_smallest_queries(sample_nums, sample_queries))
    # Expected output: [5, 1, 3]
