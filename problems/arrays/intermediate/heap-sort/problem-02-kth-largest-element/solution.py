from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Return the k-th largest element of ``nums``.

        Do not rely on ``sorted(nums)[-k]`` — practice the heap approach.
        Two idiomatic options:
          - Build a max-heap of all elements and pop ``k`` times (partial
            heap sort). ``heapq`` is a min-heap, so negate values.
          - Maintain a min-heap of size ``k``: push each value, and when the
            heap grows past ``k`` pop the smallest. The root is the answer.

        Args:
            nums: List of integers.
            k: 1-based rank counted from the largest element.

        Returns:
            The value that would sit at position ``k`` counting from the
            largest in sorted order.

        Example:
            >>> Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
            5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))            # expected: 5
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))   # expected: 4
