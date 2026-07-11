"""Find the City With the Smallest Number of Neighbors at a Threshold Distance.

LeetCode 1334. Solve with Floyd–Warshall all-pairs shortest paths.
"""

from typing import List


class Solution:
    def findTheCity(
        self,
        n: int,
        edges: List[List[int]],
        distanceThreshold: int,
    ) -> int:
        """Return the city with the fewest reachable neighbors within the threshold.

        Build the all-pairs shortest-distance matrix, then for each city count how
        many other cities are within ``distanceThreshold``. Return the city with the
        smallest count, breaking ties by choosing the largest city index.

        Args:
            n: Number of cities, labeled ``0 .. n - 1``.
            edges: List of ``[from, to, weight]`` bidirectional weighted edges.
            distanceThreshold: Maximum path distance for a city to count as reachable.

        Returns:
            The index of the qualifying city.

        Example:
            >>> Solution().findTheCity(
            ...     4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4
            ... )
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4))
    # Expected: 3
    print(
        sol.findTheCity(
            5,
            [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]],
            2,
        )
    )
    # Expected: 0
