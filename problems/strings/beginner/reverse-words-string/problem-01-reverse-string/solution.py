"""LeetCode 344 - Reverse String.

Reverse an array of characters in place using O(1) extra memory.
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """Reverse the character list `s` in place.

        Args:
            s: A list of single-character strings to be reversed in place.
               The function returns nothing; it mutates `s` directly.

        Returns:
            None. The reversal is applied to `s` in place.

        Example:
            >>> arr = ["h", "e", "l", "l", "o"]
            >>> Solution().reverseString(arr)
            >>> arr
            ['o', 'l', 'l', 'e', 'h']
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    arr = ["h", "e", "l", "l", "o"]
    Solution().reverseString(arr)
    print(arr)  # expected: ['o', 'l', 'l', 'e', 'h']

    arr2 = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(arr2)
    print(arr2)  # expected: ['h', 'a', 'n', 'n', 'a', 'H']
