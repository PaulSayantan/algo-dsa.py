"""LeetCode 220 - Contains Duplicate III.

Fill in the body of `containsNearbyAlmostDuplicate` using a bucketing scheme.
"""

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        """Detect a near-duplicate pair within index and value windows.

        Args:
            nums: The input array of integers.
            indexDiff: Maximum allowed index distance abs(i - j).
            valueDiff: Maximum allowed value distance abs(nums[i] - nums[j]).

        Returns:
            True if some pair (i, j), i != j, satisfies abs(i - j) <= indexDiff
            and abs(nums[i] - nums[j]) <= valueDiff; otherwise False.

        Example:
            >>> Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
            True
        """
        # TODO: implement using value buckets of width (valueDiff + 1)
        #       plus a sliding window over the last indexDiff indices
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))            # expected: True
    print(sol.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))      # expected: False
    print(sol.containsNearbyAlmostDuplicate([7, 2, 8], 2, 1))               # expected: True
