# Solution — K-th Smallest Distinct Substring

## Brute Force

Generate every substring, deduplicate with a set, sort the set
lexicographically, and index into it. Generating and storing is **O(n^2)**
substrings of total length **O(n^3)**, and sorting is `O(n^2 log n)` string
comparisons. Both time and space are `O(n^2)` at best — impossible for
`n = 10^5`.

## Optimal Approach (Suffix Array + LCP / Kasai)

**Two facts make this a linear scan:**

1. Iterating the suffix array in sorted order visits the suffixes — and hence
   their prefixes — in lexicographic order. All distinct substrings, sorted, are
   exactly the concatenation, in `SA` order, of the *new* prefixes each suffix
   introduces.
2. Sorted suffix `i` (length `n - SA[i]`) shares its first `LCP[i]` characters
   with the previous sorted suffix, so those short prefixes were already
   emitted. It contributes

   ```
   new(i) = (n - SA[i]) - LCP[i]
   ```

   brand-new distinct substrings, and they are the prefixes of lengths
   `LCP[i] + 1, LCP[i] + 2, ..., n - SA[i]`.

Walk the suffix array accumulating `new(i)`. As soon as the running total would
reach `k`, the answer lies in this suffix's block. If `need = k - (total so far)`
(a `1`-based offset into this block), then the answer has length
`LCP[i] + need` and is the prefix `s[SA[i] : SA[i] + LCP[i] + need]`.

### Steps

1. Build `SA` (`O(n log n)`) and `LCP` via Kasai (`O(n)`).
2. `cum = 0`. For each `i` in `0..n-1`:
   - `new = (n - SA[i]) - LCP[i]`
   - if `cum + new >= k`: `need = k - cum`; return
     `s[SA[i] : SA[i] + LCP[i] + need]`
   - else `cum += new`.
3. If the loop ends, `k` is too large: return `"-1"`.

```python
def kth_smallest_distinct_substring(s, k):
    n = len(s)
    sa = build_suffix_array(s)
    lcp = build_lcp_kasai(s, sa)
    cum = 0
    for i in range(n):
        new = (n - sa[i]) - lcp[i]
        if cum + new >= k:
            need = k - cum                 # 1..new
            length = lcp[i] + need
            return s[sa[i]:sa[i] + length]
        cum += new
    return "-1"
```

### Worked check on "dbac", k = 3

`SA = [2, 1, 3, 0]` (suffixes `ac, bac, c, dbac`), `LCP = [0, 0, 0, 0]`.

- i=0 (`ac`): new = (4-2) - 0 = 2, prefixes `a`(1), `ac`(2). cum -> 2, still < 3.
- i=1 (`bac`): new = (4-1) - 0 = 3, prefixes `b`(3), `ba`(4), `bac`(5).
  cum + new = 5 >= 3, so need = 3 - 2 = 1, length = 0 + 1 = 1 -> `s[1:2] = "b"`.

Matches the expected output `"b"`.

### Complexity

- Suffix array: **O(n log n)** time, **O(n)** space.
- Kasai LCP + single scan: **O(n)** time, **O(n)** space.
- Overall: **O(n log n)** time, **O(n)** space. Answering the query itself is a
  single `O(n)` pass; if many queries are asked on the same string, precompute
  the prefix sums of `new(i)` once and binary-search each query in `O(log n)`.

## Key Insights & Edge Cases

- **`new(i)` can be zero** when `LCP[i] == n - SA[i]` (the whole current suffix
  is a prefix of the previous one — impossible for distinct suffixes unless
  there is a repeat, but the subtraction still correctly contributes 0). The
  code simply skips such suffixes.
- **`k` out of range:** if the accumulated count never reaches `k`, there are
  fewer than `k` distinct substrings; return `"-1"`. The total equals
  `n(n+1)/2 - sum(LCP)`.
- **1-indexing:** `need` ranges `1..new`, so `length = LCP[i] + need` is at least
  `LCP[i] + 1`, correctly skipping the already-counted shared prefix.
- **Large `k` (up to `10^9`):** use 64-bit accumulation in fixed-width languages.
- The same scan, with `new(i)` as prefix sums, powers repeated
  "lexicographic substring search" queries (SPOJ SUBLEX).
