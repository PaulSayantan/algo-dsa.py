"""SimHash fingerprint & Hamming distance."""
from typing import List  # noqa: F401


class SimHash:
    def fingerprint(self, tokens: List[str]) -> int:
        # TODO: weighted bit-vote over a FIXED 64-bit arithmetic token hash,
        # then set bit i iff its vote is positive
        pass

    def hamming_distance(self, doc1: List[str], doc2: List[str]) -> int:
        # TODO: popcount of the XOR of the two fingerprints
        pass


if __name__ == "__main__":
    sh = SimHash()
    print(sh.hamming_distance(["the", "cat", "sat"], ["the", "cat", "sat"]))  # expected: 0
    print(sh.hamming_distance(["the", "cat", "sat"], ["the", "dog", "ran"]))  # expected: 33
    print(sh.hamming_distance(["a", "b", "c", "d"], ["a", "b", "c", "e"]))  # expected: 2
