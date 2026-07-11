"""Permutation in String (LeetCode 567).

Fill in the body using the Sliding Window technique.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Return True if s2 contains a contiguous permutation of s1.

        Args:
            s1: The pattern whose permutations we search for.
            s2: The text to search within.

        Returns:
            True if some contiguous substring of s2 is a permutation of s1,
            otherwise False.

        Example:
            >>> Solution().checkInclusion("ab", "eidbaooo")
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))  # expected: True
    print(sol.checkInclusion("ab", "eidboaoo"))  # expected: False
    print(sol.checkInclusion("adc", "dcda"))     # expected: True
