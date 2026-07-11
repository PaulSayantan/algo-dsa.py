"""Minimum Cost to Convert String I.

LeetCode 2976. Solve with Floyd–Warshall over the 26-letter alphabet graph.
"""

from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        """Return the minimum total cost to convert ``source`` into ``target``.

        Model each of the 26 lowercase letters as a node and each conversion rule
        ``original[i] -> changed[i]`` as a directed edge weighted ``cost[i]``. Compute
        the cheapest cost between every pair of letters with Floyd–Warshall, then sum
        the per-position conversion costs. Return -1 if any needed conversion has no
        finite-cost path.

        Args:
            source: The starting string.
            target: The desired string (same length as ``source``).
            original: Source characters of each conversion rule.
            changed: Destination characters of each conversion rule.
            cost: Cost of each conversion rule (parallel to ``original``/``changed``).

        Returns:
            The minimum total conversion cost, or -1 if conversion is impossible.

        Example:
            >>> Solution().minimumCost(
            ...     "abcd", "acbe",
            ...     ["a", "b", "c", "c", "e", "d"],
            ...     ["b", "c", "b", "e", "b", "e"],
            ...     [2, 5, 5, 1, 2, 20],
            ... )
            28
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.minimumCost(
            "abcd",
            "acbe",
            ["a", "b", "c", "c", "e", "d"],
            ["b", "c", "b", "e", "b", "e"],
            [2, 5, 5, 1, 2, 20],
        )
    )
    # Expected: 28
    print(sol.minimumCost("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]))
    # Expected: 12
    print(sol.minimumCost("abcd", "abce", ["a"], ["e"], [10000]))
    # Expected: -1
