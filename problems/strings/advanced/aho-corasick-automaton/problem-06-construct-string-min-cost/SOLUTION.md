# Solution — Construct String with Minimum Cost

## Brute Force

This is a shortest-path / word-break DP. Let `dp[i]` be the minimum cost to build
`target[0..i-1]`. `dp[0] = 0`. For each end position `i`, try every word `w`:
if `target[i-len(w):i] == w`, relax `dp[i] = min(dp[i], dp[i-len(w)] + cost(w))`.

```python
def minimumCost(self, target, words, costs):
    n = len(target)
    INF = float("inf")
    dp = [INF] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for w, c in zip(words, costs):
            L = len(w)
            if L <= i and dp[i - L] != INF and target[i - L:i] == w:
                dp[i] = min(dp[i], dp[i - L] + c)
    return dp[n] if dp[n] != INF else -1
```

- **Time:** `O(n · W · Lmax)` — for each of `n` positions, compare against each of
  `W` words at cost up to `Lmax`. With `n, W` up to `5·10^4` this is astronomically
  slow (`~10^13`), and even hashing all words per position is `O(n · Lmax^2)` or
  worse when many words share lengths.
- **Space:** `O(n)` for the DP array (plus the word storage).

The bottleneck is "which words end at position `i`?" — answered word-by-word.
Aho–Corasick answers it for *all* words at once in `O(1)` amortized per matched
word.

## Optimal Approach (Aho–Corasick Automaton + DP)

Build the automaton over `words`, storing at each terminal node the **minimum
cost** among words that end there (two different words could be identical or
share a terminal; keep the cheapest). Then scan `target` once, driving the DP
with the words that end at each position.

**Why it is correct.** As we feed `target` into the automaton and reach node
`cur` after consuming `target[0..i-1]`, every word that is a **suffix of the
consumed prefix** — i.e. every word ending exactly at position `i` — corresponds
to a terminal node on `cur`'s dictionary-suffix-link chain, and its length is the
depth of that terminal node. For each such word of length `L` and cost `c`, a
valid final append is `target[i-L:i] = word`, so `dp[i]` can be reached from
`dp[i-L]` at extra cost `c`. Relaxing over all words ending at `i` for all `i`
enumerates exactly the transitions of the brute-force DP, hence yields the same
optimum, but the enumeration is done via automaton links instead of scanning
every word.

**Speeding up the dict-link walk.** Walking the full dictionary-link chain per
position is `O(z)` and can be `Θ(n · Lmax)`. Two standard accelerations:

1. **Precompute per node the cheapest word cost keyed by its depth**, or
2. Simply walk the dict-link chain but note each terminal node stores `(depth,
   min_cost)`; the number of *distinct depths* of terminal nodes reachable is
   bounded by the number of distinct word lengths, which is at most `~sqrt(2·ΣL)`
   because distinct lengths summing to `ΣL <= 5·10^4` cannot exceed `O(sqrt(ΣL))`.

Approach (2) gives an amortized bound of `O(n · sqrt(ΣL))`, which is fast enough,
and is the standard accepted solution.

**Step by step.**

1. Insert each `words[j]` into the trie; at its terminal node record
   `min_cost = min(existing, costs[j])` and the node's depth (`= len(word)`).
2. BFS for failure links, goto transitions, and a `dict_link` per node pointing
   to the nearest ancestor-suffix terminal node (skip non-terminals).
3. `dp = [INF]*(n+1); dp[0] = 0`. Walk `target`: advance `cur`; then follow the
   `dict_link` chain from `cur`, and for each terminal node with depth `L` and
   cost `c`, relax `dp[i] = min(dp[i], dp[i-L] + c)` (using 1-based end index
   `i = position+1`).
4. Return `dp[n]` or `-1` if it is `INF`.

```python
from collections import deque

class Solution:
    def minimumCost(self, target, words, costs):
        INF = float("inf")
        nxt = [{}]; fail = [0]
        depth = [0]                 # trie depth of node = length of prefix
        node_cost = [INF]           # min cost of a word ending exactly here
        for w, c in zip(words, costs):
            cur = 0
            for ch in w:
                if ch not in nxt[cur]:
                    nxt.append({}); fail.append(0)
                    depth.append(depth[cur] + 1); node_cost.append(INF)
                    nxt[cur][ch] = len(nxt) - 1
                cur = nxt[cur][ch]
            node_cost[cur] = min(node_cost[cur], c)

        dict_link = [0] * len(nxt)
        q = deque()
        for ch, v in nxt[0].items():
            fail[v] = 0; q.append(v)
        while q:
            u = q.popleft()
            f = fail[u]
            dict_link[u] = f if node_cost[f] != INF else dict_link[f]
            for ch, v in nxt[u].items():
                g = fail[u]
                while g and ch not in nxt[g]:
                    g = fail[g]
                fail[v] = nxt[g].get(ch, 0) if (g or ch in nxt[0]) else 0
                if fail[v] == v:
                    fail[v] = 0
                q.append(v)

        n = len(target)
        dp = [INF] * (n + 1)
        dp[0] = 0
        cur = 0
        for i, ch in enumerate(target, 1):          # i = 1-based end position
            while cur and ch not in nxt[cur]:
                cur = fail[cur]
            cur = nxt[cur].get(ch, 0)
            # enumerate words ending at position i via dict-link chain
            node = cur if node_cost[cur] != INF else dict_link[cur]
            while node:
                L = depth[node]
                if dp[i - L] != INF:
                    dp[i] = min(dp[i], dp[i - L] + node_cost[node])
                node = dict_link[node]
        return dp[n] if dp[n] != INF else -1
```

- **Build:** `O(S · σ)` time / space, `S = Σ|words[i]| <= 5·10^4`.
- **DP scan:** `O(n · D)` where `D` is the number of distinct word lengths
  (`D = O(sqrt(S))`), so effectively `O(n · sqrt(S))`.
- **Overall:** comfortably within limits; `O(1)` per character for the automaton
  transitions plus the bounded dict-link walk.

## Key Insights & Edge Cases

- **Store the minimum cost per terminal node.** Multiple words (or duplicate
  words with different costs) may end at the same node; keep the cheapest so the
  DP relaxation is correct.
- **DP indexing.** Use `dp[i]` = min cost for the length-`i` prefix, and a word of
  length `L` ending at position `i` transitions from `dp[i-L]`. Guard against
  reading `dp[i-L]` when it is still `INF` (that prefix is unbuildable).
- **Impossible target** (Example 2) leaves `dp[n] == INF` → return `-1`.
- **Dictionary-link chain, not just the current node.** Shorter words ending at
  the same position (e.g. `"abc"` and `"c"` both ending at index 5) must all be
  considered; that is exactly what the `dict_link` walk enumerates.
- **Complexity guard.** Naively re-checking every word per position is TLE; the
  automaton reduces "which words end here" to a bounded link walk, which is the
  whole point of filing this under Aho–Corasick.
- **Root failure self-loop guard** (`fail[v] == v → 0`) as in every build.
