from typing import List


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        """Return the minimum total cost to build ``target`` by appending words.

        Building ``target`` means partitioning it into a sequence of dictionary
        words (repetition allowed) whose concatenation equals ``target``, while
        minimizing the summed cost. The intended approach builds an
        Aho-Corasick automaton over ``words`` and runs a DP over ``target``:
        dp[i] is the min cost to build the prefix of length i, relaxed using the
        words that end at each position (found via dictionary-suffix links).

        Args:
            target: The string to construct, length 1..5e4, lowercase letters.
            words: The available words to append; sum of lengths <= 5e4.
            costs: Parallel array; costs[i] is the cost of appending words[i].

        Returns:
            The minimum total cost, or -1 if ``target`` cannot be constructed.

        Example:
            >>> Solution().minimumCost("abcdef",
            ...     ["abdef", "abc", "d", "def", "ef"], [100, 1, 1, 10, 5])
            7
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumCost("abcdef", ["abdef", "abc", "d", "def", "ef"],
                          [100, 1, 1, 10, 5]))
    # Expected: 7
    print(sol.minimumCost("aaaa", ["z", "zz", "zzz"], [1, 10, 100]))
    # Expected: -1
    print(sol.minimumCost("abcabc", ["a", "b", "c", "abc"], [10, 10, 10, 1]))
    # Expected: 2
