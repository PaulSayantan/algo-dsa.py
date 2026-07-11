# Solution — Longest Repeated Substring

## Brute Force

Enumerate every pair of starting positions `(i, j)` and extend a match as far as
possible, tracking the longest. There are `O(n^2)` pairs and each extension is
`O(n)`, giving **O(n^3)** time.

A better brute force is **binary search on the answer length `L`** combined with
hashing: for a candidate `L`, insert every length-`L` substring's rolling hash
into a set and check for a collision. Each check is `O(n)` and there are
`O(log n)` lengths, giving **O(n log n)** expected time — but it relies on hash
collisions not occurring and only tells you *a* length, still needing care to
recover the substring. Time **O(n log n)** expected, space **O(n)**.

## Optimal Approach (Suffix Array + LCP / Kasai)

Two occurrences of the same substring `t` are exactly two different suffixes
that both start with `t`. So the longest repeated substring equals the longest
common prefix shared by *some* pair of suffixes.

Crucially, in the **sorted** order of suffixes, the pair sharing the longest
common prefix is always **adjacent** in the suffix array. (If suffixes `a < c`
share a prefix of length `h`, then every suffix `b` with `a <= b <= c` also
shares that prefix, so an adjacent pair achieves the maximum.) Therefore:

```
answer length = max(LCP)
```

### Steps

1. Build the suffix array `SA` of `s` (prefix-doubling, `O(n log n)`).
2. Build the `LCP` array with **Kasai's algorithm** in `O(n)`.
3. Let `i* = argmax(LCP)`. If `LCP[i*] == 0`, no substring repeats; return `""`.
4. Otherwise the answer is `s[SA[i*] : SA[i*] + LCP[i*]]`.

### Kasai's algorithm (why it is O(n))

Maintain `rank[]`, the inverse of `SA`. Walk the suffixes in **original string
order** `i = 0, 1, ..., n-1`, keeping a running match length `h`. For suffix `i`,
its sorted predecessor starts at `j = SA[rank[i]-1]`; extend `h` while
`s[i+h] == s[j+h]`. The invariant is that if suffix `i` matched `h` characters,
then suffix `i+1` matches at least `h-1` (drop the first character of both
strings and they are still suffixes whose predecessors share a prefix). So after
recording `LCP[rank[i]] = h` we do `h = max(h-1, 0)`. Each step decreases `h` by
at most 1 and increases it via the while-loop, so total work is `O(n)`.

```python
def build_lcp_kasai(s, sa):
    n = len(s)
    rank = [0] * n
    for i, p in enumerate(sa):
        rank[p] = i
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
        else:
            h = 0
    return lcp

def longest_repeated_substring(s):
    if not s:
        return ""
    sa = build_suffix_array(s)
    lcp = build_lcp_kasai(s, sa)
    best_i = max(range(len(s)), key=lambda i: lcp[i])
    if lcp[best_i] == 0:
        return ""
    start = sa[best_i]
    return s[start:start + lcp[best_i]]
```

### Complexity

- Suffix array (doubling): **O(n log n)** time, **O(n)** space.
- Kasai LCP: **O(n)** time, **O(n)** space.
- Overall: **O(n log n)** time, **O(n)** space (dominated by SA build).

## Key Insights & Edge Cases

- **Adjacency lemma:** the maximum common prefix over all suffix pairs is
  realized by an adjacent pair in sorted order — this is why scanning `LCP` once
  suffices.
- **No repeat:** if `max(LCP) == 0`, every character position begins a distinct
  set of characters with no shared prefix of length >= 1; return `""`.
- **Overlaps are allowed** here (e.g. `"aaaa"` -> `"aaa"`). If the problem
  required *non-overlapping* repeats, you would additionally require the two
  suffix start positions to differ by at least the match length, which needs
  more work (binary search on length + checking index spread within LCP
  intervals).
- **Ties:** any max-length repeat is a valid answer; returning the one attached
  to the argmax index is fine.
- Single character or empty string: `LCP` is all zeros, answer is `""`.
