# Longest Common Substring of Two Strings — Solution

## Brute Force

Classic dynamic programming: let `dp[i][j]` be the length of the longest common
suffix of `s[:i]` and `t[:j]`. Then `dp[i][j] = dp[i-1][j-1] + 1` when
`s[i-1] == t[j-1]`, else `0`, and the answer is the maximum entry. This is
`O(len(s) * len(t))` time and `O(len(t))` space with a rolling row. For inputs up
to `2.5 * 10^5` each, the product is `~6 * 10^10` operations — far too slow.

- **Time:** `O(len(s) * len(t))`.
- **Space:** `O(min(len(s), len(t)))` with a rolling array.

## Optimal Approach (Suffix Automaton)

### Idea

Build the SAM of `s`; it recognizes every substring of `s`. Now stream `t`
through the automaton while tracking two quantities:

- `v`: the current state (the state for the longest suffix of the processed
  prefix of `t` that is also a substring of `s`).
- `l`: the length of that current matched suffix.

For each character `c` of `t`:

1. **If** `next[v]` has an edge on `c`, extend the match: `v = next[v][c]`,
   `l += 1`.
2. **Else** follow suffix links until a state with a `c`-transition is found (or
   the root fails):
   - While `v != -1` and `c not in next[v]`: `v = link[v]`.
   - If `v == -1` (no state can consume `c`): reset `v = root`, `l = 0`.
   - Otherwise set `l = len[v] + 1` and `v = next[v][c]`. Using `len[v] + 1` is
     crucial: after climbing suffix links, the longest usable match is bounded by
     the length of the state we landed on, not the old `l`.
3. Update `answer = max(answer, l)`.

The maximum `l` observed over all of `t` is the longest common substring length.

### Why it works

At every step, `l` is the length of the longest suffix of the current prefix of
`t` that is a substring of `s`, and `v` is exactly the SAM state representing that
suffix. Following suffix links mimics dropping leading characters of the current
match until the automaton can again consume the next character — analogous to the
failure function in KMP. The state's `len` gives the correct upper bound on the
match length after each link jump.

### Reference implementation

```python
def longest_common_substring(s: str, t: str) -> int:
    sam = SuffixAutomaton()          # same class as Problem 1
    for ch in s:
        sam.extend(ch)

    v, l, best = 0, 0, 0
    for c in t:
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
        best = max(best, l)
    return best
```

### Complexity

- **Build SAM of `s`:** `O(len(s))` (or `O(len(s) log |Sigma|)` with a dict).
- **Scan `t`:** `O(len(t))` amortized — each character increases `l` by at most 1
  and suffix-link jumps only decrease `l`, so total jumps are bounded by total
  increments.
- **Total:** `O(len(s) + len(t))`.
- **Space:** `O(len(s) * |Sigma|)`.

## Key Insights & Edge Cases

- Build the SAM of the *shorter* string to minimize memory when lengths differ
  greatly; the answer is symmetric.
- After a suffix-link climb, set `l = len[landed_state] + 1` — a common bug is to
  keep the stale `l`, which overcounts.
- No common substring (`"abc"` vs `"xyz"`) yields `0`; every transition fails and
  `l` never rises above 0.
- Identical strings give `len(s)` (the whole string matches).
- This generalizes to the **longest common substring of many strings** by
  building a SAM of one and, for each other string, recording the best match
  length reachable at each state, then taking the per-state minimum across all
  strings and the maximum over states (with a suffix-link propagation step).
