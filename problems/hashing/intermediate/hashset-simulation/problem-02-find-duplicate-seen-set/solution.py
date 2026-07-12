"""Find the Duplicate Number (seen-set variant) — LeetCode 287."""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # TODO: return the first value already present in a seen set
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDuplicate([1, 3, 4, 2, 2]))  # expected: 2
    print(sol.findDuplicate([3, 1, 3, 4, 2]))  # expected: 3
    print(sol.findDuplicate([2, 2, 2, 2, 2]))  # expected: 2
