"""First Repeating Element. Index of the first element that occurs more than once."""
from typing import List  # noqa: F401


class Solution:
    def firstRepeatingIndex(self, nums: List[int]) -> int:
        # TODO: count occurrences, then return the first index whose value repeats
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstRepeatingIndex([10, 5, 3, 4, 3, 5, 6]))  # expected: 1
    print(sol.firstRepeatingIndex([1, 2, 3, 4]))  # expected: -1
    print(sol.firstRepeatingIndex([1, 1, 1]))  # expected: 0
    print(sol.firstRepeatingIndex([9, 8, 7, 8]))  # expected: 1
    print(sol.firstRepeatingIndex([4, 5, 6, 5, 4]))  # expected: 0
