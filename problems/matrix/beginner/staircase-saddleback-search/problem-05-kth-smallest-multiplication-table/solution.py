class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """Return the k-th smallest value in the m x n multiplication table.

        The table ``mat[i][j] = i * j`` (1-indexed) is doubly sorted but too large
        to build. The intended approach is binary search on the answer value in
        ``[1, m*n]``, counting entries <= mid with a saddleback walk over the
        implicit grid (``min(mid // i, n)`` per row). Overall
        O(m * log(m*n)) time, O(1) extra space.

        Args:
            m: Number of rows (values 1..m).
            n: Number of columns (values 1..n).
            k: 1-indexed rank of the element to return (``1 <= k <= m*n``).

        Returns:
            The value at sorted position ``k`` of the multiplication table.

        Example:
            >>> Solution().findKthNumber(3, 3, 5)
            3
            >>> Solution().findKthNumber(2, 3, 6)
            6
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().findKthNumber(3, 3, 5))  # expected: 3
    print(Solution().findKthNumber(2, 3, 6))  # expected: 6
    print(Solution().findKthNumber(1, 5, 4))  # expected: 4
