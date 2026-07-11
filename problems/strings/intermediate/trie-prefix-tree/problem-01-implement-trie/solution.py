"""LeetCode 208 - Implement Trie (Prefix Tree).

Implement a prefix tree supporting insert, exact-word search, and prefix search.
"""
from __future__ import annotations


class Trie:
    """A prefix tree over lowercase English letters.

    Example:
        >>> t = Trie()
        >>> t.insert("apple")
        >>> t.search("apple")   # True
        >>> t.search("app")     # False
        >>> t.startsWith("app") # True
    """

    def __init__(self) -> None:
        """Initialize an empty trie (a single root node with no children)."""
        # TODO: implement
        pass

    def insert(self, word: str) -> None:
        """Insert ``word`` into the trie.

        Args:
            word: A non-empty string of lowercase letters to store.

        Returns:
            None. The trie is mutated in place.
        """
        # TODO: implement
        pass

    def search(self, word: str) -> bool:
        """Return True if ``word`` was previously inserted as a complete word.

        Args:
            word: The exact word to look up.

        Returns:
            True if the full word exists in the trie, False otherwise.
        """
        # TODO: implement
        pass

    def startsWith(self, prefix: str) -> bool:
        """Return True if any inserted word has ``prefix`` as a prefix.

        Args:
            prefix: The prefix to test.

        Returns:
            True if at least one stored word begins with ``prefix``.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))     # expected: True
    print(trie.search("app"))       # expected: False
    print(trie.startsWith("app"))   # expected: True
    trie.insert("app")
    print(trie.search("app"))       # expected: True
