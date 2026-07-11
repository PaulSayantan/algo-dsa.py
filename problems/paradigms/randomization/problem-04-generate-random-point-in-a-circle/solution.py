"""LeetCode 478 - Generate Random Point in a Circle.

Return points uniformly distributed over a disk (interior plus boundary). Use either
rejection sampling from the bounding square, or inverse-transform sampling with
r = radius * sqrt(U) to avoid clustering near the center.
"""

from __future__ import annotations

import random
from typing import List


class Solution:
    """Sample points uniformly over a disk."""

    def __init__(self, radius: float, x_center: float, y_center: float) -> None:
        """Initialize with the circle's radius and center.

        Args:
            radius: The radius of the circle (radius > 0).
            x_center: The x-coordinate of the center.
            y_center: The y-coordinate of the center.
        """
        # TODO: store radius and center
        pass

    def randPoint(self) -> List[float]:
        """Return a point [x, y] chosen uniformly at random over the disk.

        The point must satisfy (x - x_center)^2 + (y - y_center)^2 <= radius^2,
        and the distribution must be uniform over the disk's area.

        Returns:
            A list [x, y] of floats lying inside or on the circle.

        Example:
            >>> s = Solution(1.0, 0.0, 0.0)
            >>> x, y = s.randPoint()
            >>> x * x + y * y <= 1.0 + 1e-9
            True
        """
        # TODO: implement (rejection sampling or r = radius * sqrt(U))
        pass


if __name__ == "__main__":
    obj = Solution(1.0, 0.0, 0.0)
    # Each call returns [x, y] with x^2 + y^2 <= 1, uniform over the unit disk's area.
    print(obj.randPoint())  # e.g. [-0.02493, -0.38077]
    print(obj.randPoint())  # e.g. [0.82314, 0.38945]

    obj2 = Solution(2.0, 5.0, -3.0)
    # Each call returns [x, y] with (x - 5)^2 + (y + 3)^2 <= 4.
    print(obj2.randPoint())  # e.g. [6.31041, -2.16276]
