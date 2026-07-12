"""Generate every binary string of length n using a queue."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def binaryStrings(self, n: int) -> List[str]:
        # TODO: seed the queue with ""; emit s when len(s) == n, else enqueue s+"0", s+"1"
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.binaryStrings(2))  # expected: ['00', '01', '10', '11']
    print(sol.binaryStrings(1))  # expected: ['0', '1']
    print(sol.binaryStrings(0))  # expected: ['']
    print(sol.binaryStrings(3))  # expected: ['000', '001', '010', '011', '100', '101', '110', '111']
