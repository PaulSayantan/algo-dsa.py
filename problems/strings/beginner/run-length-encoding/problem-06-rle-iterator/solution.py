"""RLE Iterator (LeetCode 900).

Iterate a run-length encoded integer sequence without expanding it. next(n)
exhausts the next n elements and returns the last one exhausted, or -1 if the
sequence runs out.
"""

from typing import List


class RLEIterator:
    def __init__(self, encoding: List[int]) -> None:
        """Initialize the iterator with a run-length encoding.

        Args:
            encoding: A flat, even-length array where each pair
                (encoding[2*i], encoding[2*i+1]) means value encoding[2*i+1]
                repeated encoding[2*i] times.
        """
        # TODO: implement
        pass

    def next(self, n: int) -> int:
        """Exhaust the next ``n`` elements and return the last one exhausted.

        Args:
            n: Number of elements to consume (n >= 1).

        Returns:
            The value of the last element exhausted, or -1 if fewer than n
            elements remain (in which case all remaining elements are consumed).

        Example:
            >>> it = RLEIterator([3, 8, 0, 9, 2, 5])
            >>> it.next(2)
            8
            >>> it.next(1)
            8
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    it = RLEIterator([3, 8, 0, 9, 2, 5])  # decodes to [8, 8, 8, 5, 5]
    print(it.next(2))  # expected: 8
    print(it.next(1))  # expected: 8
    print(it.next(1))  # expected: 5
    print(it.next(2))  # expected: -1

    big = RLEIterator([1000000000, 7])  # 1,000,000,000 copies of 7
    print(big.next(500000000))  # expected: 7
    print(big.next(400000000))  # expected: 7
    print(big.next(200000000))  # expected: -1  (only 100,000,000 remained)
