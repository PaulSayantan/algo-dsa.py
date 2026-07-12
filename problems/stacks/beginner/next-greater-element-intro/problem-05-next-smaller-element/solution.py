"""Next Smaller Element (to the right) — classic monotonic stack."""
from typing import List


class Solution:
    def nextSmallerElement(self, nums: List[int]) -> List[int]:
        # TODO: increasing stack of indices; a strictly smaller value resolves the larger ones on top
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextSmallerElement([4, 8, 5, 2, 25]))  # expected: [2, 5, 2, -1, -1]
    print(sol.nextSmallerElement([1, 2, 3, 4]))  # expected: [-1, -1, -1, -1]
    print(sol.nextSmallerElement([13, 7, 6, 12]))  # expected: [7, 6, -1, -1]
    print(sol.nextSmallerElement([5]))  # expected: [-1]
