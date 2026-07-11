from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        """Return the length of the longest substring of ``word`` that contains
        no element of ``forbidden`` as a substring.

        The intended approach builds an Aho-Corasick automaton over
        ``forbidden`` and does a single left-to-right sliding-window scan of
        ``word``: at each right endpoint the automaton reveals the shortest
        forbidden string ending there, which is used to push the window's left
        boundary forward.

        Args:
            word: The string to search, length 1..1e5, lowercase letters.
            forbidden: Up to 1e5 forbidden strings, each of length 1..10,
                lowercase letters.

        Returns:
            The maximum length of a substring of ``word`` none of whose
            substrings appear in ``forbidden`` (at least 0).

        Example:
            >>> Solution().longestValidSubstring("cbaaaabc", ["aaa", "cb"])
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestValidSubstring("cbaaaabc", ["aaa", "cb"]))
    # Expected: 4
    print(sol.longestValidSubstring("leetcode", ["de", "le", "e"]))
    # Expected: 4
    print(sol.longestValidSubstring("aaa", ["aaa"]))
    # Expected: 2
