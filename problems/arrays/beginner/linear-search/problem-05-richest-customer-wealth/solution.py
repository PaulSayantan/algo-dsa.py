from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """Return the wealth of the richest customer (maximum row sum).

        Args:
            accounts: An ``m x n`` grid where ``accounts[i][j]`` is the money
                customer ``i`` holds in bank ``j``.

        Returns:
            The largest sum among all rows.

        Example:
            >>> Solution().maximumWealth([[1, 5], [7, 3], [3, 5]])
            10
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumWealth([[1, 2, 3], [3, 2, 1]]))            # expected: 6
    print(sol.maximumWealth([[1, 5], [7, 3], [3, 5]]))          # expected: 10
    print(sol.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]])) # expected: 17
