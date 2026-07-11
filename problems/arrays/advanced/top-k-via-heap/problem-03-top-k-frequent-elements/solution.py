"""Top K Frequent Elements (LeetCode 347).

Return the k most frequent elements in any order. Recommended: count with a hash map,
then use a size-k min-heap keyed on frequency (O(n log k)), or bucket sort (O(n)).
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Return the k most frequent elements of nums (order does not matter).

        Args:
            nums: The array of integers.
            k: How many of the most frequent elements to return.

        Returns:
            A list of the k elements with the highest occurrence counts.

        Example:
            topKFrequent([1, 1, 1, 2, 2, 3], 2) -> [1, 2]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # expected (any order): [1, 2]
    print(sol.topKFrequent([1], 1))                 # expected: [1]
    print(sol.topKFrequent([4, 4, 4, 5, 5, 6], 2))  # expected (any order): [4, 5]
