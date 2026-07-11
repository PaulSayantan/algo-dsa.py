"""LeetCode 990 - Satisfiability of Equality Equations.

Fill in the body of `equationsPossible`. The intended technique is
Union-Find (Disjoint Set Union): union all '==' pairs, then check that no
'!=' pair ended up in the same set.
"""
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """Decide whether all equality/inequality equations can hold at once.

        Args:
            equations: A list of 4-character strings, each of the form
                "a==b" or "a!=b", where the endpoints are lowercase letters.

        Returns:
            True if integers can be assigned to the variables so that every
            equation is satisfied, otherwise False.

        Example:
            >>> Solution().equationsPossible(["a==b", "b!=a"])
            False
        """
        # TODO: implement using Union-Find (Disjoint Set Union)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.equationsPossible(["a==b", "b!=a"]))              # expected: False
    print(sol.equationsPossible(["b==a", "a==b"]))              # expected: True
    print(sol.equationsPossible(["a==b", "b==c", "a!=c"]))      # expected: False
    print(sol.equationsPossible(["c==c", "b==d", "x!=z"]))      # expected: True
