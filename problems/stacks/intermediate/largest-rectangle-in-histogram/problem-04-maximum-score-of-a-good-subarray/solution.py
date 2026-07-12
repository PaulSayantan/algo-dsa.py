"""Maximum Score of a Good Subarray — histogram bounds via monotonic stack."""
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # TODO: previous/next strictly-smaller boundaries per bar; keep max height*width whose span covers k
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumScore([1, 4, 3, 7, 4, 5], 3))  # expected: 15
    print(sol.maximumScore([5, 5, 4, 5, 4, 1, 1, 1], 0))  # expected: 20
    print(sol.maximumScore([1], 0))  # expected: 1
    print(sol.maximumScore([6, 4, 2], 1))  # expected: 8
