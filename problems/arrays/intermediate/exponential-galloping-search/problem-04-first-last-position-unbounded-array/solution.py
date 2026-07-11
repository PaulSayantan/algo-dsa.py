"""First and Last Position in an Unbounded Sorted Array (variant of LeetCode 34).

Fill in `Solution.search_range` using the Exponential (Galloping) Search
technique to bound the region, then two boundary (lower/upper bound) binary
searches. Reads are only through reader.get(i), which returns 2**31 - 1 for
out-of-bounds indices.
"""
from typing import List


class ArrayReader:
    """Read-only view over a sorted array (with duplicates) of unknown length.

    get(i) returns the element at index i, or 2**31 - 1 if i is out of bounds.
    Provided by the judge; a reference implementation is included here only so
    the __main__ block can run locally.
    """

    def __init__(self, arr):
        self._arr = arr

    def get(self, index: int) -> int:
        if 0 <= index < len(self._arr):
            return self._arr[index]
        return 2**31 - 1


class Solution:
    def search_range(self, reader: "ArrayReader", target: int) -> List[int]:
        """Return [first, last] indices of `target`, or [-1, -1] if absent.

        Args:
            reader: An ArrayReader over a non-decreasing array (duplicates
                allowed) of unknown length; out-of-bounds reads return
                2**31 - 1.
            target: The value whose first and last positions are wanted.

        Returns:
            A two-element list [first, last]; both -1 when `target` is missing.

        Example:
            >>> Solution().search_range(ArrayReader([5, 7, 7, 8, 8, 8, 10]), 8)
            [3, 5]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    solver = Solution()
    print(solver.search_range(ArrayReader([5, 7, 7, 8, 8, 8, 10]), 8))  # expected: [3, 5]
    print(solver.search_range(ArrayReader([5, 7, 7, 8, 8, 8, 10]), 6))  # expected: [-1, -1]
    print(solver.search_range(ArrayReader([2, 2]), 2))                  # expected: [0, 1]
