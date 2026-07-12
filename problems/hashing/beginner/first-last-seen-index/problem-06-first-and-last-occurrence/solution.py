"""First and Last Occurrence via Hash Map. Return [first index, last index] of target."""
from typing import List  # noqa: F401


class Solution:
    def firstLast(self, nums: List[int], target: int) -> List[int]:
        # TODO: build first-seen and last-seen index maps, then look up target
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstLast([5, 7, 7, 8, 8, 10], 8))  # expected: [3, 4]
    print(sol.firstLast([5, 7, 7, 8, 8, 10], 6))  # expected: [-1, -1]
    print(sol.firstLast([1], 1))  # expected: [0, 0]
    print(sol.firstLast([2, 2, 2, 2], 2))  # expected: [0, 3]
    print(sol.firstLast([1, 2, 3, 2, 1], 2))  # expected: [1, 3]
