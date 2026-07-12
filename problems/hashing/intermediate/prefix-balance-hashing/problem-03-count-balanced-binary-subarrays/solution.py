"""Count balanced binary subarrays (equal number of 0s and 1s)."""
from typing import List  # noqa: F401
from collections import defaultdict  # noqa: F401


class Solution:
    def countBalancedSubarrays(self, nums: List[int]) -> int:
        # TODO: map 0 -> -1, 1 -> +1; a balanced window has equal balance at its ends,
        #       so count pairs of positions sharing the same running balance.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countBalancedSubarrays([0, 1]))  # expected: 1
    print(sol.countBalancedSubarrays([0, 1, 0, 1]))  # expected: 4
    print(sol.countBalancedSubarrays([1, 1, 1]))  # expected: 0
    print(sol.countBalancedSubarrays([0, 0, 1, 1]))  # expected: 2
    print(sol.countBalancedSubarrays([1, 0, 1, 0, 1, 0]))  # expected: 9
