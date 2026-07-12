"""Find All Duplicates in an Array — LeetCode 442."""
from typing import List  # noqa: F401


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # TODO: return every value that appears exactly twice (as a sorted list)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # expected: [2, 3]
    print(sol.findDuplicates([1, 1, 2]))  # expected: [1]
    print(sol.findDuplicates([1]))  # expected: []
    print(sol.findDuplicates([2, 2, 3, 3]))  # expected: [2, 3]
