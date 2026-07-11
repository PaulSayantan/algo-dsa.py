"""LeetCode 389 - Find the Difference.

Find the single extra lowercase letter added when ``s`` was shuffled and one
character was inserted to form ``t``. Solve using ASCII arithmetic (sum of code
points, or XOR) rather than counting structures.
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """Return the one extra character present in ``t`` but not in ``s``.

        Args:
            s: A string of lowercase English letters (0 <= len <= 1000).
            t: ``s`` shuffled with exactly one extra lowercase letter inserted,
                so ``len(t) == len(s) + 1``.

        Returns:
            The single added character, as a length-1 string.

        Example:
            >>> Solution().findTheDifference("abcd", "abcde")
            'e'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde"))  # expected: "e"
    print(sol.findTheDifference("", "y"))          # expected: "y"
    print(sol.findTheDifference("aab", "baaa"))    # expected: "a"
