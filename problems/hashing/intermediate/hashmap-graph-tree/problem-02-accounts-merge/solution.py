"""Accounts Merge — LeetCode 721."""
from collections import defaultdict  # noqa: F401
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # TODO: union emails per account; group by root; [name, *sorted emails]; sort all
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.accountsMerge([["John", "a@x.com", "b@x.com"], ["John", "b@x.com", "c@x.com"], ["Mary", "m@x.com"]]))  # expected: [['John', 'a@x.com', 'b@x.com', 'c@x.com'], ['Mary', 'm@x.com']]
    print(sol.accountsMerge([["A", "e1@x.com"], ["B", "e2@x.com"]]))  # expected: [['A', 'e1@x.com'], ['B', 'e2@x.com']]
