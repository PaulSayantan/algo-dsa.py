# Solution — Count All Palindromic Substrings

## Brute Force

For every substring `s[i:j]`, test whether it is a palindrome and increment a
counter.

- `O(n^2)` substrings × `O(n)` palindrome test = `O(n^3)`.
- With an `is_pal[i][j]` DP table it becomes `O(n^2)` time and `O(n^2)` space.
- Expand-around-center is `O(n^2)` time, `O(1)` space and is the usual LeetCode
  647 answer.

The eertree gives an `O(n)`-node linear solution and, unlike expand-around-
center, also tells you **per-palindrome** occurrence counts for free.

## Optimal Approach — Palindromic Tree (Eertree)

### The counting trick

While building the eertree, every time `add(i)` finishes with `last = v`, the
palindrome represented by `v` occurs *as the longest palindromic suffix* of the
prefix `s[0..i]`. Increment `cnt[v]` by 1 at that moment.

But we want **all** occurrences, not just occurrences as the *longest* suffix.
The observation is: if a palindrome `P` occurs ending at position `i`, then every
palindromic **suffix** of the longest palindromic suffix at `i` also occurs
ending at `i`. Those shorter palindromic suffixes are exactly the ancestors of
`v` along the **suffix-link chain**. So an occurrence recorded at `v` must also
be credited to `suffix[v]`, `suffix[suffix[v]]`, and so on.

Rather than walking each chain (which could be `O(n)` per node), we **propagate
once**: process nodes in order of **decreasing length** and do
`cnt[suffix[v]] += cnt[v]`. Because a suffix link always points to a strictly
shorter palindrome, decreasing-length order guarantees `cnt[v]` is already final
before it flows into its (shorter) suffix-link target. Nodes are created in
non-decreasing length only loosely, so sort by length (or bucket by length in
`O(n)`); iterating over creation order in reverse also works since a child is
always created after its suffix-link target has a smaller length.

The total number of palindromic substring occurrences is then `sum(cnt[v])` over
all non-root nodes `v`.

### Reference implementation

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        length = [-1, 0]
        suffix = [0, 0]
        edges = [dict(), dict()]
        cnt = [0, 0]
        last = 1

        def get_link(v: int, i: int) -> int:
            while i - length[v] - 1 < 0 or s[i - length[v] - 1] != s[i]:
                v = suffix[v]
            return v

        for i, c in enumerate(s):
            cur = get_link(last, i)
            if c in edges[cur]:
                last = edges[cur][c]
            else:
                new = len(length)
                length.append(length[cur] + 2)
                edges.append(dict())
                cnt.append(0)
                if length[new] == 1:
                    suffix.append(1)
                else:
                    link = get_link(suffix[cur], i)
                    suffix.append(edges[link][c])
                edges[cur][c] = new
                last = new
            cnt[last] += 1                      # occurred as longest suffix here

        # propagate counts from longer palindromes to their suffix links
        for v in sorted(range(2, len(length)), key=lambda x: -length[x]):
            cnt[suffix[v]] += cnt[v]

        return sum(cnt[v] for v in range(2, len(length)))
```

- **Time:** `O(n · log |Σ|)` build + `O(n log n)` for the length sort (or `O(n)`
  with counting-sort by length / reverse creation order).
- **Space:** `O(n)`.

## Key Insights & Edge Cases

- **Two kinds of count.** `cnt[v]` before propagation = occurrences of `P_v` as
  the *longest* palindromic suffix; after propagation = *total* occurrences of
  `P_v`. Summing the latter counts every palindromic substring occurrence once.
- **Propagation order matters.** You must add child counts into shorter
  (suffix-link) nodes. Processing in decreasing length (or reverse creation
  order) is required; the opposite order under-counts.
- **`"aaa"` walkthrough:** nodes `a` and `aa` and `aaa`. Longest-suffix counts
  are `a:1` (at i=0), `aa:1` (i=1), `aaa:1` (i=2) plus `a` again... after
  propagation `a` occurs 3 times, `aa` 2 times, `aaa` 1 time → `3+2+1 = 6`.
- **`"abc"`**: three length-1 nodes, no propagation adds anything → `3`.
- Do not double-count the roots; start sums at node index `2`.
- Watch integer size for very long strings: the total can be `O(n^2)` (up to
  ~`5·10^9` for `n = 10^5`), so use 64-bit integers in languages where `int`
  overflows (Python is fine).
