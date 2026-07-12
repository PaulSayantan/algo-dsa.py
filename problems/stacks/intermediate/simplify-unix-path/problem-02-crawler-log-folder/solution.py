"""Crawler Log Folder — LeetCode 1598."""
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # TODO: stack depth — push a name, pop on '../', skip './'
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations(["d1/", "d2/", "../", "d21/", "./"]))  # expected: 2
    print(sol.minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"]))  # expected: 3
    print(sol.minOperations(["d1/", "../", "../", "../"]))  # expected: 0
    print(sol.minOperations([]))  # expected: 0
