"""Top K Frequent Words (LeetCode 692).

Return the k most frequent words sorted by frequency descending, ties broken
alphabetically ascending. Recommended: count, then a size-k heap with a carefully designed
comparison key (the tie-break runs opposite to the frequency ordering).
"""

from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """Return the k most frequent words in the required order.

        Ordering: primarily by descending frequency; words with equal frequency are
        ordered lexicographically (ascending).

        Args:
            words: The list of lowercase words.
            k: How many of the most frequent words to return.

        Returns:
            A list of k words, highest frequency first, ties broken alphabetically.

        Example:
            topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
            -> ["i", "love"]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent(
        ["i", "love", "leetcode", "i", "love", "coding"], 2))
    # expected: ["i", "love"]
    print(sol.topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
    # expected: ["the", "is", "sunny", "day"]
