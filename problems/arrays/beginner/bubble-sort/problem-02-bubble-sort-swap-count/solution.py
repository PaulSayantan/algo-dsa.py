from typing import List


class Solution:
    def countSwaps(self, arr: List[int]) -> int:
        """Sort ``arr`` with Bubble Sort and count the adjacent swaps performed.

        Args:
            arr: A list of integers to sort ascending. 1 <= len(arr) <= 600.

        Returns:
            The total number of adjacent-element swaps a full bubble sort makes
            while sorting ``arr``. This equals the number of inversions in the
            original array.

        Example:
            >>> Solution().countSwaps([3, 2, 1])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSwaps([3, 2, 1]))       # expected: 3
    print(sol.countSwaps([1, 2, 3]))       # expected: 0
    print(sol.countSwaps([3, 1, 2]))       # expected: 2
