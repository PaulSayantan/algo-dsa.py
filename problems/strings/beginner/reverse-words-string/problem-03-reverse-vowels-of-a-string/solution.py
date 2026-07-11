"""LeetCode 345 - Reverse Vowels of a String.

Reverse only the vowels of a string, leaving every consonant in place.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        """Return `s` with only its vowels reversed.

        Vowels are a, e, i, o, u in either case. Non-vowel characters keep
        their original positions.

        Args:
            s: The input string.

        Returns:
            A new string in which the vowels appear in reverse order relative to
            one another while all other characters are unchanged.

        Example:
            >>> Solution().reverseVowels("leetcode")
            'leotcede'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().reverseVowels("IceCreAm"))  # expected: "AceCreIm"
    print(Solution().reverseVowels("leetcode"))  # expected: "leotcede"
