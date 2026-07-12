# SimHash Hamming Distance

**Difficulty:** Medium

**Source:** Classic — Charikar SimHash

## Description

Implement a 64-bit SimHash over a token multiset using a **fixed** arithmetic (FNV-1a) hash per token: for each token add its weight to bit positions where its hash has a 1 and subtract where it has a 0; the fingerprint sets bit i iff the accumulated vote at i is positive. `hamming_distance(doc1, doc2)` returns the number of differing fingerprint bits. Similar documents yield small distances; the value is fully deterministic.

## Examples

### Example 1

```
Input:  identical token lists
Output: 0
```

**Explanation:** Identical documents produce identical fingerprints.

## Hint

Weighted bit-vote over each token's 64-bit hash; distance = popcount(fp1 XOR fp2).
