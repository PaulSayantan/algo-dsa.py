"""Design Underground System — LeetCode 1396."""
from collections import defaultdict  # noqa: F401


class UndergroundSystem:
    def __init__(self) -> None:
        # TODO: id -> (startStation, startTime); (start,end) -> [totalTime, count]
        pass

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # TODO
        pass

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # TODO
        pass

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # TODO: total travel time / number of trips
        pass


if __name__ == "__main__":
    us = UndergroundSystem()
    us.checkIn(45, "A", 3)
    us.checkOut(45, "B", 8)
    print(us.getAverageTime("A", "B"))  # expected: 5.0
    us.checkIn(10, "A", 10)
    us.checkOut(10, "B", 15)
    print(us.getAverageTime("A", "B"))  # expected: 5.0
    us.checkIn(27, "A", 20)
    us.checkOut(27, "B", 31)
    print(us.getAverageTime("A", "B"))  # expected: 7.0
