"""Count Number of Nice Subarrays — LeetCode 1248."""
from collections import defaultdict  # noqa: F401
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # TODO: prefix count of odd numbers; freq map like subarray-sum
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfSubarrays([1, 1, 2, 1, 1], 3))  # expected: 2
    print(sol.numberOfSubarrays([2, 4, 6], 1))  # expected: 0
    print(sol.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))  # expected: 16
