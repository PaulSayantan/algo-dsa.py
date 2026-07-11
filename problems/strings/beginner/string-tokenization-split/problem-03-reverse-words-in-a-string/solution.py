"""LeetCode 151 - Reverse Words in a String.

Fill in the body of `reverseWords`. Do not modify the signature.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """Reverse the order of words in ``s``.

        The input may contain leading/trailing spaces and multiple spaces
        between words. The output must have words in reverse order separated by
        exactly one space, with no leading or trailing spaces.

        Args:
            s: The input string, possibly with irregular whitespace.

        Returns:
            The words of ``s`` in reverse order, single-space separated.

        Example:
            >>> Solution().reverseWords("  hello world  ")
            'world hello'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords("the sky is blue"))    # expected: "blue is sky the"
    print(sol.reverseWords("  hello world  "))    # expected: "world hello"
    print(sol.reverseWords("a good   example"))   # expected: "example good a"
