"""Design a Consistent Hash Ring (with virtual nodes)."""
import bisect  # noqa: F401


class ConsistentHashRing:
    def __init__(self, vnodes: int = 3) -> None:
        # TODO: keep the ring (position -> server), a sorted list of positions,
        # and a set of node names. Use a FIXED arithmetic hash (never builtin hash()).
        pass

    def add_node(self, name: str) -> None:
        # TODO: hash `vnodes` virtual copies of `name` onto the ring
        pass

    def remove_node(self, name: str) -> None:
        # TODO: drop all ring positions owned by `name`
        pass

    def get_node(self, key: str):
        # TODO: hash the key, walk clockwise to the first ring position (wrap at end)
        pass

    def num_vnodes(self) -> int:
        # TODO
        pass

    def analyze_removal(self, keys, node: str) -> list:
        # TODO: record owners, remove `node`, count how many keys moved and whether
        # ONLY the removed node's keys moved; return [moved, only_its_keys]
        pass


if __name__ == "__main__":
    ring = ConsistentHashRing(vnodes=50)
    ring.add_node("s1")
    ring.add_node("s2")
    ring.add_node("s3")
    ring.add_node("s4")
    keys = ["key-%02d" % i for i in range(20)]
    print(ring.analyze_removal(keys, "s2"))  # expected: [4, True]
    print(ring.analyze_removal(keys, "s3"))  # expected: [4, True]
