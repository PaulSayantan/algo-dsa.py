"""Find the Most Competitive Subsequence — LeetCode 1673."""
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # TODO: monotonic increasing stack; pop while len(stack) + remaining > k
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.mostCompetitive([3, 5, 2, 6], 2))  # expected: [2, 6]
    print(sol.mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 4))  # expected: [2, 3, 3, 4]
    print(sol.mostCompetitive([5, 4, 3, 2, 1], 2))  # expected: [2, 1]
