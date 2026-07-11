class MedianFinder:
    """Maintain a running median over a stream of integers.

    Suggested design (two heaps):
      - a max-heap ``lo`` holding the smaller half (in ``heapq``, store
        negated values so the largest of the small half is at the root),
      - a min-heap ``hi`` holding the larger half,
      - keep the sizes balanced to within 1 after every insertion.

    Then ``findMedian`` reads the root(s) in O(1):
      - if one heap is larger, its extreme is the median,
      - if the sizes are equal, average the two roots.
    """

    def __init__(self) -> None:
        """Initialize the data structure."""
        # TODO: implement (e.g. self.lo = [] ; self.hi = [])
        pass

    def addNum(self, num: int) -> None:
        """Add ``num`` to the stream, keeping the two heaps balanced.

        Args:
            num: The integer to insert.

        Returns:
            None.
        """
        # TODO: implement
        pass

    def findMedian(self) -> float:
        """Return the median of all elements added so far.

        Returns:
            The median as a float: the middle value for an odd count, or the
            average of the two middle values for an even count.

        Example:
            After addNum(1), addNum(2): findMedian() == 1.5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())   # expected: 1.5
    mf.addNum(3)
    print(mf.findMedian())   # expected: 2.0
