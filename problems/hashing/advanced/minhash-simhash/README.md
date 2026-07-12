# MinHash & SimHash (Similarity)

Similarity sketches let you estimate how alike two sets or documents are from tiny fixed-size fingerprints instead of comparing them directly. **MinHash** keeps, for each of k fixed hash functions, the minimum hash over a set; the probability two sets share a given minimum equals their Jaccard similarity, so the fraction of matching signature positions estimates Jaccard. **SimHash** projects a document's token multiset onto a 64-bit fingerprint via weighted bit-votes; similar documents have fingerprints a small Hamming distance apart. Both are locality-sensitive and, with fixed hash constants and seeds, fully deterministic — the engines behind near-duplicate detection and clustering at web scale.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [MinHash Signature](problem-01-minhash-signature/PROBLEM.md) | Min-of-hash signature | Medium |
| 2 | [Estimate Jaccard Similarity](problem-02-estimate-jaccard/PROBLEM.md) | Jaccard from signatures | Medium |
| 3 | [SimHash Hamming Distance](problem-03-simhash-hamming/PROBLEM.md) | Fingerprint + popcount | Medium |
