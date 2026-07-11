"""LeetCode 1157 - Online Majority Element In Subarray, via a Wavelet Tree.

Build a Wavelet Tree over `arr`. A value that occurs > half the range must be
the range median, so:
  1. find the median with a k-th-smallest descent (k = (len // 2) + 1),
  2. verify its frequency in [left, right] with a range-count / rank query,
  3. return it iff the count meets the threshold, else -1.
"""

from typing import List


class MajorityChecker:
    """Answer online majority-in-subarray queries over a static array."""

    def __init__(self, arr: List[int]) -> None:
        """Preprocess `arr` in O(n log sigma).

        Args:
            arr: The static input array (1 <= len <= 2e4, 1 <= arr[i] <= 2e4).
        """
        # TODO: implement
        pass

    def query(self, left: int, right: int, threshold: int) -> int:
        """Return the element occurring >= threshold times in arr[left..right].

        The bounds are inclusive. It is guaranteed that
        2 * threshold > right - left + 1, so at most one element can qualify.

        Args:
            left: Inclusive left index (0 <= left <= right < n).
            right: Inclusive right index.
            threshold: Minimum required occurrence count.

        Returns:
            The qualifying element, or -1 if none exists.

        Example:
            >>> mc = MajorityChecker([1, 1, 2, 2, 1, 1])
            >>> mc.query(0, 5, 4)
            1
        """
        # TODO: implement
        # Hint: candidate = kth_smallest(left, right + 1, (right - left + 1) // 2 + 1)
        #       cnt = occurrences of candidate in [left, right + 1)
        #       return candidate if cnt >= threshold else -1
        pass


if __name__ == "__main__":
    mc = MajorityChecker([1, 1, 2, 2, 1, 1])
    print(mc.query(0, 5, 4))  # expected: 1
    print(mc.query(0, 3, 3))  # expected: -1
    print(mc.query(2, 3, 2))  # expected: 2
