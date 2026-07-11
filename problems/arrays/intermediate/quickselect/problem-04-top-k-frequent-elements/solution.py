"""Top K Frequent Elements (LeetCode 347).

Fill in the body of `topKFrequent` using Quickselect over distinct elements
keyed by frequency.
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Return the k most frequently occurring elements of `nums`.

        Args:
            nums: A list of integers, possibly with repeats.
            k: How many of the highest-frequency elements to return
                (1 <= k <= number of distinct values in nums).

        Returns:
            A list of the k elements with the greatest frequency, in any order.

        Example:
            >>> sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
            [1, 2]
        """
        # TODO: implement using Quickselect on distinct elements keyed by frequency
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))        # expected (any order): [1, 2]
    print(sol.topKFrequent([1], 1))                        # expected: [1]
    print(sol.topKFrequent([4, 4, 4, 5, 5, 6, 7], 1))      # expected: [4]
