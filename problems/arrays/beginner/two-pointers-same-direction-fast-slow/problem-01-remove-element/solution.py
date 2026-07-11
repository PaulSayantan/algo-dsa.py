from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """Remove all occurrences of `val` from `nums` in place.

        After the call, the first `k` elements of `nums` must be the elements
        not equal to `val` (in any order). Return `k`. Must use O(1) extra
        space.

        Args:
            nums: The integer array to filter in place.
            val:  The value to remove from `nums`.

        Returns:
            The number of elements in `nums` that are not equal to `val`.

        Example:
            >>> Solution().removeElement([3, 2, 2, 3], 3)
            2  # nums becomes [2, 2, _, _]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = Solution().removeElement(nums, 2)
    print(k, nums[:k] if k else [])
    # Expected: k == 5, and nums[:5] is a permutation of [0, 1, 3, 0, 4]
