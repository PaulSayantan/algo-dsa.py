from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Remove duplicates from a sorted array in place, keeping one of each.

        After the call, the first `k` elements of `nums` must be the distinct
        values in their original (sorted) order. Return `k`. Must use O(1)
        extra space.

        Args:
            nums: A non-decreasing sorted integer array (length >= 1).

        Returns:
            The number of unique elements `k`.

        Example:
            >>> Solution().removeDuplicates([1, 1, 2])
            2  # nums becomes [1, 2, _]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = Solution().removeDuplicates(nums)
    print(k, nums[:k] if k else [])
    # Expected: k == 5, and nums[:5] == [0, 1, 2, 3, 4]
