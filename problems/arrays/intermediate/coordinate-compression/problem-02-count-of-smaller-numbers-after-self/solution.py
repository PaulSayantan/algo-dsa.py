"""Count of Smaller Numbers After Self (LeetCode 315).

Fill in the body of `countSmaller`. A Fenwick tree over coordinate-compressed
values is the intended approach. Do NOT look at SOLUTION.md until you have tried.
"""

from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """Count, for each index, how many later elements are strictly smaller.

        Args:
            nums: The input array of integers.

        Returns:
            A list ``counts`` of the same length where ``counts[i]`` is the number of
            indices ``j > i`` with ``nums[j] < nums[i]``.

        Example:
            >>> Solution().countSmaller([5, 2, 6, 1])
            [2, 1, 1, 0]
        """
        # TODO: implement
        # Hint: sort(set(nums)) -> value->rank map; sweep from the right, and for
        #       each value query the BIT prefix-sum below its rank, then add it.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSmaller([5, 2, 6, 1]))   # expected: [2, 1, 1, 0]
    print(sol.countSmaller([-1, -1]))        # expected: [0, 0]
    print(sol.countSmaller([2, 0, 1]))       # expected: [2, 0, 0]
