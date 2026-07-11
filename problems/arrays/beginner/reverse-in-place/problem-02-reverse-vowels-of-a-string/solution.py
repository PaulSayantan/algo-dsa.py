class Solution:
    def reverseVowels(self, s: str) -> str:
        """Reverse only the vowels of ``s``, leaving all other characters fixed.

        Args:
            s: The input string. Vowels are 'a', 'e', 'i', 'o', 'u' in either
                upper or lower case.

        Returns:
            A new string in which the vowels appear in reversed relative order
            while every non-vowel character keeps its original position.

        Example:
            >>> Solution().reverseVowels("IceCreAm")
            'AceCreIm'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().reverseVowels("IceCreAm"))  # expected: 'AceCreIm'
    print(Solution().reverseVowels("leetcode"))  # expected: 'leotcede'
