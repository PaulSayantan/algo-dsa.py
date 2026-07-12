"""132 Pattern — LeetCode 456."""
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # TODO: right-to-left monotonic stack tracking the best '2'
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.find132pattern([1, 2, 3, 4]))  # expected: False
    print(sol.find132pattern([3, 1, 4, 2]))  # expected: True
    print(sol.find132pattern([-1, 3, 2, 0]))  # expected: True
    print(sol.find132pattern([1, 0, 1, -4, -3]))  # expected: False
