"""AHU canonical hashing of rooted trees.

Recursively build each node's signature as "(" + concatenation of its children's
signatures, SORTED + ")". Isomorphic rooted trees produce identical canonical
strings; use the string itself as the key (never the salted built-in hash()).
"""
from typing import List  # noqa: F401


class Solution:
    def canonicalHash(self, parent: List[int]) -> str:
        # TODO: return the AHU canonical string of the rooted tree (root has parent -1)
        pass

    def areIsomorphic(self, parent_a: List[int], parent_b: List[int]) -> bool:
        # TODO: two rooted trees are isomorphic iff their canonical strings match
        pass

    def countDistinctShapes(self, forest: List[List[int]]) -> int:
        # TODO: number of distinct canonical shapes among the rooted trees
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.canonicalHash([-1]))  # expected: '()'
    print(sol.canonicalHash([-1, 0, 0]))  # expected: '(()())'
    print(sol.canonicalHash([-1, 0, 1]))  # expected: '((()))'
    print(sol.canonicalHash([-1, 0, 0, 0]))  # expected: '(()()())'
