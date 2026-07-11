"""LeetCode 151 - Reverse Words in a String.

Reverse the order of words, collapsing any extra whitespace to single spaces.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """Return the words of `s` in reverse order, single-space separated.

        Leading, trailing, and repeated internal spaces are removed from the
        result.

        Args:
            s: The input sentence, possibly with irregular spacing.

        Returns:
            A string containing the words of `s` in reverse order, separated by
            exactly one space and with no leading or trailing spaces.

        Example:
            >>> Solution().reverseWords("  hello world  ")
            'world hello'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))  # expected: "blue is sky the"
    print(Solution().reverseWords("  hello world  "))  # expected: "world hello"
