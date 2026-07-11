"""Repeated DNA Sequences (LeetCode 187).

Solve this with the Rabin-Karp rolling-hash technique over fixed-length windows.
"""

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """Return all 10-letter substrings of ``s`` that occur more than once.

        Args:
            s: A DNA string over the alphabet {'A', 'C', 'G', 'T'}.

        Returns:
            A list of the distinct 10-letter substrings that appear at least
            twice in ``s``. The order of the returned list does not matter, and
            each repeated sequence appears exactly once.

        Example:
            >>> Solution().findRepeatedDnaSequences(
            ...     "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
            ['AAAAACCCCC', 'CCCCCAAAAA']
        """
        # TODO: implement using Rabin-Karp (rolling hash + set of seen hashes)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    # expected (any order): ['AAAAACCCCC', 'CCCCCAAAAA']
    print(sol.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
    # expected: ['AAAAAAAAAA']
    print(sol.findRepeatedDnaSequences("ACGTACGT"))
    # expected: []
