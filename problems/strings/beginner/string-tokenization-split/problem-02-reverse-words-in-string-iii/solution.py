"""LeetCode 557 - Reverse Words in a String III.

Fill in the body of `reverseWords`. Do not modify the signature.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """Reverse the letters of each word while keeping word order.

        Words are separated by exactly one space and there are no leading or
        trailing spaces.

        Args:
            s: The input sentence.

        Returns:
            A new sentence where each word's characters are reversed but the
            words remain in their original order, separated by single spaces.

        Example:
            >>> Solution().reverseWords("Mr Ding")
            'rM gniD'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords("Let's take LeetCode contest"))
    # expected: "s'teL ekat edoCteeL tsetnoc"
    print(sol.reverseWords("Mr Ding"))   # expected: "rM gniD"
    print(sol.reverseWords("hello"))     # expected: "olleh"
