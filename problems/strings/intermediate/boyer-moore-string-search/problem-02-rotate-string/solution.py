"""Rotate String — is `goal` a rotation of `s`?

Reduce to a substring test: `goal` is a rotation of `s` iff the lengths match
and `goal` is a substring of `s + s`. Run that substring search with
Boyer–Moore (string search).
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """Return True iff `goal` is some rotation of `s`.

        Args:
            s: The original string.
            goal: The candidate rotation.

        Returns:
            True if `goal` can be obtained from `s` by repeated left shifts,
            i.e. lengths are equal and `goal` occurs in `s + s`; else False.

        Example:
            >>> Solution().rotateString("abcde", "cdeab")
            True
            >>> Solution().rotateString("abcde", "abced")
            False
        """
        # TODO: implement using Boyer–Moore search of `goal` inside `s + s`
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.rotateString("abcde", "cdeab"))   # expected: True
    print(sol.rotateString("abcde", "abced"))   # expected: False
    print(sol.rotateString("aa", "a"))          # expected: False
