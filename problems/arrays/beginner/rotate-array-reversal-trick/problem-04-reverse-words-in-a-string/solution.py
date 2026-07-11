class Solution:
    def reverseWords(self, s: str) -> str:
        """Reverse the order of the words in a string.

        Leading, trailing, and repeated interior spaces are collapsed so the
        result has words separated by exactly one space and no padding.

        Args:
            s: The input sentence, which may contain leading/trailing spaces
               and multiple spaces between words.

        Returns:
            A new string with the words in reverse order, separated by single
            spaces, with no leading or trailing whitespace.

        Example:
            >>> Solution().reverseWords("a good   example")
            'example good a'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))    # expected: 'blue is sky the'
    print(Solution().reverseWords("  hello world  "))    # expected: 'hello world'
    print(Solution().reverseWords("a good   example"))   # expected: 'example good a'
