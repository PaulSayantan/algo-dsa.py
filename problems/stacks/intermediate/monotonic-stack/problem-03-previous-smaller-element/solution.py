"""Previous Smaller Element (nearest smaller to the left)."""
from typing import List


class Solution:
    def previousSmaller(self, nums: List[int]) -> List[int]:
        # TODO: monotonic increasing stack
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.previousSmaller([4, 5, 2, 10, 8]))  # expected: [-1, 4, -1, 2, 2]
    print(sol.previousSmaller([1, 2, 3, 4]))  # expected: [-1, 1, 2, 3]
    print(sol.previousSmaller([3, 2, 1]))  # expected: [-1, -1, -1]
