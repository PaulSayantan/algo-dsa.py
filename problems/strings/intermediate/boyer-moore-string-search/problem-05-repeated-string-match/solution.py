"""Repeated String Match — fewest copies of `a` so that `b` is a substring.

Build `a` repeated ceil(len(b)/len(a)) times (and try one extra copy to cover an
offset start), then test whether `b` is a substring using Boyer–Moore (string
search).
"""


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """Return the minimum number of copies of `a` so that `b` is a substring.

        Args:
            a: The string to repeat.
            b: The target substring to contain.

        Returns:
            The minimum copy count k such that `b` occurs in `a * k`, or -1 if
            no repetition of `a` ever contains `b`.

        Example:
            >>> Solution().repeatedStringMatch("abcd", "cdabcdab")
            3
            >>> Solution().repeatedStringMatch("abc", "wxyz")
            -1
        """
        # TODO: implement using Boyer–Moore search of `b` inside repeated `a`
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.repeatedStringMatch("abcd", "cdabcdab"))   # expected: 3
    print(sol.repeatedStringMatch("a", "aa"))            # expected: 2
    print(sol.repeatedStringMatch("abc", "wxyz"))        # expected: -1
