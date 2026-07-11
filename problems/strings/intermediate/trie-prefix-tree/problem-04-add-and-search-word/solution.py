"""LeetCode 211 - Design Add and Search Words Data Structure.

Support adding words and searching with '.' as a single-character wildcard.
"""
from __future__ import annotations


class WordDictionary:
    """A word store supporting exact and '.'-wildcard searches.

    Example:
        >>> wd = WordDictionary()
        >>> wd.addWord("bad")
        >>> wd.search("bad")   # True
        >>> wd.search(".ad")   # True
        >>> wd.search("b..")   # True
    """

    def __init__(self) -> None:
        """Initialize an empty word dictionary."""
        # TODO: implement
        pass

    def addWord(self, word: str) -> None:
        """Add ``word`` (lowercase letters only) to the dictionary.

        Args:
            word: The word to store.

        Returns:
            None. The structure is mutated in place.
        """
        # TODO: implement
        pass

    def search(self, word: str) -> bool:
        """Return True if any stored word matches ``word``.

        A '.' in ``word`` matches any single letter. Matching also requires the
        lengths to be equal (the pattern must land exactly on a word-end node).

        Args:
            word: The query pattern; may contain '.' wildcards.

        Returns:
            True if some added word matches the pattern, else False.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    wd = WordDictionary()
    for w in ("bad", "dad", "mad"):
        wd.addWord(w)
    print(wd.search("pad"))   # expected: False
    print(wd.search("bad"))   # expected: True
    print(wd.search(".ad"))   # expected: True
    print(wd.search("b.."))   # expected: True
