# Cyclical Quest — Solution

## Brute Force

For each query `x`, generate all `|x|` cyclic rotations, deduplicate them, and
count occurrences of each rotation in `s` (e.g. with KMP). Each rotation costs
`O(|s| + |x|)`, so a single query is `O(|x| * (|s| + |x|))`. With `|s|` and total
query length up to `10^6`, this is astronomically slow (up to `~10^12` and
beyond).

- **Time:** `O(sum over queries of |x| * (|s| + |x|))`.
- **Space:** `O(|x|)` per query.

## Optimal Approach (Suffix Automaton)

### Setup

Build the SAM of `s` and compute `endpos` sizes (`cnt[v]`, exactly as in
Problem 3): seed `cur` states with `1`, clones with `0`, then propagate up the
suffix-link tree in decreasing `len` order. Now `cnt[v]` is the number of
occurrences in `s` of every substring represented by state `v`.

### Sliding a rotation window

All cyclic rotations of `x` are exactly the length-`|x|` substrings of the doubled
string `x + x` (taking start offsets `0 .. |x|-1`). So process `w = x + x` through
the automaton while maintaining a current state `v` and current matched length
`l`, using the *same* extend-or-follow-suffix-links logic as the longest-common-
substring scan:

For each character `c` of `w`:

1. If `next[v]` has an edge on `c`: `v = next[v][c]`, `l += 1`.
2. Else climb suffix links: while `v != -1` and `c not in next[v]`, `v = link[v]`.
   - If `v == -1`: `v = root`, `l = 0`.
   - Else: `l = len[v] + 1`, `v = next[v][c]`.
3. **Trim** the window to length `|x|`: if `l > |x|`, we must drop leading
   characters. If `l - 1 >= len[link[v]] + 1` after decrement... concretely:
   while `l > |x|`: decrement `l`; if `l` drops to `len[link[v]]` we must move to
   the suffix-link parent, i.e. `if len[link[v]] >= l: ... ` The standard trim is:
   `if l > |x|: l -= 1; if l == len[link[v]]: v = link[v]` — but the robust form
   loops. See the reference below.
4. Once we have processed at least `|x|` characters (index `>= |x| - 1`) and
   `l >= |x|` we are looking at a rotation. Because trimming keeps `l == |x|`
   here, we are at the state representing the current length-`|x|` rotation. If
   this state has not been visited for this query, add `cnt[v]` and mark it.

### Deduplicating rotations

Different start offsets may map to the **same SAM state** (that happens exactly
when the rotations are equal strings, e.g. periodic `x`). Keep a `visited`
timestamp per state (or a set) and only add `cnt[v]` the first time a state is
counted within the current query. This guarantees each *distinct* rotation
contributes once.

### Reference implementation

```python
def cyclical_quest(s, queries):
    sam = SuffixAutomaton()            # SAM with cnt[] endpos sizes (Problem 3)
    for ch in s:
        sam.extend(ch)                 # seed cnt=1 for cur, 0 for clone
    # propagate cnt up suffix-link tree (longest first)
    order = sorted(range(1, len(sam.length)),
                   key=lambda v: sam.length[v], reverse=True)
    for u in order:
        if sam.link[u] > 0:
            sam.cnt[sam.link[u]] += sam.cnt[u]

    res = []
    stamp = [0] * len(sam.length)
    tick = 0
    for x in queries:
        tick += 1
        m = len(x)
        v, l, ans = 0, 0, 0
        for i, c in enumerate(x + x):
            if c in sam.next[v]:
                v = sam.next[v][c]
                l += 1
            else:
                while v != -1 and c not in sam.next[v]:
                    v = sam.link[v]
                if v == -1:
                    v, l = 0, 0
                else:
                    l = sam.length[v] + 1
                    v = sam.next[v][c]
            # trim window down to length m
            if l > m:
                # move up until the state's longest is < m via suffix links
                while sam.length[sam.link[v]] >= m:
                    v = sam.link[v]
                l = m
            # count a full-length rotation once per state
            if i >= m - 1 and l == m and stamp[v] != tick:
                stamp[v] = tick
                ans += sam.cnt[v]
        res.append(ans)
    return res
```

### Complexity

- **Build SAM + cnt:** `O(|s|)` (or `O(|s| log |Sigma|)` with a dict `next`).
- **Per query:** `O(|x|)` amortized — scanning `x + x` is `2|x|` steps, each with
  amortized-`O(1)` suffix-link work.
- **Total:** `O(|s| + total query length)`.
- **Space:** `O(|s| * |Sigma|)`.

## Key Insights & Edge Cases

- Rotations of `x` == length-`|x|` substrings of `x + x`; that is the whole trick.
- The trim step is what keeps the window at exactly length `|x|`. When `l > m`,
  the current match got too long; you shrink it and, if it drops to the state's
  suffix-link boundary, hop to the parent state that represents shorter suffixes.
- Deduplicate by state with a per-query timestamp so periodic queries (e.g.
  `x = "aa"`, whose rotations are all `"aa"`) are counted once, not `|x|` times.
- A rotation that does not appear in `s` contributes `0` naturally — either the
  scan cannot reach a length-`m` match at that offset, or its state is simply
  never reached with `l == m`.
- Only start counting once at least `m` characters have been consumed
  (`i >= m - 1`); earlier positions cannot represent a full rotation.
- With `|s|` up to `10^6`, prefer an array-based `next` (size 26) over a dict for
  speed and to keep the constant factor low.
