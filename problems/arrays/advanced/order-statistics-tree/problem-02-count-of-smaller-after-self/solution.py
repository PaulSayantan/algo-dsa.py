"""LeetCode 315 - Count of Smaller Numbers After Self.

Solve with an Order-Statistics Tree: scan right to left, and for each element
query the rank (# of stored keys strictly less than it) before inserting it.

This is an EMPTY TEMPLATE. Fill in the logic yourself.
"""
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """Count strictly-smaller elements to the right of each index.

        Args:
            nums: The input integer array.

        Returns:
            A list `counts` of the same length, where counts[i] is the number of
            j > i with nums[j] < nums[i].

        Example:
            Solution().countSmaller([5, 2, 6, 1])  # -> [2, 1, 1, 0]
        """
        # TODO: implement (right-to-left scan; rank query then insert into OST)
        pass


if __name__ == "__main__":
    print(Solution().countSmaller([5, 2, 6, 1]))  # expected [2, 1, 1, 0]
    print(Solution().countSmaller([-1, -1]))       # expected [0, 0]
    print(Solution().countSmaller([-1]))           # expected [0]
