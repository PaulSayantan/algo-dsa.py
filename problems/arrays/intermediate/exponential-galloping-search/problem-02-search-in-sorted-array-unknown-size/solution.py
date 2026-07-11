"""Search in a Sorted Array of Unknown Size (LeetCode 702).

Fill in `Solution.search` using the Exponential (Galloping) Search technique.
You may only read the array through `reader.get(i)`, which returns 2**31 - 1
for any out-of-bounds index.
"""


class ArrayReader:
    """Read-only view over a hidden sorted array.

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
    def search(self, reader: "ArrayReader", target: int) -> int:
        """Return the index of `target`, or -1 if it is not present.

        Args:
            reader: An ArrayReader over a sorted array of unique integers whose
                length is unknown; reads past the end return 2**31 - 1.
            target: The value to locate.

        Returns:
            The index `k` with `reader.get(k) == target`, or -1 if absent.

        Example:
            >>> Solution().search(ArrayReader([-1, 0, 3, 5, 9, 12]), 9)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    solver = Solution()
    print(solver.search(ArrayReader([-1, 0, 3, 5, 9, 12]), 9))  # expected: 4
    print(solver.search(ArrayReader([-1, 0, 3, 5, 9, 12]), 2))  # expected: -1
    print(solver.search(ArrayReader([5]), 5))                   # expected: 0
