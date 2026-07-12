"""Find the Town Judge — LeetCode 997."""
from collections import defaultdict  # noqa: F401
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # TODO: judge has indegree n-1 and outdegree 0
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findJudge(2, [[1, 2]]))  # expected: 2
    print(sol.findJudge(3, [[1, 3], [2, 3]]))  # expected: 3
    print(sol.findJudge(3, [[1, 3], [2, 3], [3, 1]]))  # expected: -1
    print(sol.findJudge(1, []))  # expected: 1
