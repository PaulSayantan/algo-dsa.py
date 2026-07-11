"""LeetCode 389 - Find the Difference.

t is s shuffled with exactly one extra letter inserted. Return that extra letter.
Fill in the body using a Character Frequency Count.
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """Return the single extra letter present in t but not accounted for by s.

        Args:
            s: The original lowercase string.
            t: A shuffle of s with one additional lowercase letter inserted;
                len(t) == len(s) + 1.

        Returns:
            The one-character string that was added to t.

        Example:
            >>> Solution().findTheDifference("abcd", "abcde")
            'e'
            >>> Solution().findTheDifference("", "y")
            'y'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde"))  # expected: "e"
    print(sol.findTheDifference("", "y"))          # expected: "y"
    print(sol.findTheDifference("aabb", "abbba"))  # expected: "b"
