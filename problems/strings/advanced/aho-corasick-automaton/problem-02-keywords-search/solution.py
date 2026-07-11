from typing import List


def count_keyword_occurrences(keywords: List[str], text: str) -> int:
    """Count total occurrences of all distinct keywords inside ``text``.

    Every occurrence at every starting index counts, occurrences may overlap,
    and duplicate keywords are collapsed to a single distinct keyword before
    counting. This is the canonical multi-pattern counting task solved by
    building one Aho-Corasick automaton over the keywords and scanning the text
    once.

    Args:
        keywords: Up to 1e4 lowercase strings, each of length 1..50. May
            contain duplicates, which should be counted only once as a keyword.
        text: A lowercase string of length up to 1e6 to scan.

    Returns:
        The total number of (distinct keyword, start index) pairs at which some
        keyword occurs in ``text``.

    Example:
        >>> count_keyword_occurrences(["she", "he", "say", "shr", "her"], "yasherhs")
        3
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(count_keyword_occurrences(["she", "he", "say", "shr", "her"], "yasherhs"))
    # Expected: 3
    print(count_keyword_occurrences(["aa", "aaa"], "aaaa"))
    # Expected: 5
    print(count_keyword_occurrences(["abc", "xyz"], "aaaaaa"))
    # Expected: 0
