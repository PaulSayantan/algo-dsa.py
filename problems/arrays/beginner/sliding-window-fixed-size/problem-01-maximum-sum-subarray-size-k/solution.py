from typing import List


def max_sum_subarray(nums: List[int], k: int) -> int:
    """Return the maximum sum among all contiguous subarrays of length ``k``.

    Args:
        nums: A list of integers (may include negatives).
        k: The fixed window size, with ``1 <= k <= len(nums)``.

    Returns:
        The largest sum obtainable from any single contiguous subarray that
        contains exactly ``k`` elements.

    Example:
        >>> max_sum_subarray([2, 1, 5, 1, 3, 2], 3)
        9
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # expected: 9
    print(max_sum_subarray([2, 3, 4, 1, 5], 2))      # expected: 7
    print(max_sum_subarray([-1, -2, -3, -4], 2))     # expected: -3
