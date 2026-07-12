"""Check If N and Its Double Exist — LeetCode 1346."""
from typing import List  # noqa: F401


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # TODO: as you scan, check whether 2*x or x/2 was already seen
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkIfExist([10, 2, 5, 3]))  # expected: True
    print(sol.checkIfExist([3, 1, 7, 11]))  # expected: False
    print(sol.checkIfExist([0, 0]))  # expected: True
