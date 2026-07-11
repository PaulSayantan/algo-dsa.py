from typing import List


class Solution:
    def rowWithMax1s(self, mat: List[List[int]]) -> int:
        """Return the index of the row holding the most 1s.

        Every row is sorted non-decreasing (0s then 1s). Ties go to the smaller
        row index; return -1 if there are no 1s. Aim for O(m + n) time and O(1)
        extra space using a staircase walk from the top-right corner.

        Args:
            mat: An ``m x n`` binary matrix; each row sorted non-decreasing.

        Returns:
            The 0-based index of the row with the maximum number of 1s, or -1 if
            no row contains a 1.

        Example:
            >>> Solution().rowWithMax1s([[0, 0], [1, 1]])
            1
            >>> Solution().rowWithMax1s([[0, 0], [0, 0]])
            -1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    m1 = [
        [0, 0, 0, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 0],
    ]
    print(Solution().rowWithMax1s(m1))                 # expected: 1
    print(Solution().rowWithMax1s([[0, 0], [0, 0]]))   # expected: -1
