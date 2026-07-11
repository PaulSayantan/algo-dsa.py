from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """For each index, count elements to its right that are smaller.

        Args:
            nums: List of integers.

        Returns:
            A list ``counts`` where ``counts[i]`` is the number of indices
            ``j > i`` with ``nums[j] < nums[i]``.

        Example:
            >>> Solution().countSmaller([5, 2, 6, 1])
            [2, 1, 1, 0]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.countSmaller([5, 2, 6, 1]))  # expected: [2, 1, 1, 0]
    print(s.countSmaller([-1, -1]))      # expected: [0, 0]
    print(s.countSmaller([3, 2, 2, 1]))  # expected: [3, 1, 1, 0]
