"""Find Beautiful Indices in the Given Array I.

Find all occurrences of `a` and of `b` in `s` (each a single-pattern search via
Boyer–Moore), then keep every occurrence index of `a` that lies within distance
`k` of some occurrence of `b`.
"""
from typing import List


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        """Return the sorted list of beautiful indices.

        An index i is beautiful if `a` occurs starting at i and some occurrence
        of `b` starts at an index j with abs(i - j) <= k.

        Args:
            s: The text to search within.
            a: The first pattern; its occurrence positions are the candidates.
            b: The second pattern; must occur within distance k of a candidate.
            k: The maximum allowed absolute distance between occurrences.

        Returns:
            Sorted list of start indices of `a` that are beautiful.

        Example:
            >>> Solution().beautifulIndices(
            ...     "isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15)
            [16, 33]
            >>> Solution().beautifulIndices("abcd", "a", "a", 4)
            [0]
        """
        # TODO: implement using Boyer–Moore to find all occurrences of a and b
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.beautifulIndices(
        "isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15))  # [16, 33]
    print(sol.beautifulIndices("abcd", "a", "a", 4))                   # [0]
