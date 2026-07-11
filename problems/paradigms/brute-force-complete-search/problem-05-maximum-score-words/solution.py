"""Maximum Score Words Formed by Letters — Brute Force practice template.

Fill in the body of `max_score_words`. Do NOT look at SOLUTION.md until you have
tried.
"""
from typing import List


class Solution:
    def max_score_words(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        """Return the maximum total score of any subset of words that can be
        formed using each available letter at most once.

        Args:
            words: Candidate words (at most 14). Each is used whole or not at all.
            letters: Multiset of available lowercase letters (each usable once).
            score: Length-26 list; score[i] is the value of chr(ord('a') + i).

        Returns:
            The highest achievable total score over all feasible word subsets.
            Returns 0 if no word can be formed (the empty subset is always valid).

        Example:
            >>> s = [0]*26
            >>> for ch, v in {'a':1, 'c':9, 'd':5, 'g':3}.items():
            ...     s[ord(ch) - 97] = v
            >>> Solution().max_score_words(
            ...     ["dog", "cat", "dad", "good"],
            ...     ["a","a","c","d","d","d","g","o","o"], s)
            19
        """
        # TODO: implement using Brute Force / Complete Search
        # (iterate every subset via a bitmask in range(1 << len(words)),
        #  tally the letters each subset needs, discard infeasible subsets,
        #  and keep the maximum score).
        pass


if __name__ == "__main__":
    sol = Solution()

    score1 = [0] * 26
    for ch, v in {"a": 1, "c": 9, "d": 5, "g": 3}.items():
        score1[ord(ch) - 97] = v
    print(sol.max_score_words(
        ["dog", "cat", "dad", "good"],
        ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
        score1,
    ))  # expected: 19

    score2 = [0] * 26
    for ch, v in {"a": 4, "b": 4, "c": 4, "x": 5, "z": 10}.items():
        score2[ord(ch) - 97] = v
    print(sol.max_score_words(
        ["xxxz", "ax", "bx", "cx"],
        ["z", "a", "b", "c", "x", "x", "y", "y"],
        score2,
    ))  # expected: 18
