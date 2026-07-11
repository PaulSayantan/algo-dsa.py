"""Orderly Queue (LeetCode 899).

Return the lexicographically smallest string obtainable by repeatedly moving one
of the first k characters to the end. When k == 1 this is the least rotation
(Booth's Algorithm); when k >= 2 it is the sorted string.
"""


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """Return the smallest string reachable under the move described above.

        Args:
            s: The input string of lowercase letters.
            k: Number of leading characters eligible to be moved to the end.

        Returns:
            The lexicographically smallest achievable string.

        Example:
            >>> Solution().orderlyQueue("cba", 1)
            'acb'
            >>> Solution().orderlyQueue("baaca", 3)
            'aaabc'
        """
        # TODO: implement
        #   if k >= 2: return the sorted string
        #   if k == 1: return the lexicographically smallest rotation
        #              (use Booth's Algorithm to find the least-rotation index)
        pass


if __name__ == "__main__":
    print(Solution().orderlyQueue("cba", 1))    # expected: "acb"
    print(Solution().orderlyQueue("baaca", 3))  # expected: "aaabc"
    print(Solution().orderlyQueue("nlarb", 2))  # expected: "ablnr"
    print(Solution().orderlyQueue("v", 1))      # expected: "v"
