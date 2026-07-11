from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """Apply a batch of range-increment updates to a zero-initialized array.

        Each update [startIdx, endIdx, inc] adds `inc` to every element in the
        inclusive index range [startIdx, endIdx].

        Args:
            length: The size of the array, initially all zeros.
            updates: A list of [startIdx, endIdx, inc] operations to apply.

        Returns:
            The array of size `length` after applying all updates in order.

        Example:
            >>> Solution().getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]])
            [-2, 0, 3, 5, 3]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]))  # expected: [-2, 0, 3, 5, 3]
    print(sol.getModifiedArray(4, [[0, 3, 1], [1, 2, 5]]))              # expected: [1, 6, 6, 1]
