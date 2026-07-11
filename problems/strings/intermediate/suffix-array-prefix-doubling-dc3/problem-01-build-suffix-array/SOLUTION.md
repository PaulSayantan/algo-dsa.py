# Solution — Build the Suffix Array

## Brute Force

Generate all `n` suffixes as actual strings and sort them, then read off their
start indices.

```python
def build_suffix_array_naive(s):
    return sorted(range(len(s)), key=lambda i: s[i:])
```

- Building each suffix key and comparing costs up to O(n) characters.
- Python's Timsort does O(n log n) comparisons, each up to O(n) work.
- **Time:** O(n^2 log n) worst case. **Space:** O(n^2) for the materialized keys.

Fine as a reference oracle for testing, but far too slow / memory-hungry for
`n = 2 * 10^5`.

## Optimal Approach — Prefix Doubling

**Idea.** Instead of comparing full suffixes, sort them by their first `2^k`
characters in round `k = 0, 1, 2, ...`. Crucially, after round `k` we know the
*rank* of every suffix based on its first `2^k` characters. In round `k+1` the
key of suffix `i` for its first `2^(k+1)` characters is the **pair**
`(rank_k[i], rank_k[i + 2^k])` — the rank of its first half followed by the rank
of its second half (use a sentinel rank `-1` when `i + 2^k` runs past the end).
Sorting by these integer pairs is far cheaper than comparing strings, and after
`ceil(log2 n)` rounds every `2^k >= n`, so each suffix has a unique rank and the
order is final.

**Why it is correct.** Lexicographic order of two suffixes is decided by their
first differing character. After round `k`, `rank_k[i]` orders suffixes correctly
by their first `2^k` characters (ties get equal rank). The pair
`(rank_k[i], rank_k[i+2^k])` compares the first `2^k` chars, and on a tie the next
`2^k` chars — i.e. the first `2^(k+1)` chars. By induction, once `2^k >= n` the
key covers the entire suffix, so ranks are a strict total order equal to the true
suffix order.

**Steps.**
1. Initialize `rank[i] = ord(s[i])` (rank by the first character) and `sa` = indices sorted by `rank`.
2. For `k` with step `= 1, 2, 4, ...` while step `< n`:
   - Sort `sa` by the pair key `(rank[i], rank[i+step] if i+step < n else -1)`.
   - Recompute a new `rank` array by scanning the sorted order and giving equal
     consecutive keys the same rank, incrementing when the key changes.
   - If the largest new rank is `n-1`, all suffixes are distinct — stop early.
3. Return `sa`.

```python
def build_suffix_array(s):
    n = len(s)
    sa = list(range(n))
    rank = [ord(c) for c in s]
    tmp = [0] * n
    step = 1
    while True:
        # key: (rank[i], rank[i+step] or -1)
        def key(i):
            return (rank[i], rank[i + step] if i + step < n else -1)
        sa.sort(key=key)                       # O(n log n) comparisons
        tmp[sa[0]] = 0
        for j in range(1, n):
            tmp[sa[j]] = tmp[sa[j - 1]] + (key(sa[j]) != key(sa[j - 1]))
        rank = tmp[:]                          # copy new ranks
        if rank[sa[-1]] == n - 1:              # all ranks unique
            break
        step <<= 1
        if step >= n:
            break
    return sa
```

- Each round runs one comparison sort: O(n log n). There are O(log n) rounds.
- **Time:** O(n log^2 n) with a comparison sort; O(n log n) if you replace the
  sort with **radix / counting sort** on the integer pairs (ranks are in `0..n`).
- **Space:** O(n).

### Linear-time alternative — DC3 / skew

The DC3 (Difference Cover mod 3, a.k.a. skew) algorithm builds the suffix array
in true **O(n)**:
1. Sort the "sample" suffixes at positions `i mod 3 != 0` by their first three
   characters (radix sort), assign them ranks, and if any tie remains, **recurse**
   on a string of those ranks (length ~ 2n/3).
2. From the recursive result, derive the sorted order of all sample suffixes.
3. Sort the remaining suffixes (`i mod 3 == 0`) using the sample ranks (radix sort by `(s[i], rank[i+1])`).
4. **Merge** the two sorted groups; comparisons between a `mod 0` and a `mod 1/2`
   suffix resolve in O(1) using precomputed ranks.

`T(n) = T(2n/3) + O(n) = O(n)`. It has a larger constant and more code than prefix
doubling, so contests usually prefer doubling + radix sort unless linear time is
strictly required.

## Key Insights & Edge Cases

- **Reusing ranks is the whole trick**: comparing pairs of integers instead of
  strings turns an O(n) comparison into O(1).
- **Sentinel for the second half**: when `i + step >= n`, use a rank smaller than
  any real rank (`-1`), reflecting that a shorter suffix is lexicographically smaller.
- **Early exit** when all ranks become distinct saves rounds on low-repetition input.
- **Single character / empty-ish input**: `n = 1` returns `[0]`; make sure the
  loop handles `step >= n` immediately.
- **Ties everywhere (`"aaaa"`)**: needs all `log n` rounds because ranks stay tied
  the longest; the result is `[n-1, ..., 1, 0]`.
- For O(n log n), radix-sort by the *second* key first then the *first* key
  (LSD radix), since ranks fit in `0..n`.
