# Build the Suffix Array

**Difficulty:** Medium

**Source:** Classic (SPOJ SARRAY, CP-Algorithms "Suffix Array"), foundational subroutine.

## Description

Given a string `S` of length `n`, build its **suffix array**: the array `SA` of
length `n` containing the starting indices of every suffix of `S`, sorted so that

```
S[SA[0]:] < S[SA[1]:] < ... < S[SA[n-1]:]
```

lexicographically (all suffixes of a string are distinct, so the order is strict).

`S[i:]` denotes the suffix starting at index `i` (0-indexed). Your task is to
return `SA` as a list of integers.

This is the fundamental building block for the rest of this folder. The interesting
part is doing it in **O(n log n)** or **O(n log^2 n)** rather than the naive
O(n^2 log n) that sorts the suffix strings directly.

## Constraints

- `1 <= n <= 2 * 10^5`
- `S` consists of printable ASCII characters (you may assume lowercase English
  letters for the examples, but the method should work for any comparable alphabet).
- The returned array must be a permutation of `0 .. n-1`.

## Examples

### Example 1
```
Input:  S = "banana"
Output: [5, 3, 1, 0, 4, 2]
Explanation: Sorted suffixes are
  "a"      (index 5)
  "ana"    (index 3)
  "anana"  (index 1)
  "banana" (index 0)
  "na"     (index 4)
  "nana"   (index 2)
so the suffix array lists their starting indices in that order.
```

### Example 2
```
Input:  S = "abracadabra"
Output: [10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
Explanation: The lexicographically smallest suffix is "a" (index 10), then "abra"
(index 7), then "abracadabra" (index 0) because "abra" is a proper prefix of it,
then "acadabra" (3), "adabra" (5), "bra" (8), "bracadabra" (1), "cadabra" (4),
"dabra" (6), "ra" (9), and finally "racadabra" (2).
```

### Example 3
```
Input:  S = "aaaa"
Output: [3, 2, 1, 0]
Explanation: The suffixes "a", "aa", "aaa", "aaaa" (indices 3, 2, 1, 0) are already
sorted because a shorter string is smaller than a longer one sharing its prefix.
```

## Hint

Use **Suffix Array (prefix-doubling / DC3)**: sort suffixes by their first `2^k`
characters in successive rounds, reusing the ranks computed in the previous round
so that each round only sorts *pairs of ranks* rather than whole strings.
