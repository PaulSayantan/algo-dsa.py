# Estimate Jaccard Similarity

**Difficulty:** Medium

**Source:** Classic — MinHash Jaccard estimation

## Description

Using the MinHash sketch, estimate the Jaccard similarity of two sets as the fraction of signature positions where their per-hash minima coincide: `matches / k`. Implement `estimate_jaccard(s1, s2)`. The estimate is deterministic given the fixed hash family and, in expectation, equals the true Jaccard |A n B| / |A u B|.

## Examples

### Example 1

```
Input:  identical sets
Output: 1.0
```

**Explanation:** Identical sets have identical signatures, so all k positions match.

## Hint

Compare the two signatures coordinate-wise; return (#equal positions)/k as a float.
