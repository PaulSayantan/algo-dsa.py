from typing import List


class Solution:
    def countInversions(self, nums: List[int]) -> int:
        """Count inversions: pairs (i, j) with i < j and nums[i] > nums[j].

        Args:
            nums: List of integers.

        Returns:
            The total number of inversions in ``nums``.

        Example:
            >>> Solution().countInversions([2, 4, 1, 3, 5])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.countInversions([2, 4, 1, 3, 5]))  # expected: 3
    print(s.countInversions([5, 4, 3, 2, 1]))  # expected: 10
    print(s.countInversions([1, 2, 3, 4, 5]))  # expected: 0
