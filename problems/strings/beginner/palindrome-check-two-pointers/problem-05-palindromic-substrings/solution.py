class Solution:
    def countSubstrings(self, s: str) -> int:
        """Return the number of palindromic substrings of ``s``.

        Substrings at different index ranges are counted separately even if
        their contents are identical.

        Args:
            s: The input string of lowercase English letters.

        Returns:
            The total count of contiguous substrings that are palindromes.

        Example:
            >>> Solution().countSubstrings("abc")
            3
            >>> Solution().countSubstrings("aaa")
            6
        """
        # TODO: for each center (odd and even), expand two pointers outward,
        # incrementing the count for every matched pair.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubstrings("abc"))  # expected: 3
    print(sol.countSubstrings("aaa"))  # expected: 6
    print(sol.countSubstrings("aba"))  # expected: 4
