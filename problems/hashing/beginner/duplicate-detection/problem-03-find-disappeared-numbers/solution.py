"""Find All Numbers Disappeared in an Array — LeetCode 448."""
from typing import List  # noqa: F401


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # TODO: return the values in [1..n] that never appear (ascending)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # expected: [5, 6]
    print(sol.findDisappearedNumbers([1, 1]))  # expected: [2]
    print(sol.findDisappearedNumbers([1, 2, 3]))  # expected: []
    print(sol.findDisappearedNumbers([2, 2]))  # expected: [1]
