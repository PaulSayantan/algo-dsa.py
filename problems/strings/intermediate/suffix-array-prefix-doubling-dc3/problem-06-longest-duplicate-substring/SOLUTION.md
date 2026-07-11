# Solution — Longest Duplicate Substring (LeetCode 1044)

## Brute Force

Enumerate every pair of start indices and extend the common prefix, tracking the
longest, or check every candidate length by materializing all substrings of that
length in a set.

- Pair extension: O(n^2) pairs × O(n) extension = O(n^3).
- Set of all length-`L` substrings for each `L`: O(n^2) time and O(n^2) space in the
  worst case (each substring is O(n) to build).
- **Time:** O(n^3) / O(n^2). **Space:** O(n^2). Too slow for `n = 3 * 10^4`.

## Optimal Approach — Suffix Array + LCP

**Idea (identical core to "longest repeated substring").** A duplicated substring
is a common prefix of two distinct suffixes. Sort the suffixes (suffix array) and
compute the LCP array. The longest duplicated substring has length `max(LCP)`, and
it is the first `max(LCP)` characters of the corresponding suffix. Adjacent sorted
suffixes are the ones that can share the longest prefixes, so the global maximum is
attained between some adjacent pair.

**Why correct.** If a string `w` of length `L` occurs at positions `p` and `q`, then
suffixes `s[p:]` and `s[q:]` both start with `w`, and after sorting, every suffix
between them shares the prefix `w`. Hence some adjacent pair in `SA` has
`LCP >= L`. Conversely any adjacent LCP of value `L` exhibits a substring of length
`L` occurring at two positions. So `answer length = max adjacent LCP`.

**Steps.**
1. `SA = build_suffix_array(s)` — prefix doubling, O(n log n) / O(n log^2 n).
2. `LCP = kasai(s, SA)` — O(n).
3. `i = argmax(LCP)`; if `LCP[i] == 0` return `""`.
4. Return `s[SA[i] : SA[i] + LCP[i]]`.

```python
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        sa = build_suffix_array(s)
        lcp = kasai(s, sa)                 # lcp[i] = LCP(sa[i-1], sa[i]), lcp[0]=0
        best_len, best_pos = 0, 0
        for i in range(1, n):
            if lcp[i] > best_len:
                best_len, best_pos = lcp[i], sa[i]
        return s[best_pos: best_pos + best_len]
```

- **Time:** O(n log n) (or O(n log^2 n) with a comparison-sort doubling build).
- **Space:** O(n).

### Alternative accepted on LeetCode — Binary Search + Rabin-Karp

Binary-search the answer length `L` in `[1, n-1]`. For a fixed `L`, slide a rolling
hash over all length-`L` windows and detect a repeat via a hash set (verify on
collision). If a duplicate of length `L` exists, try longer; else shorter.

- **Time:** O(n log n) expected (log n lengths × O(n) hashing). **Space:** O(n).
- Simpler to code than a suffix array and passes the constraints, but is
  randomized (hash-collision risk) — the suffix-array solution is deterministic.

## Key Insights & Edge Cases

- **Same quantity as "longest repeated substring"**; LeetCode 1044 is its named
  incarnation. If you solved problem 3 in this folder, you already have this.
- **Return `""` when `max(LCP) == 0`** — no character repeats (e.g. `"abcd"`).
- **Overlaps count**: `"aaaaa"` → `"aaaa"` (positions 0 and 1 overlap).
- **Determinism**: prefer the suffix-array approach when you want to avoid the tiny
  false-positive probability of a single-hash Rabin-Karp; if hashing, use double
  hashing or verify candidates by direct comparison.
- **Ties**: any adjacent pair reaching the max LCP gives an acceptable answer, which
  matches the problem's "return any" clause.
- For `n = 3 * 10^4`, both O(n log n) suffix array and O(n log n) hashing are
  comfortably fast; the quadratic brute force is not.
