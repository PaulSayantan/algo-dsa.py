"""Find First and Last Position of Element in Sorted Array (LeetCode 34).

Return the first and last index of ``target`` in a non-decreasing array, or
[-1, -1] if it is absent.
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Return ``[first, last]`` indices of ``target`` in ``nums``.

        Args:
            nums: A list of integers sorted in non-decreasing order (duplicates
                allowed).
            target: The value whose first and last positions are sought.

        Returns:
            A two-element list ``[first, last]`` with the smallest and largest
            indices ``i`` where ``nums[i] == target``. Returns ``[-1, -1]`` if
            ``target`` does not occur in ``nums``.

        Example:
            >>> Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
            [3, 4]
            >>> Solution().searchRange([5, 7, 7, 8, 8, 10], 6)
            [-1, -1]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # Expected: [3, 4]
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
    # Expected: [-1, -1]
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))
    # Expected: [-1, -1]
    print(sol.searchRange([], 0))
