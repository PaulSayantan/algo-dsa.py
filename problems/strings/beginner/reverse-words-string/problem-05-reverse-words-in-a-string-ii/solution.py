"""LeetCode 186 - Reverse Words in a String II.

Reverse the order of words in a character array in place with O(1) extra space.
"""
from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """Reverse the order of the words in `s` in place.

        Words are separated by single spaces with no leading or trailing
        spaces. The function mutates `s` and returns nothing.

        Args:
            s: A character array to be modified in place. After the call it
               holds the same words in reversed order.

        Returns:
            None. The reordering is applied to `s` in place.

        Example:
            >>> arr = list("a b")
            >>> Solution().reverseWords(arr)
            >>> "".join(arr)
            'b a'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    arr = list("the sky is blue")
    Solution().reverseWords(arr)
    print("".join(arr))  # expected: "blue is sky the"

    arr2 = ["a"]
    Solution().reverseWords(arr2)
    print("".join(arr2))  # expected: "a"
