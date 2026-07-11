"""LeetCode 557 - Reverse Words in a String III.

Reverse the letters of each word while keeping word order and spacing.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """Reverse the characters of every word, preserving word order.

        Args:
            s: A sentence with single spaces between words and no leading or
               trailing spaces.

        Returns:
            A new string in which each word's characters are reversed but the
            words remain in their original order and the spaces are preserved.

        Example:
            >>> Solution().reverseWords("Mr Ding")
            'rM gniD'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().reverseWords("Let's take LeetCode contest"))
    # expected: "s'teL ekat edoCteeL tsetnoc"

    print(Solution().reverseWords("Mr Ding"))
    # expected: "rM gniD"
