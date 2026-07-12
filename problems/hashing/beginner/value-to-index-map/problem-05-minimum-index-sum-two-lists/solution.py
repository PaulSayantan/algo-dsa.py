"""Minimum Index Sum of Two Lists — LeetCode 599. Common strings, least index sum."""
from typing import List  # noqa: F401


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # TODO: map name -> index in list1; scan list2 tracking the smallest index sum
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))  # expected: ['Shogun']
    print(sol.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]))  # expected: ['Shogun']
    print(sol.findRestaurant(["a", "b", "c"], ["c", "b", "a"]))  # expected: ['a', 'b', 'c']
    print(sol.findRestaurant(["x", "y"], ["p", "q"]))  # expected: []
