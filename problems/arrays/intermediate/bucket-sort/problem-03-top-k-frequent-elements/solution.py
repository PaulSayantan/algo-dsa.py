"""LeetCode 347 - Top K Frequent Elements.

Fill in the body of `topKFrequent` using Bucket Sort.
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Return the k most frequent elements of ``nums``.

        Args:
            nums: The input array of integers.
            k: How many of the most frequent elements to return.

        Returns:
            A list of the k most frequent values, in any order.

        Example:
            >>> sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
            [1, 2]
        """
        # TODO: implement using bucket sort by frequency
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))     # expected: [1, 2] (any order)
    print(sol.topKFrequent([1], 1))                    # expected: [1]
    print(sol.topKFrequent([4, 4, 4, 5, 5, 6, 7], 3))  # expected: [4, 5, 6] or [4, 5, 7]
