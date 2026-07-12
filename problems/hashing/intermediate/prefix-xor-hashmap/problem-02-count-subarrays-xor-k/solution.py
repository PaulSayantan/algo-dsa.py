"""Count subarrays whose XOR equals k."""
from typing import List  # noqa: F401
from collections import defaultdict  # noqa: F401


class Solution:
    def subarraysWithXorK(self, nums: List[int], k: int) -> int:
        # TODO: subarray (j..i] has XOR k iff prefix[j] == prefix[i] ^ k;
        #       count previously-seen prefixes equal to cur ^ k.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraysWithXorK([4, 2, 2, 6, 4], 6))  # expected: 4
    print(sol.subarraysWithXorK([5, 6, 7, 8, 9], 5))  # expected: 2
    print(sol.subarraysWithXorK([1, 1, 1, 1], 0))  # expected: 4
    print(sol.subarraysWithXorK([3, 3], 0))  # expected: 1
    print(sol.subarraysWithXorK([1, 2, 3], 7))  # expected: 0
