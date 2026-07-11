"""Document Containment Count with an FM-Index over a concatenated corpus.

Build one FM-Index over documents joined by a unique separator, then for each
pattern report how many distinct documents contain it.
"""
from typing import Dict, List


class FMIndex:
    """FM-Index supporting locate over a text (used on the joined corpus)."""

    def __init__(self, text: str) -> None:
        """Build the FM-Index for `text` (which already ends with a terminal).

        Args:
            text: The concatenated corpus, e.g. "doc1#doc2#...#docD$".
        """
        # TODO: implement
        #   Build the suffix array of `text`, the BWT, the C[] table, and the
        #   prefix-rank table occ[][]. Keep the suffix array for locate().
        pass

    def _rank(self, c: str, i: int) -> int:
        """Return occurrences of `c` in BWT[0:i] (0 if `c` is not in the text)."""
        # TODO: implement
        pass

    def locate(self, pattern: str) -> List[int]:
        """Return every start position of `pattern` in the concatenated text.

        Args:
            pattern: The pattern to locate.

        Returns:
            Unsorted-or-sorted list of 0-based positions in the concatenation;
            empty if the pattern is absent.
        """
        # TODO: backward search to get [sp, ep), then map rows to SA positions
        pass


class DocumentCorpus:
    """A collection of documents queryable for distinct-document containment."""

    def __init__(self, documents: List[str], sep: str = "#", term: str = "$") -> None:
        """Build the corpus index.

        Args:
            documents: The list of documents to index.
            sep: A separator character absent from all documents, sorting below
                letters (so no pattern spans two documents).
            term: A terminal sentinel absent from all documents, sorting below
                `sep`.
        """
        # TODO: implement
        #   1. concat = sep.join(documents) + term
        #   2. record start offset of each document (cumulative len + 1 per sep)
        #   3. self.fm = FMIndex(concat)
        pass

    def _doc_of(self, position: int) -> int:
        """Return the document id that contains concatenation index `position`.

        Args:
            position: A 0-based index into the concatenated corpus.

        Returns:
            The 0-based document id (via binary search over start offsets).
        """
        # TODO: implement (bisect over the recorded start offsets)
        pass

    def document_count(self, pattern: str) -> int:
        """Return the number of distinct documents containing `pattern`.

        Args:
            pattern: The pattern to search for.

        Returns:
            Count of distinct documents that contain `pattern` at least once.

        Example:
            >>> DocumentCorpus(["banana", "ananas", "cabana"]).document_count("ana")
            3
        """
        # TODO: implement
        #   positions = self.fm.locate(pattern)
        #   return len({ self._doc_of(p) for p in positions })
        pass


def document_counts(documents: List[str], queries: List[str]) -> List[int]:
    """Answer a batch of document-containment queries.

    Args:
        documents: The corpus.
        queries: Patterns to count documents for.

    Returns:
        A list whose i-th entry is the distinct-document count for queries[i].
    """
    # TODO: build one DocumentCorpus and map document_count() over queries
    pass


if __name__ == "__main__":
    print(document_counts(["banana", "ananas", "cabana"],
                          ["ana", "ban", "nas", "cab", "xyz"]))
    # expected: [3, 2, 1, 1, 0]
    print(document_counts(["abcabc", "bcd", "xyzabc"], ["abc", "bc", "c"]))
    # expected: [2, 3, 3]
