"""Round-robin load balancer: hand out servers cyclically with add/remove."""


class RoundRobinBalancer:
    def __init__(self) -> None:
        # TODO: a list of server ids and a cursor index
        pass

    def addServer(self, server_id: int) -> None:
        # TODO: append to the rotation
        pass

    def removeServer(self, server_id: int) -> None:
        # TODO: remove it; keep the cursor pointing at the same next server
        pass

    def next(self) -> int:
        # TODO: return servers[idx] and advance the cursor, or -1 if empty
        pass


if __name__ == "__main__":
    b = RoundRobinBalancer()
    b.addServer(10)
    b.addServer(20)
    b.addServer(30)
    print(b.next())  # expected: 10
    print(b.next())  # expected: 20
    print(b.next())  # expected: 30
    print(b.next())  # expected: 10
    b.removeServer(20)
    print(b.next())  # expected: 30
    print(b.next())  # expected: 10
    print(b.next())  # expected: 30

    c = RoundRobinBalancer()
    print(c.next())  # expected: -1
    c.addServer(1)
    print(c.next())  # expected: 1
    print(c.next())  # expected: 1
    c.addServer(2)
    print(c.next())  # expected: 1
    print(c.next())  # expected: 2
