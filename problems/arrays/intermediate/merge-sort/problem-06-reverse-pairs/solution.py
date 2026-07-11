from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """Count reverse pairs: (i, j) with i < j and nums[i] > 2 * nums[j].

        Args:
            nums: List of integers.

        Returns:
            The number of reverse pairs in ``nums``.

        Example:
            >>> Solution().reversePairs([1, 3, 2, 3, 1])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.reversePairs([1, 3, 2, 3, 1]))  # expected: 2
    print(s.reversePairs([2, 4, 3, 5, 1]))  # expected: 3
    print(s.reversePairs([1, 2, 3, 4, 5]))  # expected: 0
