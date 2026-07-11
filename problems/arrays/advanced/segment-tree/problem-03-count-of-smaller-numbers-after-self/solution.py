"""Count of Smaller Numbers After Self (LeetCode 315).

For each index i, count how many elements to the right of i are strictly smaller
than nums[i]. Solve in O(n log n) with a Segment Tree built over the value domain
(a frequency / count segment tree).

Fill in the method body. Do NOT use the naive O(n^2) double loop.
"""
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """Return counts[i] = #{ j > i : nums[j] < nums[i] }.

        Args:
            nums: The input integer array.

        Returns:
            A list `counts` of the same length as `nums`, where counts[i] is the
            number of elements after index i that are strictly smaller than nums[i].

        Example:
            Solution().countSmaller([5, 2, 6, 1])  # -> [2, 1, 1, 0]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().countSmaller([5, 2, 6, 1]))  # expected: [2, 1, 1, 0]
    print(Solution().countSmaller([-1, -1]))       # expected: [0, 0]
