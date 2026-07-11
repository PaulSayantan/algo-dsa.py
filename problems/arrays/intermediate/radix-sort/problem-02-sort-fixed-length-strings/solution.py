from typing import List


def sort_fixed_length_strings(words: List[str]) -> List[str]:
    """Sort equal-length lowercase strings lexicographically via radix sort.

    Every string in ``words`` has the same length ``L`` and contains only
    lowercase English letters. Treat each character position as a digit over a
    26-symbol alphabet and apply a stable counting sort per position, from the
    last character (least significant) to the first (most significant).

    Args:
        words: List of strings, all of identical length ``L``, each character in
            ``'a'``..``'z'``. Duplicates are allowed.

    Returns:
        A new list containing the same strings in ascending lexicographic order.

    Example:
        >>> sort_fixed_length_strings(["cba", "abc", "bca", "aaa"])
        ['aaa', 'abc', 'bca', 'cba']
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(sort_fixed_length_strings(["cba", "abc", "bca", "aaa"]))
    # Expected: ['aaa', 'abc', 'bca', 'cba']
    print(sort_fixed_length_strings(["dog", "cat", "cow", "cab"]))
    # Expected: ['cab', 'cat', 'cow', 'dog']
    print(sort_fixed_length_strings(["ba", "ab", "ba", "aa"]))
    # Expected: ['aa', 'ab', 'ba', 'ba']
