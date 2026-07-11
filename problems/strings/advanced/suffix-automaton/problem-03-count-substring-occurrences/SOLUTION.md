# Count Substring Occurrences — Solution

## Brute Force

For each query `p`, scan `s` with a naive or KMP search and count matches. Naive
matching is `O(len(s) * len(p))` per query; KMP is `O(len(s) + len(p))` per
query. With `Q` queries and `|s| = n` that is `O(Q * (n + |p|))`, which is
`O(Q * n)` in the worst case — too slow when both `Q` and `n` are `10^5`.

- **Time:** `O(Q * n)` (KMP) up to `O(Q * n * maxlen)` (naive).
- **Space:** `O(n)`.

## Optimal Approach (Suffix Automaton)

### The `endpos` insight

For any substring `w` of `s`, define `endpos(w)` as the set of end positions
where `w` occurs. The number of occurrences of `w` (counting overlaps) is exactly
`|endpos(w)|`. In a SAM, all substrings represented by the same state share the
same `endpos` set, so a single integer per state answers occurrence counts for
every substring in that class.

### Computing `endpos` sizes

1. Build the SAM of `s`. While building, mark the state created for each new
   prefix (the `cur` state in `extend`) with `cnt = 1`. **Clone states** created
   during a split get `cnt = 0` — they represent substrings that do not
   themselves end a prefix, and their counts come entirely from descendants.
2. The suffix links form a tree. A substring's `endpos` set is the union of the
   `endpos` sets of its children in that tree, and those child sets are disjoint
   for the "prefix-ending" seeds. So propagate counts from longer states to
   shorter ones: sort states by `len` descending (a counting sort works since
   lengths are bounded by `n`), and add each state's `cnt` to its suffix-link
   parent's `cnt`.

After this, `cnt[v]` equals `|endpos|` for every substring represented by state
`v`, i.e., the number of occurrences of any of those substrings.

### Answering a query

Walk `p` character by character from the initial state following `next`
transitions. If any transition is missing, `p` is not a substring -> answer `0`.
Otherwise you land in some state `v`, and the answer is `cnt[v]`.

### Reference implementation

```python
def count_occurrences(s, queries):
    sam = SuffixAutomaton()          # same class as Problem 1, plus a `cnt` list
    cnt = [0]
    def extend(c):
        # identical to Problem 1's extend, but:
        #   - append cnt.append(1) for the new `cur` state
        #   - append cnt.append(0) for any `clone` state
        ...
    for ch in s:
        extend(ch)

    # propagate counts up the suffix-link tree, longest state first
    order = sorted(range(1, len(sam.length)),
                   key=lambda v: sam.length[v], reverse=True)
    for v in order:
        p = sam.link[v]
        if p > 0:
            cnt[p] += cnt[v]

    res = []
    for p in queries:
        cur = 0
        ok = True
        for ch in p:
            if ch in sam.next[cur]:
                cur = sam.next[cur][ch]
            else:
                ok = False
                break
        res.append(cnt[cur] if ok else 0)
    return res
```

### Complexity

- **Build + count propagation:** `O(n)` (counting sort by `len` keeps it linear).
- **Each query:** `O(|p|)`.
- **Total:** `O(n + sum(|p|))`.
- **Space:** `O(n * |Sigma|)`.

## Key Insights & Edge Cases

- Clone states MUST be seeded with `cnt = 0`; seeding them with `1` double-counts
  occurrences. Only the `cur` states from each `extend` step get `cnt = 1`.
- Propagation order matters: process states in decreasing `len` so a child is
  always added into its parent before the parent is itself consumed.
- The initial state (index 0) is the empty string; do not add into it and never
  return its count as an answer.
- A query longer than `s`, or containing a character not in `s`, simply fails a
  transition and returns `0`.
- Overlaps are counted naturally because `endpos` records every end position
  independently.
