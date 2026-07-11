from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Remove duplicates in a sorted array so each value appears <= twice.

        After the call, the first `k` elements of `nums` must be the retained
        elements in their original (sorted) order. Return `k`. Must use O(1)
        extra space.

        Args:
            nums: A non-decreasing sorted integer array (length >= 1).

        Returns:
            The number of retained elements `k`.

        Example:
            >>> Solution().removeDuplicates([1, 1, 1, 2, 2, 3])
            5  # nums becomes [1, 1, 2, 2, 3, _]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = Solution().removeDuplicates(nums)
    print(k, nums[:k] if k else [])
    # Expected: k == 7, and nums[:7] == [0, 0, 1, 1, 2, 3, 3]
