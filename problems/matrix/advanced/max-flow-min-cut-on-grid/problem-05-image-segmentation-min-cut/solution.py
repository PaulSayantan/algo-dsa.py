"""Image Segmentation Min-Cut — minimum-cost foreground/background labeling.

Fill in `min_segmentation_cost` using a Max-Flow / Min-Cut on Grid model: source
= foreground terminal, sink = background terminal, S->pixel capacity = bg penalty,
pixel->T capacity = fg penalty, and undirected edges of capacity `sep` between
orthogonally adjacent pixels. The minimum S-T cut equals the answer.
"""

from typing import List


class Solution:
    def min_segmentation_cost(
        self, fg: List[List[int]], bg: List[List[int]], sep: int
    ) -> int:
        """Return the minimum total cost of labeling every pixel FG or BG.

        Total cost = sum of each pixel's chosen-label penalty
                     + sep * (number of orthogonally adjacent pairs labeled differently).

        Args:
            fg: R x C matrix; fg[i][j] is the penalty for labeling (i, j) foreground.
            bg: R x C matrix; bg[i][j] is the penalty for labeling (i, j) background.
            sep: Non-negative smoothness penalty per differing adjacent pair.

        Returns:
            The minimum achievable total cost over all labelings.

        Example:
            >>> Solution().min_segmentation_cost([[3, 1]], [[1, 4]], 2)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.min_segmentation_cost([[3, 1]], [[1, 4]], 2))                  # expected: 4
    print(sol.min_segmentation_cost([[1, 5], [5, 1]], [[5, 1], [1, 5]], 1))  # expected: 8
    print(sol.min_segmentation_cost([[3]], [[5]], 100))                      # expected: 3
