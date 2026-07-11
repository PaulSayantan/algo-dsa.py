from typing import List


class StreamChecker:
    """Online matcher: after each streamed character, is some word a suffix?

    Build an Aho-Corasick automaton over ``words`` once, then keep a single
    "current node" that advances by one transition per query. A word is a
    suffix of the stream-so-far exactly when the current node is terminal or
    reaches a terminal node through dictionary-suffix links; precompute a
    per-node boolean so each query is O(1).
    """

    def __init__(self, words: List[str]) -> None:
        """Initialize the checker with the dictionary of words.

        Args:
            words: 1..2000 lowercase strings, each of length 1..200.
        """
        # TODO: implement
        pass

    def query(self, letter: str) -> bool:
        """Consume the next stream character and test the suffix condition.

        Args:
            letter: A single lowercase English letter appended to the stream.

        Returns:
            True if any word in the dictionary is a suffix of the stream of
            characters queried so far, else False.

        Example:
            >>> sc = StreamChecker(["cd", "f", "kl"])
            >>> [sc.query(c) for c in "abcd"]
            [False, False, False, True]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sc = StreamChecker(["cd", "f", "kl"])
    print([sc.query(c) for c in "abcdefghijkl"])
    # Expected: [False, False, False, True, False, True, False, False, False,
    #            False, False, True]

    sc2 = StreamChecker(["ab", "ba"])
    print([sc2.query(c) for c in "aabab"])
    # Expected: [False, False, True, True, True]
