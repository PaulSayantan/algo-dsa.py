"""Rotate String — LeetCode 796.

Fill in the body using Naive Pattern Matching. Do not use the built-in
`in` / str.find substring search — practice sliding `goal` over `s + s`
yourself.
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """Return whether ``goal`` is a rotation of ``s``.

        Args:
            s: The original string.
            goal: The candidate rotation of ``s``.

        Returns:
            ``True`` if some number of left-shifts of ``s`` yields ``goal``,
            otherwise ``False``.

        Example:
            >>> Solution().rotateString("abcde", "cdeab")
            True
            >>> Solution().rotateString("abcde", "abced")
            False
        """
        # TODO: implement using Naive Pattern Matching
        # Idea: goal is a rotation of s  <=>  len(s) == len(goal)
        #       and goal occurs as a substring of (s + s).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.rotateString("abcde", "cdeab"))  # expected: True
    print(sol.rotateString("abcde", "abced"))  # expected: False
    print(sol.rotateString("aa", "aa"))        # expected: True
