"""Smallest Subarrays With Maximum Bitwise OR (LeetCode 2411).

Approach to implement: build a Sparse Table over bitwise OR (idempotent), and
for each start index binary-search the shortest window whose OR reaches the
suffix OR (the maximum achievable OR from that start).
"""

from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        """For each start i, return the shortest subarray length reaching max OR.

        Args:
            nums: A 0-indexed array of non-negative integers.

        Returns:
            answer where answer[i] is the length of the shortest subarray
            starting at i whose bitwise OR equals the maximum OR of any
            subarray starting at i.

        Example:
            >>> Solution().smallestSubarrays([1, 0, 2, 1, 3])
            [3, 3, 2, 2, 1]
            >>> Solution().smallestSubarrays([1, 2])
            [2, 1]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().smallestSubarrays([1, 0, 2, 1, 3]))  # Expected: [3, 3, 2, 2, 1]
    print(Solution().smallestSubarrays([1, 2]))           # Expected: [2, 1]
