from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Sort ``nums`` in ascending order using heap sort.

        Do not use any built-in sort. Aim for O(n log n) time and O(1)
        auxiliary space (sort the list in place, then return it).

        Suggested structure:
          - a ``sift_down(arr, start, end)`` helper that restores the max-heap
            property at index ``start`` within ``arr[:end]``,
          - a build-heap loop that calls ``sift_down`` from the last parent
            down to index 0,
          - an extraction loop that swaps ``arr[0]`` with ``arr[i]`` and
            sifts the new root down over ``arr[:i]``.

        Args:
            nums: List of integers to sort.

        Returns:
            The same list, reordered into non-decreasing order.

        Example:
            >>> Solution().sortArray([5, 2, 3, 1])
            [1, 2, 3, 5]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))        # expected: [1, 2, 3, 5]
    print(s.sortArray([5, 1, 1, 2, 0, 0]))  # expected: [0, 0, 1, 1, 2, 5]
    print(s.sortArray([-3, 0, -3, 2]))      # expected: [-3, -3, 0, 2]
