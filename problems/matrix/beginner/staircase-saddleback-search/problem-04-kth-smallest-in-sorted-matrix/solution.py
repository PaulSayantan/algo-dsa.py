from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """Return the k-th smallest element (with duplicates) in a sorted matrix.

        Each row and column is sorted ascending. The intended approach is binary
        search on the answer value, using a staircase / saddleback walk to count
        entries <= mid in O(n) per step -> O(n * log(range)) overall, O(1) extra
        space.

        Args:
            matrix: An ``n x n`` matrix with rows and columns sorted ascending.
            k: 1-indexed rank of the element to return (``1 <= k <= n*n``).

        Returns:
            The value that would sit at position ``k`` if all entries were sorted.

        Example:
            >>> Solution().kthSmallest([[1, 2], [1, 3]], 2)
            1
            >>> Solution().kthSmallest([[-5]], 1)
            -5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15],
    ]
    print(Solution().kthSmallest(grid, 8))          # expected: 13
    print(Solution().kthSmallest([[1, 2], [1, 3]], 2))  # expected: 1
