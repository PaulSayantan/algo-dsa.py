"""Number of Good Pairs — LeetCode 1512. Count pairs i < j with nums[i] == nums[j]."""
from typing import List  # noqa: F401


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # TODO: for each value, add how many equal values were seen before it
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # expected: 4
    print(sol.numIdenticalPairs([1, 1, 1, 1]))  # expected: 6
    print(sol.numIdenticalPairs([1, 2, 3]))  # expected: 0
    print(sol.numIdenticalPairs([5, 5, 5]))  # expected: 3
