from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Return the ``k`` most frequent elements of ``nums`` (any order).

        Suggested approach:
          - build a frequency map (e.g. ``collections.Counter``),
          - push ``(count, value)`` pairs into a min-heap, popping the
            smallest count whenever the heap size exceeds ``k``,
          - the ``k`` pairs left in the heap are the answer.

        Args:
            nums: List of integers.
            k: Number of most-frequent elements to return.

        Returns:
            A list of the ``k`` most frequent values, in any order.

        Example:
            >>> sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
            [1, 2]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()
    print(sorted(s.topKFrequent([1, 1, 1, 2, 2, 3], 2)))   # expected: [1, 2]
    print(sorted(s.topKFrequent([1], 1)))                  # expected: [1]
    print(sorted(s.topKFrequent([4, 4, 4, 5, 5, 6], 2)))   # expected: [4, 5]
