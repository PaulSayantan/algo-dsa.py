"""Find Median from Data Stream — LeetCode 295.

Empty solution template. Fill in the body yourself.
"""


class MedianFinder:
    def __init__(self) -> None:
        """Initialize an empty median-finder structure."""
        # TODO: implement
        pass

    def addNum(self, num: int) -> None:
        """Add an integer from the data stream to the structure.

        Args:
            num: The next value from the stream.
        """
        # TODO: implement
        pass

    def findMedian(self) -> float:
        """Return the median of all values added so far.

        For an odd count this is the middle value; for an even count it is the
        mean of the two middle values.

        Returns:
            The median as a float.

        Example:
            >>> mf = MedianFinder()
            >>> mf.addNum(1)
            >>> mf.addNum(2)
            >>> mf.findMedian()
            1.5
            >>> mf.addNum(3)
            >>> mf.findMedian()
            2.0
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # expected: 1.5
    mf.addNum(3)
    print(mf.findMedian())  # expected: 2.0
