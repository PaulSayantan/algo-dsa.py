"""LeetCode 347 - Top K Frequent Elements.

Return the k most frequent values using Quickselect on frequency.
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Return the k most frequent elements in nums.

        Args:
            nums: List of integers (with repeats).
            k: Number of most-frequent distinct values to return
                (1 <= k <= number of distinct values).

        Returns:
            A list of the k values with the highest frequencies, in any order.

        Example:
            >>> sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
            [1, 2]
        """
        # TODO: implement
        # Hint: 1) count frequencies with a hash map;
        #       2) collect the distinct values into a list;
        #       3) Quickselect on frequency so the k highest-frequency values
        #          end up in one contiguous block, then return that block.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)))              # expected: [1, 2]
    print(sol.topKFrequent([1], 1))                                     # expected: [1]
    print(sol.topKFrequent([4, 4, 4, 6, 6, 2, 2, 2, 2], 1))             # expected: [2]
