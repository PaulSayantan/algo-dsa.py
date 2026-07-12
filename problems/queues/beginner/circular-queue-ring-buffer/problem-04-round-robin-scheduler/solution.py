"""Round-Robin Task Scheduler — cycle tasks with a modulo-wrapping head index."""
from typing import List  # noqa: F401


class RoundRobin:
    def __init__(self, tasks: List[str]) -> None:
        # TODO: store the task list, its length, and a head cursor at 0
        pass

    def next(self) -> str:
        # TODO: read the task at head, then advance head as (head + 1) % n
        pass

    def peek(self) -> str:
        # TODO: return the task at head without advancing
        pass


if __name__ == "__main__":
    rr = RoundRobin(["A", "B", "C"])
    print(rr.next())  # expected: 'A'
    print(rr.next())  # expected: 'B'
    print(rr.next())  # expected: 'C'
    print(rr.next())  # expected: 'A'
    print(rr.peek())  # expected: 'B'
