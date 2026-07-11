from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """Return the k-th smallest element (in sorted order) of a row/col-sorted matrix.

        Duplicates are counted separately. Aim for better than O(n^2) memory by
        binary-searching the value range instead of materializing all elements.

        Args:
            matrix: An ``n x n`` matrix with every row and column sorted
                non-decreasingly.
            k: 1-indexed rank of the element to return (``1 <= k <= n*n``).

        Returns:
            The value that is the k-th smallest across the whole matrix.

        Example:
            >>> Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)
            13
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))  # expected: 13
    print(sol.kthSmallest([[-5]], 1))                                   # expected: -5
    print(sol.kthSmallest([[1, 2], [1, 3]], 2))                         # expected: 1
