"""Longest duplicate substring: binary search the length + rolling hash.

For a fixed length L a duplicate exists iff two windows share a hash (verified by
slice). The answer length is monotone, so binary-search it.
"""
from typing import List  # noqa: F401


class Solution:
    BASE = 911382323
    MOD = 972663749

    def longestDupLength(self, s: str) -> int:
        # TODO: binary-search L; use rolling hashes to detect a duplicate of length L
        pass

    def longestRepeatedSubstringLength(self, s: str) -> int:
        # TODO
        pass

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # TODO: return the sorted list of 10-letter sequences that occur more than once
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGGTTTT"))  # expected: ['AAAAACCCCC', 'CCCCCAAAAA']
    print(sol.findRepeatedDnaSequences("AAAAAAAAAAAAA"))  # expected: ['AAAAAAAAAA']
    print(sol.findRepeatedDnaSequences("AAAAAAAAAA"))  # expected: []
    print(sol.findRepeatedDnaSequences("ACGT"))  # expected: []
