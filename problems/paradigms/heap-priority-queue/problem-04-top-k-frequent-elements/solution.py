"""Top K Frequent Elements — LeetCode 347.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Return the k most frequently occurring values in nums.

        The answer may be returned in any order and is guaranteed unique.

        Args:
            nums: The input array of integers.
            k: How many of the most frequent values to return.

        Returns:
            A list of the k most frequent values, in any order.

        Example:
            >>> sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
            [1, 2]
            >>> Solution().topKFrequent([1], 1)
            [1]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))         # expected (any order): [1, 2]
    print(sol.topKFrequent([1], 1))                        # expected: [1]
    print(sol.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))    # expected (any order): [-1, 2]
