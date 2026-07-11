# Total Length of All Distinct Substrings — Solution

## Brute Force

Insert every substring into a hash set, then sum `len(w)` over the set. There are
`O(n^2)` substrings, each up to length `n`, so building the set is `O(n^3)` time
(or `O(n^2)` with rolling hashes) and `O(n^2)` space. Acceptable only for small
`n`.

A suffix array + LCP approach also works: for each starting suffix the distinct
substrings contributed are those longer than the LCP with the previous suffix,
and the sum of their lengths is an arithmetic series. That is `O(n log n)`, but
the SAM version is a clean single linear pass.

- **Time:** `O(n^3)` naive / `O(n^2)` with hashing.
- **Space:** `O(n^2)`.

## Optimal Approach (Suffix Automaton)

### Why it works

As in Problem 1, each state `v` (other than the initial state) owns exactly the
distinct substrings whose lengths fall in the half-open interval
`(len[link[v]], len[v]]`. So instead of merely counting them
(`len[v] - len[link[v]]`), we sum the integers in that interval:

```
sum of lengths for state v = a + (a+1) + ... + b
                           = (a + b) * (b - a + 1) / 2
```

where `a = len[link[v]] + 1` (shortest substring in the class) and
`b = len[v]` (longest). Because the intervals partition all distinct substrings
with no overlap, summing this per state yields the total length exactly once per
distinct substring.

### Steps

1. Build the SAM of `s`.
2. For every state `v != initial`, let `a = len[link[v]] + 1`, `b = len[v]`.
3. Add `(a + b) * (b - a + 1) // 2` to the running total.

### Reference implementation

```python
def total_length_distinct_substrings(s: str) -> int:
    sam = SuffixAutomaton()          # same class as in Problem 1
    for ch in s:
        sam.extend(ch)
    total = 0
    for v in range(1, len(sam.length)):
        b = sam.length[v]
        a = sam.length[sam.link[v]] + 1
        total += (a + b) * (b - a + 1) // 2
    return total
```

### Complexity

- **Build:** `O(n)` (or `O(n log |Sigma|)` with a dict `next`).
- **Summation pass:** `O(number of states) = O(n)`.
- **Space:** `O(n * |Sigma|)`.

## Key Insights & Edge Cases

- The interval endpoints satisfy `a <= b` for every non-initial state, so the
  arithmetic-series count `b - a + 1` is always `>= 1`.
- `count of substrings in state v = b - a + 1 = len[v] - len[link[v]]`; this is
  exactly the quantity Problem 1 sums, confirming the two problems share the same
  state decomposition.
- Use integer arithmetic; `(a + b) * (b - a + 1)` is always even, so `// 2` is
  exact.
- Single character `"a"` -> total `1`. All-equal `"aaaa"` -> `1+2+3+4 = 10`.
- The magnitude grows like `n^3/6`; for `n = 10^5` this is about `1.7e14`, which
  overflows 32-bit but fits comfortably in 64-bit (and Python handles it
  natively).
