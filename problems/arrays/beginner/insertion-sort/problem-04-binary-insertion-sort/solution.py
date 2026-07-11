from typing import List


class Solution:
    def binaryInsertionSort(self, nums: List[int]) -> List[int]:
        """Sort an array with Binary Insertion Sort (stable).

        Same structure as insertion sort, but the insertion index within the
        sorted prefix is found with binary search (O(log i) comparisons) instead
        of a linear scan. Elements after that index are shifted right to open a
        gap for the key.

        Args:
            nums: Integers to sort. 1 <= len(nums) <= 1e4.

        Returns:
            ``nums`` sorted in ascending order, stably (equal elements keep their
            original relative order). Sorting in place is allowed.

        Example:
            >>> Solution().binaryInsertionSort([5, 2, 4, 6, 1, 3])
            [1, 2, 3, 4, 5, 6]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.binaryInsertionSort([5, 2, 4, 6, 1, 3]))  # expected: [1, 2, 3, 4, 5, 6]
    print(sol.binaryInsertionSort([10, 10, 9]))         # expected: [9, 10, 10]
    print(sol.binaryInsertionSort([1, 2, 3, 4]))        # expected: [1, 2, 3, 4]
