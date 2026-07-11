"""Range Sum of Elements <= K, via an augmented Merge Sort Tree.

Fill in the implementation. Build a Merge Sort Tree where each node stores its
sorted list AND a prefix-sum array of that list. To answer (l, r, k), binary search
for k in each covering node's sorted list and read the matching prefix sum in O(1).
"""

from typing import List


class RangeSumAtMostSolver:
    """Answer 'sum of elements <= k in nums[l..r]' queries on a static array."""

    def __init__(self, nums: List[int]) -> None:
        """Preprocess the array (build the augmented Merge Sort Tree).

        Args:
            nums: The static input array. Not modified after construction.
        """
        # TODO: implement
        pass

    def sum_at_most(self, l: int, r: int, k: int) -> int:
        """Sum of nums[p] for l <= p <= r with nums[p] <= k.

        Args:
            l: Left endpoint, 0-based inclusive.
            r: Right endpoint, 0-based inclusive.
            k: Threshold value.

        Returns:
            Sum of elements in nums[l..r] that are <= k (0 if none).
        """
        # TODO: implement
        pass


def range_sum_at_most_queries(nums: List[int], queries: List[List[int]]) -> List[int]:
    """Answer a batch of (l, r, k) 'sum of elements <= k' queries.

    Args:
        nums: The static input array of length n.
        queries: A list of [l, r, k] triples (l, r are 0-based inclusive).

    Returns:
        A list of answers, one per query, in order.

    Example:
        >>> range_sum_at_most_queries([3, 1, 4, 1, 5], [[0, 4, 3], [1, 3, 4], [0, 4, 0]])
        [5, 6, 0]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    sample_nums = [3, 1, 4, 1, 5]
    sample_queries = [[0, 4, 3], [1, 3, 4], [0, 4, 0]]
    print(range_sum_at_most_queries(sample_nums, sample_queries))
    # Expected output: [5, 6, 0]
