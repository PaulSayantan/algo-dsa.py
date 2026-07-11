# Solution — Longest Matchable Suffix

## Brute Force

Try each suffix of `P`, longest first, and test whether it occurs in `T`. There
are `m` suffixes and each substring test costs `O(n)` (naive) or `O(n + len)`
(KMP), so the total is `O(m * n)` in the worst case per query. Alternatively,
binary-search the answer length `L` and test one substring per step, giving
`O(n log m)` per query with a substring-search subroutine — still linear in `n`
each time.

- Time: `O(m * n)` (or `O(n log m)` with binary search + KMP)
- Space: `O(m)`

## Optimal Approach (FM-Index partial backward search)

Backward search is *incremental from the right*, which matches this problem
perfectly: as we prepend characters of `P` from the end, the matched string is
always a suffix of `P`, and it stays a substring of `T` exactly while the
interval `[sp, ep)` is non-empty. So we do **one** backward search and count how
many characters we consumed before the interval would empty out.

### Steps

1. Build the FM-Index over `T` (`S = T + "$"`, `SA`, `BWT`, `C[]`, rank table).
2. Initialize `sp, ep = 0, n` and `matched = 0`.
3. Iterate `c` over `P` from right to left. Tentatively update:
   ```
   nsp = C[c] + Occ(c, sp)
   nep = C[c] + Occ(c, ep)
   ```
   If `c` is not in the alphabet of `T`, or `nsp >= nep`, the current character
   cannot extend the match — **stop**.
   Otherwise commit `sp, ep = nsp, nep` and `matched += 1`.
4. Return `matched` — the length of the longest suffix of `P` present in `T`.

```python
def longest_matchable_suffix(self, pattern):
    sp, ep = 0, self.n
    matched = 0
    for c in reversed(pattern):
        if c not in self.C:
            break
        nsp = self.C[c] + self._rank(c, sp)
        nep = self.C[c] + self._rank(c, ep)
        if nsp >= nep:
            break
        sp, ep = nsp, nep
        matched += 1
    return matched
```

### Why it is correct

At every step the interval `[sp, ep)` is the block of suffixes of `S` beginning
with the current matched suffix of `P` (backward-search invariant). The interval
is non-empty **iff** that suffix occurs in `T`. Because we extend one character
at a time to the left, the matched string grows through the suffixes of `P` in
increasing length. The first character that empties the interval marks a suffix
that is *not* in `T`; every shorter suffix we already accepted *is* in `T`.
Hence `matched` is precisely the length of the longest matchable suffix. (Note we
must stop at the first failure: a failed extension means the current, longer
suffix is absent, and prepending more characters can never make an already-absent
string present.)

### Complexity

- Build: `O(n)`–`O(n log n)` time, `O(n)` space.
- Query: `O(m)` time (at most `m` steps, each two rank lookups), `O(1)` extra
  space. Independent of `n`.

## Key Insights & Edge Cases

- **Stop at first failure.** Once the interval empties, do not keep scanning: a
  longer suffix that contains an absent shorter one is also absent. Returning
  `matched` at that point is the answer.
- **Missing character:** if `c` is not in `T` at all, treat it as an immediate
  failure. In particular, if the *last* character of `P` is absent, the answer is
  `0`.
- **Full match:** if backward search consumes all of `P`, the answer is
  `len(P)` — the entire pattern is a substring of `T`.
- **Relation to matching statistics.** Running this style of backward matching
  while sliding along a query and recording, at each position, the longest match
  gives "backward matching statistics", the backbone of seed-and-extend read
  aligners. This problem is the single-shot version.
- This is strictly cheaper than the brute force because it removes the `O(n)`
  factor: the interval bookkeeping replaces re-scanning `T`.
