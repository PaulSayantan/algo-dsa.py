"""Count Pattern Occurrences in a Text.

Build a suffix tree of `text` once (Ukkonen, O(n)), then for each query pattern
report how many times it occurs in `text` (overlaps allowed).
"""
from typing import List


class Solution:
    def count_occurrences(self, text: str, patterns: List[str]) -> List[int]:
        """Return, for each pattern, its number of (overlapping) occurrences in text.

        Args:
            text: The fixed text to search within (lowercase English letters).
            patterns: The list of query patterns.

        Returns:
            A list of ints, where result[i] is the number of times patterns[i]
            occurs as a contiguous substring of text (overlapping occurrences
            counted separately). 0 if a pattern does not occur.

        Example:
            >>> Solution().count_occurrences("banana", ["ana", "na", "ban", "xyz"])
            [2, 2, 1, 0]
        """
        # TODO: implement
        #   1. Append a unique terminal (e.g. '$') to text and build a suffix
        #      tree with Ukkonen's algorithm.
        #   2. Precompute leaf-counts for every node (one DFS).
        #   3. For each pattern, walk down the edges matching characters; the
        #      leaf count of the node/edge you land on is the answer (0 if the
        #      walk fails to match).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.count_occurrences("banana", ["ana", "na", "ban", "xyz"]))  # expected: [2, 2, 1, 0]
    print(sol.count_occurrences("aaaa", ["a", "aa", "aaa", "aaaa"]))     # expected: [4, 3, 2, 1]
    print(sol.count_occurrences("mississippi", ["issi", "ss", "ppi", "sip"]))  # expected: [2, 2, 1, 1]
