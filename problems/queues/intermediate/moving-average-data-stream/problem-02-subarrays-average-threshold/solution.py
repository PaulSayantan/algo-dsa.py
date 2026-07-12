"""Number of Sub-arrays of Size K and Average >= Threshold — LeetCode 1343."""
from typing import List  # noqa: F401


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # TODO: slide a size-k window with a running sum; count sums >= k*threshold
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))  # expected: 3
    print(sol.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))  # expected: 6
    print(sol.numOfSubarrays([1, 1, 1, 1, 1], 1, 0))  # expected: 5
    print(sol.numOfSubarrays([5], 1, 5))  # expected: 1
