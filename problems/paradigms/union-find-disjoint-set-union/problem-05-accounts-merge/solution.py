"""LeetCode 721 - Accounts Merge.

Fill in the body of `accountsMerge`. The intended technique is
Union-Find (Disjoint Set Union): union all emails within each account,
then group emails by their DSU root and attach the owner's name.
"""
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """Merge accounts that share at least one email address.

        Args:
            accounts: A list where each entry is [name, email1, email2, ...].
                Accounts sharing any email belong to the same person.

        Returns:
            The merged accounts. Each merged account is [name, *sorted_emails]
            with emails in lexicographic order. The outer list may be in any
            order.

        Example:
            >>> Solution().accountsMerge([
            ...     ["John", "a@m.com", "b@m.com"],
            ...     ["John", "a@m.com", "c@m.com"],
            ... ])
            [['John', 'a@m.com', 'b@m.com', 'c@m.com']]
        """
        # TODO: implement using Union-Find (Disjoint Set Union)
        pass


if __name__ == "__main__":
    sol = Solution()
    result = sol.accountsMerge([
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ])
    # expected (order of accounts may vary):
    # [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
    #  ["Mary", "mary@mail.com"],
    #  ["John", "johnnybravo@mail.com"]]
    print(result)
