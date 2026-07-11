"""LeetCode 1392 - Longest Happy Prefix.

Return the longest proper prefix of s that is also a suffix. With the
Z-Algorithm: a suffix starting at index i equals a prefix iff z[i] == n - i.
"""

from typing import List


class Solution:
    def longestPrefix(self, s: str) -> str:
        """Return the longest non-empty proper prefix of s that is also a suffix.

        Args:
            s: A non-empty lowercase string.

        Returns:
            The longest happy prefix (a proper prefix equal to a suffix), or the
            empty string ``""`` if none exists.

        Example:
            >>> Solution().longestPrefix("level")
            'l'
            >>> Solution().longestPrefix("ababab")
            'abab'
            >>> Solution().longestPrefix("abcdef")
            ''
        """
        # TODO: implement
        pass

    def _z_array(self, s: str) -> List[int]:
        """Optional helper: compute the Z-array of ``s`` in O(len(s)) time.

        Args:
            s: The string whose Z-array should be computed.

        Returns:
            A list ``z`` where ``z[i]`` is the length of the longest substring
            starting at ``i`` that is also a prefix of ``s``.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPrefix("level"))    # expected: "l"
    print(sol.longestPrefix("ababab"))   # expected: "abab"
    print(sol.longestPrefix("abcdef"))   # expected: ""
