"""Next Greater Element II — LeetCode 503 (circular)."""
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # TODO: monotonic stack over 2n indices
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElements([1, 2, 1]))  # expected: [2, -1, 2]
    print(sol.nextGreaterElements([1, 2, 3, 4, 3]))  # expected: [2, 3, 4, -1, 4]
    print(sol.nextGreaterElements([5, 4, 3, 2, 1]))  # expected: [-1, 5, 5, 5, 5]
