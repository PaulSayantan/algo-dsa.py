"""Matching Bracket Indices — classic stack bracket matching."""
from typing import List


class Solution:
    def matchingBrackets(self, s: str) -> List[int]:
        # TODO: push opener indices; on a closer, pop and pair the two indices
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.matchingBrackets("([])"))  # expected: [3, 2, 1, 0]
    print(sol.matchingBrackets("()[]"))  # expected: [1, 0, 3, 2]
    print(sol.matchingBrackets("(())"))  # expected: [3, 2, 1, 0]
    print(sol.matchingBrackets("{[()]}"))  # expected: [5, 4, 3, 2, 1, 0]
