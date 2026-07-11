from typing import List


class Solution:
    def count_occurrences(self, nums: List[int], target: int) -> int:
        """Return how many times ``target`` appears in ``nums``.

        Args:
            nums: A list of integers (may be empty, unsorted).
            target: The value to count.

        Returns:
            The number of elements equal to ``target`` (0 if none).

        Example:
            >>> Solution().count_occurrences([1, 2, 2, 3], 2)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.count_occurrences([1, 2, 3, 2, 4, 2, 5], 2))  # expected: 3
    print(sol.count_occurrences([7, 8, 9], 6))              # expected: 0
    print(sol.count_occurrences([4, 4, 4, 4], 4))           # expected: 4
