"""Set Mismatch — LeetCode 645."""
from typing import List  # noqa: F401


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # TODO: return [duplicated_value, missing_value] for the set {1..n}
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findErrorNums([1, 2, 2, 4]))  # expected: [2, 3]
    print(sol.findErrorNums([1, 1]))  # expected: [1, 2]
    print(sol.findErrorNums([2, 2]))  # expected: [2, 1]
    print(sol.findErrorNums([3, 2, 3, 4, 6, 5]))  # expected: [3, 1]
