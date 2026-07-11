"""String Compression (LeetCode 443).

In-place Run-Length Encoding of a character array. Runs of length 1 omit the
count; longer runs write the count as individual digit characters. Return the
new length; use O(1) extra space.
"""

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        """Compress ``chars`` in place and return the new length.

        Args:
            chars: A list of single-character strings, modified in place. The
                first `return value` entries will hold the compressed form.

        Returns:
            The length of the compressed array. Characters at indices >= the
            returned length are irrelevant.

        Example:
            >>> s = Solution()
            >>> chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
            >>> s.compress(chars)
            6
            >>> chars[:6]
            ['a', '2', 'b', '2', 'c', '3']
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    c1 = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
    n1 = Solution().compress(c1)
    print(n1)         # expected: 6
    # expected c1[:6]: ['a', '2', 'b', '2', 'c', '3']

    c2 = ['a']
    n2 = Solution().compress(c2)
    print(n2)         # expected: 1  (c2[:1] == ['a'])

    c3 = ['a'] + ['b'] * 12
    n3 = Solution().compress(c3)
    print(n3)         # expected: 4  (c3[:4] == ['a', 'b', '1', '2'])
