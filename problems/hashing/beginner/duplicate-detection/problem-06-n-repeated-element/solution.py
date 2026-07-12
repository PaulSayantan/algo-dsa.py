"""N-Repeated Element in Size 2N Array — LeetCode 961."""
from typing import List  # noqa: F401


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # TODO: exactly one value repeats; return the first value seen twice
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.repeatedNTimes([1, 2, 3, 3]))  # expected: 3
    print(sol.repeatedNTimes([2, 1, 2, 5, 3, 2]))  # expected: 2
    print(sol.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))  # expected: 5
    print(sol.repeatedNTimes([9, 5, 3, 3]))  # expected: 3
