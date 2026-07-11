"""Count and Say (LeetCode 38).

Each term is the Run-Length Encoding (count + digit) of the previous term,
starting from "1".
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        """Return the n-th term of the count-and-say sequence.

        Args:
            n: 1-indexed position in the sequence (1 <= n <= 30).

        Returns:
            The n-th count-and-say string. Each term is the RLE description
            (count followed by digit, per run) of the previous term, with the
            base case countAndSay(1) = "1".

        Example:
            >>> Solution().countAndSay(4)
            '1211'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().countAndSay(1))  # expected: "1"
    print(Solution().countAndSay(4))  # expected: "1211"
    print(Solution().countAndSay(6))  # expected: "312211"
