# Solution — Longest Substring With At Least K Occurrences

## Brute Force

For each candidate length `L` from `n` down to `1`, hash every length-`L`
substring and count occurrences with a dictionary; stop at the first `L` where
some substring hits count `>= k`. Each length costs `O(n)`, and there are `O(n)`
lengths, giving **O(n^2)** time (with hashing) plus collision risk. Enumerating
substrings explicitly and comparing is even worse at `O(n^3)`. Too slow for
`n = 10^5`.

You can binary-search on `L` to get `O(n log n)` with rolling hashes, but it is
hash-dependent and awkward to recover the actual substring. The suffix-array
method is deterministic and reconstructs the substring directly.

## Optimal Approach (Suffix Array + LCP / Kasai)

**Grouping insight:** a substring `t` that occurs `>= k` times is a common prefix
of `>= k` suffixes. In the suffix array these suffixes form a **contiguous block**
of `>= k` consecutive entries (all suffixes sharing prefix `t` sort together).
For a window of `k` consecutive suffixes `SA[i], SA[i+1], ..., SA[i+k-1]`, the
length of their common prefix is

```
min( LCP[i+1], LCP[i+2], ..., LCP[i+k-1] )   -- the min over the k-1 internal gaps
```

So the answer length is the **maximum, over all windows of size `k`, of the
minimum LCP inside the window**:

```
answer_len = max over valid windows of  min(LCP[j] for the k-1 gaps in window)
```

This is a classic **sliding-window-minimum** computed with a monotonic deque in
`O(n)`. Concretely, slide a window of width `w = k - 1` across `LCP[1..n-1]`; for
each full window take its minimum and keep the largest minimum together with the
window's location, so we can reconstruct the substring.

### Steps

1. If `k <= 1`, return `s` (the whole string occurs once).
2. If `k > n`, return `""` (no substring can occur `k` times).
3. Build `SA` (`O(n log n)`) and `LCP` via Kasai (`O(n)`).
4. Sliding-window minimum of width `w = k - 1` over `LCP[1..n-1]`; track the
   maximum window-min `best` and a window index that achieves it.
5. If `best == 0`, the only `k`-times substring would be empty; return `""`
   (occurs when even single characters don't repeat `k` times). Otherwise take
   any suffix start `SA[j]` inside the winning window and return
   `s[SA[j] : SA[j] + best]`.

```python
from collections import deque

def longest_substring_at_least_k(s, k):
    n = len(s)
    if k <= 1:
        return s
    if k > n:
        return ""
    sa = build_suffix_array(s)
    lcp = build_lcp_kasai(s, sa)
    w = k - 1                       # number of internal gaps in a size-k window

    best_len, best_win_end = 0, -1
    dq = deque()                    # indices into lcp, increasing lcp values
    for i in range(1, n):
        while dq and lcp[dq[-1]] >= lcp[i]:
            dq.pop()
        dq.append(i)
        while dq[0] <= i - w:       # keep only the current window [i-w+1, i]
            dq.popleft()
        if i - w + 1 >= 1:          # first full window
            m = lcp[dq[0]]
            if m > best_len:
                best_len, best_win_end = m, i

    if best_len == 0:
        return ""
    start = sa[best_win_end]        # any suffix in the winning window works
    return s[start:start + best_len]
```

### Worked check on "banana", k = 2

`SA = [5, 3, 1, 0, 4, 2]` (suffixes `a, ana, anana, banana, na, nana`),
`LCP = [0, 1, 3, 0, 0, 2]`, `w = 1` (windows are single gaps).
The maximum single LCP gap is `3` at `i = 2`, between `ana` and `anana`, so the
answer is `s[SA[2] : SA[2] + 3] = s[1:4] = "ana"`. Matches.

For `k = 3`, `w = 2`: window minimums of adjacent pairs of `LCP[1..5]` are
`min(1,3)=1, min(3,0)=0, min(0,0)=0, min(0,2)=0` -> best `1`, giving a length-1
answer `"a"` (which indeed occurs 3 times). Matches.

### Complexity

- Suffix array: **O(n log n)** time, **O(n)** space.
- Kasai LCP + monotonic-deque sliding-window minimum: **O(n)** time, **O(n)**
  space.
- Overall: **O(n log n)** time, **O(n)** space.

## Key Insights & Edge Cases

- **Window of `k` suffixes = `k-1` internal LCP gaps.** Off-by-one here is the
  most common bug: use width `w = k - 1` over the LCP array, not `k`.
- **`k <= 1`:** the whole string qualifies; return `s` directly (the LCP scan
  would otherwise miss the full-length single occurrence).
- **`k > n`:** impossible; return `""`.
- **Overlaps allowed:** counting `k` suffixes with a shared prefix inherently
  permits overlapping occurrences (as in `"aaaaa"` with `k = 3` giving `"aaa"`).
  For a **non-overlapping** variant you would additionally binary-search the
  length and verify that within each LCP interval you can pick `k` start
  positions pairwise at least `L` apart.
- **Reconstruction:** any suffix index inside the winning window starts with the
  answer, so `s[SA[j] : SA[j] + best_len]` for any `j` in the window is correct.
- **`best_len == 0`:** means no character repeats `k` times; return `""`.
