from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """Reverse a list of characters in place.

        Args:
            s: A list of single-character strings to be reversed. The list is
                modified in place; the function returns nothing.

        Returns:
            None. The input list ``s`` is mutated so that its elements appear
            in reverse order.

        Example:
            >>> chars = ["h", "e", "l", "l", "o"]
            >>> Solution().reverseString(chars)
            >>> chars
            ['o', 'l', 'l', 'e', 'h']
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    chars = ["h", "e", "l", "l", "o"]
    Solution().reverseString(chars)
    print(chars)  # expected: ['o', 'l', 'l', 'e', 'h']
