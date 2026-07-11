"""Longest Common Path.

Fill in `longest_common_path` so it returns the longest directory prefix shared by every
path, aligned on whole `/`-separated segments.
"""
from __future__ import annotations

from typing import List


def longest_common_path(paths: List[str]) -> str:
    """Return the longest common path prefix, aligned on whole segments.

    Args:
        paths: A non-empty list of absolute Unix-style paths (each begins with "/").

    Returns:
        The longest common directory as a normalized path string. Returns "/" when the
        paths share no leading segment.

    Example:
        >>> longest_common_path(["/usr/local/bin", "/usr/local/lib"])
        '/usr/local'
        >>> longest_common_path(["/a/b/c", "/x/y/z"])
        '/'
    """
    # TODO: implement
    #   1. Split each path into non-empty segments.
    #   2. Vertical-scan the segment columns (or binary search on segment count).
    #   3. Join the common segments back into "/" + "/".join(...).
    pass


if __name__ == "__main__":
    print(longest_common_path(["/usr/local/bin", "/usr/local/lib", "/usr/local/bin/python"]))
    # expected: "/usr/local"
    print(longest_common_path(["/usr/lib", "/usr/libexec"]))          # expected: "/usr"
    print(longest_common_path(["/a/b/c", "/x/y/z"]))                  # expected: "/"
    print(longest_common_path(["/data/logs", "/data/logs/2026", "/data/logs/2026/07"]))
    # expected: "/data/logs"
