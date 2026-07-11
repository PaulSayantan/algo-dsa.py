# K-th Lexicographically Smallest Distinct Substring — Solution

## Brute Force

Generate all distinct substrings, sort them, and index position `k`. There are
`O(n^2)` substrings, each up to length `n`; storing and sorting them costs
`O(n^2)` space and `O(n^2 log n * n)` time in the worst case (comparisons touch
strings of length `O(n)`). Only viable for tiny `n`.

- **Time:** `O(n^3 log n)` in the worst case.
- **Space:** `O(n^2)`.

## Optimal Approach (Suffix Automaton)

### Structure

The SAM is a DAG where every path from the initial state spells a distinct
substring. Sorting substrings lexicographically corresponds to a DFS that visits
outgoing edges in increasing character order. To jump directly to the `k`-th, we
precompute for each state `v`:

```
paths[v] = number of distinct non-empty substrings reachable by leaving v
         = sum over edges (v -> u) of (1 + paths[u])
```

The `1` counts the substring that ends exactly at `u` via that edge; `paths[u]`
counts everything that extends it. `paths[v]` is computed by a reverse
topological order (or memoized DFS) over the DAG. Note this counts substrings,
which are automatically distinct because each DAG path is a distinct string.

### Greedy descent

Start at the initial state with the answer string empty. Repeat:

1. For each character `c` from `'a'` to `'z'` that has an edge `v -> u`:
   - Let `cnt = 1 + paths[u]` (the substring reaching `u` plus its extensions).
   - If `k <= cnt`: append `c` to the answer, consume this edge:
     `k -= 1` (we "used up" the substring that ends here); if `k == 0` stop and
     return the answer; otherwise move `v = u` and continue descending.
   - Else: `k -= cnt` and try the next character.
2. If no character satisfies the condition, `k` exceeded the total -> return `""`.

The key accounting: taking edge `c` first accounts for the string ending right at
`u` (that is the smallest string with this prefix), which is why we decrement `k`
by 1 and check for zero before recursing deeper.

### Reference implementation

```python
def kth_distinct_substring(s: str, k: int) -> str:
    sam = SuffixAutomaton()          # same class as Problem 1
    for ch in s:
        sam.extend(ch)

    n = len(sam.length)
    paths = [0] * n            # distinct substrings reachable leaving each state
    order = sorted(range(n), key=lambda v: sam.length[v], reverse=True)
    for v in order:            # longer states first == reverse topo order
        total = 0
        for c in sorted(sam.next[v]):
            u = sam.next[v][c]
            total += 1 + paths[u]
        paths[v] = total

    # total distinct substrings = paths[0]; bail if k is out of range
    if k > paths[0]:
        return ""

    v = 0
    ans = []
    while True:
        for c in sorted(sam.next[v]):
            u = sam.next[v][c]
            cnt = 1 + paths[u]
            if k <= cnt:
                ans.append(c)
                k -= 1
                if k == 0:
                    return "".join(ans)
                v = u
                break
            else:
                k -= cnt
```

### Complexity

- **Build SAM:** `O(n)` (or `O(n log |Sigma|)` with a dict).
- **Compute `paths`:** `O(n * |Sigma|)` — each edge is visited once.
- **Descent:** `O(len(answer) * |Sigma|) = O(n * |Sigma|)`.
- **Space:** `O(n * |Sigma|)`.

## Key Insights & Edge Cases

- Ordering by `len` descending is a valid reverse topological order because every
  DAG edge goes from a shorter longest-substring to a longer one.
- `paths[0]` is the total number of distinct substrings; if `k > paths[0]`,
  return `""` immediately (Example 3).
- Iterate edges in sorted character order at *both* the precompute and the
  descent steps so the counts line up with lexicographic order.
- Beware of huge `k` (up to `10^18`): use 64-bit / Python big ints; the counts
  `paths[v]` can themselves reach `O(n^2)`.
- Do not confuse this with the k-th smallest substring *with multiplicity*
  (counting repeats). For that variant, weight each edge by the `endpos` size of
  the target state instead of using `1 + paths[u]`.
