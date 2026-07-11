class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """Reverse the first ``k`` characters of every ``2k``-character block.

        Args:
            s: The input string of lowercase English letters.
            k: The block half-size. For each ``2k`` window, the first ``k``
                characters are reversed (with the trailing-remainder rules).

        Returns:
            The transformed string after applying the block reversals.

        Example:
            >>> Solution().reverseStr("abcdefg", 2)
            'bacdfeg'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().reverseStr("abcdefg", 2))  # expected: 'bacdfeg'
    print(Solution().reverseStr("abcd", 2))     # expected: 'bacd'
