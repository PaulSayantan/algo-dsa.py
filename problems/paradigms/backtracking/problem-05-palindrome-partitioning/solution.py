"""LeetCode 131 - Palindrome Partitioning.

Fill in the body of `partition` using backtracking. Do not hard-code answers.
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """Return every partition of `s` into all-palindrome substrings.

        A valid partition cuts `s` into contiguous non-empty pieces that
        concatenate back to `s`, where each piece is a palindrome.

        Args:
            s: A lowercase string of length 1..16.

        Returns:
            A list of partitions; each partition is a list of palindrome
            substrings whose concatenation equals `s`. Any ordering is valid.

        Example:
            >>> Solution().partition("aab")
            [['a', 'a', 'b'], ['aa', 'b']]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.partition("aab"))
    # Expected (in any order): [["a","a","b"], ["aa","b"]]
    print(sol.partition("aba"))
    # Expected (in any order): [["a","b","a"], ["aba"]]
