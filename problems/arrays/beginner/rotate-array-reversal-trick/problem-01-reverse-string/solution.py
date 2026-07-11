from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """Reverse a list of characters in place.

        Args:
            s: A list of single-character strings. Modified in place; the
               function returns nothing.

        Returns:
            None. The reversal is performed by mutating ``s`` directly.

        Example:
            >>> chars = ["h", "e", "l", "l", "o"]
            >>> Solution().reverseString(chars)
            >>> chars
            ['o', 'l', 'l', 'e', 'h']
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    data = ["h", "e", "l", "l", "o"]
    Solution().reverseString(data)
    print(data)  # expected: ['o', 'l', 'l', 'e', 'h']
