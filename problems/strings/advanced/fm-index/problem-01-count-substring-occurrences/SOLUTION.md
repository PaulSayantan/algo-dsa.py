# Solution — Count Substring Occurrences

## Brute Force

For each query `P`, scan `T` and count matches. Using naive matching this is
`O(n * m)` per query; with KMP it is `O(n + m)` per query. Across `q` queries the
total is `O(q * (n + m))`. When `n` is large and there are many queries, the
repeated `O(n)` factor is the bottleneck: every query re-reads the whole text.

- Time: `O(q * (n + m))`
- Space: `O(m)` per query (plus the text)

## Optimal Approach (FM-Index + Backward Search)

Build a single index once, then answer each query in `O(m)` — no dependence on
`n` at query time.

### Building the index

1. Append a sentinel `$` that is smaller than every real character:
   `S = T + "$"`, length `n`.
2. Build the **suffix array** `SA` of `S` (SA-IS in `O(n)`, or prefix-doubling in
   `O(n log n)`; even Python's `sorted` on suffixes is fine for teaching).
3. The **Burrows–Wheeler Transform** is the last column of the sorted rotation
   matrix; using the suffix array, `BWT[i] = S[(SA[i] - 1) mod n]`.
4. Precompute two tables over `BWT`:
   - `C[c]` = number of characters in `S` strictly smaller than `c`. This is the
     index of the first suffix-array row starting with `c`.
   - `Occ(c, i)` = number of `c` in `BWT[0:i]` (a *rank* query). For teaching,
     store a full prefix table `occ[c][0..n]`.

### Backward search

The core identity is the **LF-mapping**: the `k`-th occurrence of `c` in the last
column (`L = BWT`) corresponds to the `k`-th occurrence of `c` in the first
column (`F`), because both columns list the same characters in the same relative
order. Reading `P` right to left, maintain a half-open interval `[sp, ep)` of
sorted-suffix rows that begin with the pattern suffix seen so far:

```
sp, ep = 0, n
for c in reversed(P):
    sp = C[c] + Occ(c, sp)
    ep = C[c] + Occ(c, ep)
    if sp >= ep:
        return 0          # pattern absent
return ep - sp            # number of occurrences
```

Each character does two rank lookups, so a query is `O(m)` with `O(1)` rank (or
`O(m log sigma)` with a wavelet tree). The final interval width `ep - sp` is
exactly the number of suffixes of `S` that start with `P` — i.e. the number of
occurrences of `P` in `T`.

### Why it is correct

The rows of the sorted rotation matrix are the suffixes of `S` in lexicographic
order. All suffixes beginning with a given string `W` form a **contiguous block**
of rows. Backward search maintains the invariant that `[sp, ep)` is exactly the
block of suffixes beginning with the current pattern suffix. Prepending character
`c` and applying `C[c] + Occ(c, .)` moves from "rows starting with `W`" to "rows
starting with `cW`" — this is the LF-mapping restricted to the interval. By
induction, after the whole pattern the interval is the block of all suffixes that
begin with `P`.

### Reference implementation

```python
class FMIndex:
    def __init__(self, text, sentinel="$"):
        self.s = text + sentinel
        self.n = len(self.s)
        sa = sorted(range(self.n), key=lambda i: self.s[i:])   # O(n^2 log n) naive; use SA-IS in practice
        self.sa = sa
        self.bwt = "".join(self.s[(sa[i] - 1) % self.n] for i in range(self.n))
        self.alphabet = sorted(set(self.s))
        # C[]
        counts = {c: self.bwt.count(c) for c in self.alphabet}
        self.C, total = {}, 0
        for c in self.alphabet:
            self.C[c] = total
            total += counts[c]
        # prefix rank table
        self.occ = {c: [0] * (self.n + 1) for c in self.alphabet}
        for i, ch in enumerate(self.bwt):
            for c in self.alphabet:
                self.occ[c][i + 1] = self.occ[c][i] + (1 if ch == c else 0)

    def _rank(self, c, i):
        return self.occ[c][i] if c in self.occ else 0

    def count(self, pattern):
        sp, ep = 0, self.n
        for c in reversed(pattern):
            if c not in self.C:
                return 0
            sp = self.C[c] + self._rank(c, sp)
            ep = self.C[c] + self._rank(c, ep)
            if sp >= ep:
                return 0
        return ep - sp
```

### Complexity

- Build: `O(n)`–`O(n log n)` time (dominated by the suffix array), `O(n)` space
  for the teaching version (a real FM-Index compresses rank tables to
  `n H_k + o(n log sigma)` bits).
- Query `count(P)`: `O(m)` time with `O(1)` rank, `O(1)` extra space.

## Key Insights & Edge Cases

- **Sentinel `$`** must be strictly smaller than every text character and appear
  exactly once; it makes all rotations distinct and pins the suffix ordering to
  the suffix ordering of `T`.
- **Half-open intervals** `[sp, ep)` make the width `ep - sp` the count directly
  and keep the empty test as `sp >= ep`.
- **Unknown character:** if a pattern character never appears in `T`, `C` has no
  entry (or rank is 0 everywhere) — return `0` immediately.
- **Overlaps are counted**, because two overlapping occurrences are two distinct
  suffixes starting with `P`, hence two distinct rows in the interval.
- **Pattern longer than the text** simply produces an empty interval during the
  search and returns `0`.
- The plain prefix-rank table is `O(n * sigma)` space; for large alphabets use a
  **wavelet tree** so rank is `O(log sigma)` and space is `O(n log sigma)` bits.
