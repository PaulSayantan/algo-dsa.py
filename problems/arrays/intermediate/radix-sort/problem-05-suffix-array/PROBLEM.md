# Build a Suffix Array

**Difficulty:** Hard

**Source:** Classic (competitive programming — prefix-doubling suffix array
construction; e.g. SPOJ SARRAY, CP-Algorithms "Suffix Array")

## Description

The **suffix array** of a string `s` of length `n` is the array of starting
indices of all `n` suffixes of `s`, sorted in ascending lexicographic order.

Given a lowercase string `s`, return its suffix array: a list of `n` integers
where the `i`-th value is the starting index of the `i`-th smallest suffix.

Sorting the suffixes naively is expensive because comparing two suffixes can
take `O(n)` time. The standard efficient construction uses **prefix doubling**:
at step `k` you know the sorted order of all suffixes by their first `2^(k-1)`
characters; you then sort by the first `2^k` characters by treating each suffix
as a **pair of ranks** `(rank of first half, rank of second half)` and sorting
those pairs. Sorting integer pairs is exactly a two-pass radix sort, giving
`O(n log n)` overall.

## Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists of lowercase English letters `'a'`–`'z'`
- Return the indices of all `n` suffixes (a permutation of `0..n-1`)

## Examples

### Example 1

```
Input:  s = "banana"
Output: [5, 3, 1, 0, 4, 2]
Explanation: The suffixes and their start indices are:
  5: "a"
  3: "ana"
  1: "anana"
  0: "banana"
  4: "na"
  2: "nana"
Sorted lexicographically they appear in the order above, giving indices
[5, 3, 1, 0, 4, 2].
```

### Example 2

```
Input:  s = "abab"
Output: [2, 0, 3, 1]
Explanation: Suffixes sorted lexicographically:
  2: "ab"
  0: "abab"
  3: "b"
  1: "bab"
Note "ab" < "abab" because "ab" is a proper prefix of "abab" (shorter wins), and
"b" < "bab" for the same reason.
```

### Example 3

```
Input:  s = "aaa"
Output: [2, 1, 0]
Explanation: Suffixes "a" (index 2), "aa" (index 1), "aaa" (index 0). A shorter
string that is a prefix of a longer one sorts first, so the order is 2, 1, 0.
```

## Hint

Use **Radix Sort** inside a prefix-doubling loop: represent each suffix by the
pair `(rank_first_half, rank_second_half)` and stably radix-sort those pairs
(sort by the second element, then by the first). Doubling the compared prefix
length each round gives `O(log n)` rounds of linear-time radix sort.
