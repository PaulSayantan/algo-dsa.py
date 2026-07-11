# Rank & Select over a Sequence

**Difficulty:** Easy (foundational)

Source: Classic data-structures exercise (Navarro, *Compact Data Structures*;
the `rank`/`select` primitives underlying succinct sequences and FM-indexes).

## Description

You are given a **static** integer array `arr` of length `n`. Build a data
structure that supports the two fundamental sequence primitives, each answered
many times:

- `rank(c, i)` — return the number of positions `p` with `0 <= p < i` such that
  `arr[p] == c`. In other words, how many times value `c` occurs in the prefix
  `arr[0..i)`. (`i` is an exclusive right bound, `0 <= i <= n`.)
- `select(c, j)` — return the index (0-based) of the `j`-th occurrence of value
  `c` in `arr`, using **1-based** `j`. If fewer than `j` occurrences exist,
  return `-1`.

Your solution should preprocess `arr` once and then answer each query far faster
than the `O(n)` cost of rescanning the array. Implement a class that builds the
structure in the constructor and exposes `rank` and `select`.

`rank` and `select` are inverses of each other: `select(c, rank(c, i) )` returns
the index of the last `c` at or before position `i-1` (when one exists), and
`rank(c, select(c, j) + 1) == j`.

## Constraints

- `1 <= n <= 10^5`
- `-10^9 <= arr[i] <= 10^9` (coordinate-compress before building)
- Up to `10^5` `rank`/`select` queries.
- For `rank`: `0 <= i <= n`.
- For `select`: `j >= 1`.

## Examples

Let `arr = [4, 2, 4, 1, 4, 3, 2]` (indices `0..6`).

### Example 1
```
Input:  rank(4, 5)
Output: 3
Explanation: In the prefix arr[0..5) = [4, 2, 4, 1, 4], the value 4 occurs at
             indices 0, 2, and 4 -> 3 occurrences.
```

### Example 2
```
Input:  select(4, 3)
Output: 4
Explanation: The occurrences of 4 are at indices 0, 2, 4. The 3rd occurrence
             (1-based) is at index 4.
```

### Example 3
```
Input:  select(2, 2)
Output: 6
Explanation: The value 2 occurs at indices 1 and 6. The 2nd occurrence is at
             index 6.
```

## Hint

Build a **Wavelet Tree** over the value range. At each node store a prefix-count
of how many of the node's elements go to the left (lower-value) child; that
prefix lets you map a position down the tree in O(1) per level for `rank`, and
back up the tree for `select`.
