from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Return the index of the first occurrence of ``target`` in ``nums``.

        Args:
            nums: A list of integers (not necessarily sorted).
            target: The value to search for.

        Returns:
            The 0-based index of the first element equal to ``target``,
            or ``-1`` if ``target`` is not present.

        Example:
            >>> Solution().search([10, 50, 30, 70], 30)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([10, 50, 30, 70, 80, 20, 90, 40], 30))  # expected: 2
    print(sol.search([5, 1, 4], 9))                          # expected: -1
    print(sol.search([7], 7))                                # expected: 0
