"""Longest subarray with XOR equal to k."""
from typing import List  # noqa: F401


class Solution:
    def longestSubarrayXorK(self, nums: List[int], k: int) -> int:
        # TODO: store the EARLIEST index of each prefix XOR (seed {0: -1});
        #       at i, if (cur ^ k) was seen, candidate length is i - first[cur ^ k].
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubarrayXorK([4, 2, 2, 6, 4], 6))  # expected: 5
    print(sol.longestSubarrayXorK([1, 2, 3, 4, 5], 0))  # expected: 4
    print(sol.longestSubarrayXorK([3, 3], 0))  # expected: 2
    print(sol.longestSubarrayXorK([1, 2, 3], 100))  # expected: 0
    print(sol.longestSubarrayXorK([6], 6))  # expected: 1
