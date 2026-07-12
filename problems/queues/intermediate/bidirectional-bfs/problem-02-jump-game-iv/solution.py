"""Jump Game IV — LeetCode 1345 (bidirectional BFS)."""
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # TODO: two frontiers from index 0 and the last index; expand the smaller,
        # jump to i-1, i+1, and same-value indices; stop when the frontiers meet
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))  # expected: 3
    print(sol.minJumps([7, 6, 9, 6, 9, 6, 9, 7]))  # expected: 1
    print(sol.minJumps([6, 1, 9]))  # expected: 2
    print(sol.minJumps([11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]))  # expected: 3
    print(sol.minJumps([7]))  # expected: 0
