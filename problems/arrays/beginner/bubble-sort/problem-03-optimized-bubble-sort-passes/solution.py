from typing import List


class Solution:
    def countPasses(self, arr: List[int]) -> int:
        """Sort ``arr`` with early-exit Bubble Sort and count passes performed.

        A pass is one complete left-to-right sweep. Passes continue until one
        completes with no swaps; the final confirming (zero-swap) pass is
        counted too.

        Args:
            arr: A list of integers to sort ascending. 1 <= len(arr) <= 1000.

        Returns:
            The number of passes the optimized bubble sort performs, including
            the final pass that detects the array is sorted.

        Example:
            >>> Solution().countPasses([1, 2, 3, 4])
            1
        """
        # TODO: implement
        swaps = 0
        for _ in range(len(arr)):
            currSwaps = 0
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    currSwaps += 1
            if currSwaps == 0:
                swaps += 1
                break
            else:
                swaps += 1

        return swaps


if __name__ == "__main__":
    sol = Solution()
    print(sol.countPasses([1, 2, 3, 4]))       # expected: 1
    print(sol.countPasses([5, 1, 4, 2, 8]))    # expected: 3
    print(sol.countPasses([4, 3, 2, 1]))       # expected: 4
