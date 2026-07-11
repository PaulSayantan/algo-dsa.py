"""LeetCode 519 - Random Flip Matrix.

Uniformly pick a currently-0 cell and flip it to 1, then support reset().
Use a lazy, map-backed Fisher-Yates over the flattened grid of m*n ids.
"""
from typing import List


class Solution:
    def __init__(self, m: int, n: int):
        """Initialize the object with the grid dimensions.

        Args:
            m: Number of rows.
            n: Number of columns.
        """
        # TODO: implement
        # Hint: total = m * n. Track `remaining` (number of 0-cells left) and a
        # dict that lazily records Fisher-Yates swaps over the id space [0, total).
        pass

    def flip(self) -> List[int]:
        """Flip a uniformly random currently-0 cell to 1 and return its [i, j].

        Returns:
            The [row, col] of the flipped cell; each still-0 cell is equally
            likely.

        Example:
            >>> obj = Solution(3, 1)
            >>> r = obj.flip()
            >>> r in ([0, 0], [1, 0], [2, 0])
            True
        """
        # TODO: implement
        # Hint: remaining -= 1; x = random.randint(0, remaining); the chosen id is
        # swap.get(x, x). Then record swap[x] = swap.get(remaining, remaining) so
        # the last live id fills slot x. Convert id -> [id // n, id % n].
        pass

    def reset(self) -> None:
        """Reset every cell back to 0."""
        # TODO: implement
        # Hint: clear the swap map and restore remaining = total.
        pass


if __name__ == "__main__":
    obj = Solution(3, 1)
    print(obj.flip() in ([0, 0], [1, 0], [2, 0]))  # expected: True
    print(obj.flip() in ([0, 0], [1, 0], [2, 0]))  # expected: True
    obj.reset()
    print(obj.flip() in ([0, 0], [1, 0], [2, 0]))  # expected: True
