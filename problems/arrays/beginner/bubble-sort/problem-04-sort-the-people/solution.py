from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """Return ``names`` ordered by descending height, via Bubble Sort.

        Sort the (height, name) pairs so taller people come first, then return
        the names in that order.

        Args:
            names: Names of the people; ``names[i]`` pairs with ``heights[i]``.
            heights: Distinct positive heights, same length as ``names``.

        Returns:
            The names sorted so that taller people appear earlier (descending
            by height).

        Example:
            >>> Solution().sortPeople(["Mary", "John", "Emma"], [180, 165, 170])
            ['Mary', 'Emma', 'John']
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # expected: ['Mary', 'Emma', 'John']
    print(sol.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
    # expected: ['Bob', 'Alice', 'Bob']
    print(sol.sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]))
    # expected: ['Kai']
    print(sol.sortPeople(["Kai"], [42]))
