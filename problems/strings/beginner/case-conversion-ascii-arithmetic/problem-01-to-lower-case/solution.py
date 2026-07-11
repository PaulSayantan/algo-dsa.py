"""LeetCode 709 - To Lower Case.

Convert every uppercase letter in ``s`` to lowercase using ASCII arithmetic,
without calling built-in case-conversion helpers such as ``str.lower()``.
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        """Return ``s`` with every uppercase letter replaced by its lowercase form.

        Args:
            s: A string of printable ASCII characters (1 <= len <= 100).

        Returns:
            A new string identical to ``s`` except that each character whose code
            falls in the uppercase range 'A'..'Z' is shifted into the matching
            lowercase character. All other characters are unchanged.

        Example:
            >>> Solution().toLowerCase("Hello")
            'hello'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.toLowerCase("Hello"))   # expected: "hello"
    print(sol.toLowerCase("here"))    # expected: "here"
    print(sol.toLowerCase("LOVELY"))  # expected: "lovely"
