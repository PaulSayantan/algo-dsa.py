class Solution:
    def reverseWords(self, s: str) -> str:
        """Reverse the order of the words in ``s``.

        Words are runs of non-space characters. Leading, trailing, and repeated
        interior spaces are collapsed so the result has words separated by a
        single space with no surrounding whitespace.

        Args:
            s: The input string, possibly containing extra spaces.

        Returns:
            A string with the words of ``s`` in reversed order, single-spaced.

        Example:
            >>> Solution().reverseWords("the sky is blue")
            'blue is sky the'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))   # expected: 'blue is sky the'
    print(Solution().reverseWords("  hello world  "))   # expected: 'world hello'
    print(Solution().reverseWords("a good   example"))  # expected: 'example good a'
