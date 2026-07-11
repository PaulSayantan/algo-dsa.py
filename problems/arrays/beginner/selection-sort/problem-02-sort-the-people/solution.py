"""Sort the People — Selection Sort over parallel arrays (LeetCode 2418).

Return `names` ordered by descending height, keeping names and heights aligned.
"""
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """Return names sorted by descending height using Selection Sort.

        Args:
            names: The list of person names.
            heights: The list of heights (all distinct); heights[i] belongs to
                names[i].

        Returns:
            The names reordered so the tallest person appears first.

        Example:
            >>> Solution().sortPeople(["Mary", "John", "Emma"], [180, 165, 170])
            ['Mary', 'Emma', 'John']
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
    # expected: ['Mary', 'Emma', 'John']
    print(sol.sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]))
    # expected: ['Bob', 'Alice', 'Bob']
    print(sol.sortPeople(["Zoe"], [42]))
    # expected: ['Zoe']
