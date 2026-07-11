from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Return the ``k`` points closest to the origin (any order).

        Suggested approach:
          - rank points by SQUARED distance ``x*x + y*y`` (avoid ``sqrt``:
            it is monotonic and squaring keeps everything integral),
          - maintain a max-heap of size ``k`` so the farthest of the current
            best is at the root and cheap to evict. ``heapq`` is a min-heap,
            so store negated distances to simulate a max-heap.

        Args:
            points: List of ``[x, y]`` coordinate pairs.
            k: Number of closest points to return.

        Returns:
            A list of the ``k`` closest points, in any order.

        Example:
            >>> Solution().kClosest([[1, 3], [-2, 2]], 1)
            [[-2, 2]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.kClosest([[1, 3], [-2, 2]], 1))            # expected: [[-2, 2]]
    print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))   # expected (any order): [[3, 3], [-2, 4]]
