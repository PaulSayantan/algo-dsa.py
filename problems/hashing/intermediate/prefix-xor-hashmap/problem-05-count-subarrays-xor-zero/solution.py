"""Count subarrays with XOR equal to 0."""
from typing import List  # noqa: F401
from collections import defaultdict  # noqa: F401


class Solution:
    def countZeroXorSubarrays(self, nums: List[int]) -> int:
        # TODO: XOR(j..i] == 0 iff prefix[j] == prefix[i]; count equal-prefix pairs.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countZeroXorSubarrays([1, 1, 1, 1]))  # expected: 4
    print(sol.countZeroXorSubarrays([4, 2, 2, 4]))  # expected: 2
    print(sol.countZeroXorSubarrays([1, 2, 3]))  # expected: 1
    print(sol.countZeroXorSubarrays([5]))  # expected: 0
    print(sol.countZeroXorSubarrays([7, 7, 7, 7]))  # expected: 4
