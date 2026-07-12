# Design a Bloom Filter

**Difficulty:** Medium

**Source:** Classic — Bloom filter (probabilistic membership)

## Description

Implement a Bloom filter over integers with a bit array of size `m` and `k` hash functions `h_s(x) = (x * 2654435761 + s * 40503) mod m` for `s = 1..k`. Support `add(x)` (set the `k` bits) and `contains(x)` (true iff all `k` bits are set). Added items must always report present; an unadded item may report present only if it collides on all `k` bits (a false positive).

## Examples

### Example 1

```
Input:  add 10,20,30; contains(10)
Output: True
```

**Explanation:** Added items never give a false negative.

### Example 2

```
Input:  contains(110)
Output: True
```

**Explanation:** False positive: 110 hashes to bits {13,16,19}, exactly the bits 10 set.

## Hint

add sets h_1..h_k to 1; contains is all() over the same k positions. No false negatives.
