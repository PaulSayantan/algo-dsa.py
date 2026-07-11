class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """Return the maximum number of vowels in any length-``k`` substring of ``s``.

        Vowels are the letters 'a', 'e', 'i', 'o', 'u'.

        Args:
            s: A string of lowercase English letters.
            k: The fixed window (substring) length, with ``1 <= k <= len(s)``.

        Returns:
            The greatest count of vowel characters found in any contiguous
            substring of length exactly ``k``.

        Example:
            >>> Solution().maxVowels("abciiidef", 3)
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxVowels("abciiidef", 3))  # expected: 3
    print(sol.maxVowels("aeiou", 2))       # expected: 2
    print(sol.maxVowels("leetcode", 3))    # expected: 2
