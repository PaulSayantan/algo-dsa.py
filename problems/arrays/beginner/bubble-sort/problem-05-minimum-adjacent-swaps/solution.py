from typing import List


class Solution:
    def minAdjacentSwaps(self, arr: List[int]) -> int:
        """Return the minimum number of adjacent swaps that sort ``arr``.

        This equals the number of inversions in ``arr`` and also the number of
        swaps a plain Bubble Sort performs.

        Args:
            arr: A list of integers (duplicates allowed). 1 <= len(arr) <= 2000.

        Returns:
            The minimum count of adjacent-element swaps needed to sort ``arr``
            into non-decreasing order.

        Example:
            >>> Solution().minAdjacentSwaps([2, 8, 5, 3, 9, 4])
            6
        """
        swaps = 0
        for _ in range(len(arr)):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    swaps += 1
                    arr[i], arr[i+1] = arr[i+1], arr[i]
        return swaps


if __name__ == "__main__":
    sol = Solution()
    print(sol.minAdjacentSwaps([2, 8, 5, 3, 9, 4]))    # expected: 6
    print(sol.minAdjacentSwaps([1, 2, 3, 4, 5]))       # expected: 0
    print(sol.minAdjacentSwaps([3, 2, 3, 1]))          # expected: 4
