"""MinHash signature & Jaccard estimate."""
from typing import List  # noqa: F401


class MinHash:
    def __init__(self, k: int = 8) -> None:
        # TODO: seed the RNG with a FIXED int and pick k universal hashes (a, b)
        pass

    def signature(self, elements: List[int]) -> List[int]:
        # TODO: for each hash, the minimum of (a*x+b) mod p over the set
        pass

    def estimate_jaccard(self, s1: List[int], s2: List[int]) -> float:
        # TODO: fraction of signature positions where the two minima agree
        pass


if __name__ == "__main__":
    mh = MinHash(k=8)
    print(mh.estimate_jaccard([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))  # expected: 1.0
    print(mh.estimate_jaccard([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))  # expected: 0.25
    print(mh.estimate_jaccard([1, 2, 3], [10, 20, 30]))  # expected: 0.0
