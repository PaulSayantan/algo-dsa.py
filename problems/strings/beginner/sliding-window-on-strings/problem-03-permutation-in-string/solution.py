class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Return whether ``s2`` contains a permutation of ``s1`` as a
        contiguous substring.

        Args:
            s1: The pattern whose permutations we search for.
            s2: The text to search within.

        Returns:
            True if some length-len(s1) window of ``s2`` is an anagram of
            ``s1``; False otherwise.

        Example:
            >>> Solution().checkInclusion("ab", "eidbaooo")
            True
            >>> Solution().checkInclusion("ab", "eidboaoo")
            False
        """
        # TODO: implement using a fixed-size sliding window of length len(s1).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))  # expected: True
    print(sol.checkInclusion("ab", "eidboaoo"))  # expected: False
    print(sol.checkInclusion("adc", "dcda"))     # expected: True
    print(sol.checkInclusion("abc", "ab"))       # expected: False
