"""Sort Colors — LeetCode 75.

Sort an array containing only 0s, 1s, and 2s in place, without a library sort.
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Sort nums in place so all 0s precede all 1s, which precede all 2s.

        Args:
            nums: A list whose every element is 0, 1, or 2. Mutated in place;
                nothing is returned.

        Returns:
            None. The input list ``nums`` is modified directly.

        Example:
            >>> arr = [2, 0, 2, 1, 1, 0]
            >>> Solution().sortColors(arr)
            >>> arr
            [0, 0, 1, 1, 2, 2]
        """
        # TODO: implement using Counting Sort (only three distinct keys).
        pass


if __name__ == "__main__":
    sol = Solution()

    a = [2, 0, 2, 1, 1, 0]
    sol.sortColors(a)
    print(a)  # expected: [0, 0, 1, 1, 2, 2]

    b = [2, 0, 1]
    sol.sortColors(b)
    print(b)  # expected: [0, 1, 2]

    c = [0]
    sol.sortColors(c)
    print(c)  # expected: [0]
