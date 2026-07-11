"""Two Sum II - Input Array Is Sorted — LeetCode 167.

Empty solution template. Fill in the body yourself.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Return the 1-indexed positions of the two values summing to target.

        Args:
            numbers: A list of integers sorted in non-decreasing order.
            target: The desired pair sum.

        Returns:
            A list [index1, index2] (1-indexed, index1 < index2) whose values
            add up to `target`. Exactly one such pair is guaranteed to exist.

        Example:
            >>> Solution().twoSum([2, 7, 11, 15], 9)
            [1, 2]
        """
        # TODO: implement using two pointers (opposite ends)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # expected: [1, 2]
    print(sol.twoSum([2, 3, 4], 6))       # expected: [1, 3]
    print(sol.twoSum([-1, 0], -1))        # expected: [1, 2]
