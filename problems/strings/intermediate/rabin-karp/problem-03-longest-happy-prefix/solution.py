"""Longest Happy Prefix (LeetCode 1392).

Solve this with Rabin-Karp: compare prefix hashes against suffix hashes.
"""


class Solution:
    def longestPrefix(self, s: str) -> str:
        """Return the longest proper prefix of ``s`` that is also a suffix.

        A "happy prefix" is a non-empty prefix of ``s`` that also occurs as a
        suffix, excluding the whole string itself (i.e. it must be proper).

        Args:
            s: The input string of lowercase English letters.

        Returns:
            The longest happy prefix of ``s``, or ``""`` if none exists.

        Example:
            >>> Solution().longestPrefix("level")
            'l'
            >>> Solution().longestPrefix("ababab")
            'abab'
        """
        # TODO: implement using Rabin-Karp (rolling / prefix hashes)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(repr(sol.longestPrefix("level")))   # expected: 'l'
    print(repr(sol.longestPrefix("ababab")))  # expected: 'abab'
    print(repr(sol.longestPrefix("abcdef")))  # expected: ''
