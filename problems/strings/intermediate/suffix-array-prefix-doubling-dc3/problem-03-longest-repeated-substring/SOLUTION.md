# Solution — Longest Repeated Substring

## Brute Force

Check every pair of start positions and extend the common prefix, or binary-search
the answer length `L` and hash all length-`L` substrings looking for a duplicate.

- Naive pair extension: O(n^3) (O(n^2) pairs × O(n) extension).
- Binary search on length + hashing: O(n log n) expected but relies on hashing and
  can have collisions; still a common practical approach.
- **Time:** O(n^3) naive / O(n log n) with hashing. **Space:** O(n).

## Optimal Approach — Suffix Array + LCP (Kasai)

**Idea.** Any substring occurring twice is a common prefix of two distinct
suffixes. Among all pairs of suffixes, the pair sharing the **longest** common
prefix must be **adjacent** in sorted order: if two suffixes share a prefix of
length `L`, then every suffix between them in sorted order also shares that prefix,
so some adjacent pair achieves at least `L`. Therefore:

```
answer length = max(LCP[i])  over adjacent sorted suffixes
```

and the substring itself is the first `LCP[i]` characters of suffix `SA[i]`.

**LCP array via Kasai's algorithm (O(n)).** `LCP[i]` is the length of the longest
common prefix of `S[SA[i-1]:]` and `S[SA[i]:]` (with `LCP[0] = 0`). Kasai walks the
suffixes in *text* order using the inverse permutation `rank` (`rank[SA[i]] = i`).
The key invariant: if the LCP of suffix `i` with its predecessor is `h`, then the
LCP of suffix `i+1` with *its* predecessor is at least `h-1`, so the running
counter `h` only decreases by at most 1 per step → total work O(n).

**Steps.**
1. `SA = build_suffix_array(S)`.
2. `LCP = kasai(S, SA)`.
3. Find `i = argmax(LCP)`. If `max(LCP) == 0`, return `""`.
4. Return `S[SA[i] : SA[i] + LCP[i]]`.

```python
def kasai(s, sa):
    n = len(s)
    rank = [0] * n
    for i, p in enumerate(sa):
        rank[p] = i
    lcp = [0] * n          # lcp[i] = LCP(sa[i-1], sa[i]); lcp[0] = 0
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h:
                h -= 1
        else:
            h = 0
    return lcp

def longest_repeated_substring(s):
    if not s:
        return ""
    sa = build_suffix_array(s)
    lcp = kasai(s, sa)
    best_len, best_i = 0, 0
    for i in range(1, len(s)):
        if lcp[i] > best_len:
            best_len, best_i = lcp[i], i
    return s[sa[best_i]: sa[best_i] + best_len]
```

- Build SA: O(n log n). Kasai LCP: O(n). Scan for max: O(n).
- **Time:** O(n log n). **Space:** O(n).

## Key Insights & Edge Cases

- **Max LCP = answer length.** This is the single most reused fact about LCP arrays.
- **Adjacent pairs suffice** — you do NOT need to compare all O(n^2) suffix pairs.
- **No repeat** (all distinct chars) ⇒ every `LCP[i] = 0` ⇒ return `""`.
- **Overlap allowed**: `"aaaa"` → `"aaa"` (occurs at 0 and 1, overlapping). If the
  problem required *non-overlapping* repeats, you would additionally require the two
  start positions to differ by at least the length — a harder variant.
- **Ties**: any adjacent pair achieving the maximum LCP yields a valid answer.
- The LCP array is the workhorse for the next problems (distinct substrings, LCS),
  so implement Kasai once and reuse it.
