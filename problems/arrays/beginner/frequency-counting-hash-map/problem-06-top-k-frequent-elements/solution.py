"""Top K Frequent Elements (LeetCode 347).

Return the k values that occur most frequently in the array.
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Return the ``k`` most frequently occurring values in ``nums``.

        The result may be in any order. The answer is guaranteed to be unique.

        Args:
            nums: A non-empty list of integers.
            k: The number of top-frequency elements to return; ``1 <= k <=``
                number of distinct values in ``nums``.

        Returns:
            A list of the ``k`` values with the highest frequencies.

        Example:
            >>> sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
            [1, 2]
            >>> Solution().topKFrequent([1], 1)
            [1]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    solver = Solution()

    print(solver.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # expected: [1, 2] (any order)
    print(solver.topKFrequent([1], 1))  # expected: [1]
    print(solver.topKFrequent([4, 4, 4, 6, 6, 2, 2, 2, 2], 1))  # expected: [2]
