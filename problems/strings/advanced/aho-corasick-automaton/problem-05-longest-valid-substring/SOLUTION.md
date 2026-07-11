# Solution — Longest Valid Substring

## Brute Force

For every right endpoint `r`, extend a window leftward and, for each candidate
start `l`, check whether the window `word[l..r]` contains any forbidden string.
Because `forbidden[i]` has length at most 10, a common "brute-ish" trick is: at
each `r`, look back up to 10 characters and test whether any suffix ending at `r`
of length `1..10` is forbidden (store `forbidden` in a set).

```python
def longestValidSubstring(self, word, forbidden):
    fset = set(forbidden)
    n = len(word)
    left = 0
    ans = 0
    for r in range(n):
        # any forbidden string ending at r starts no earlier than r-9
        for l in range(r, max(r - 10, left - 1), -1):
            if word[l:r + 1] in fset:
                left = l + 1
                break
        ans = max(ans, r - left + 1)
    return ans
```

- **Time:** `O(n · Lmax)` where `Lmax <= 10`, i.e. `O(10n)`. This actually passes
  LeetCode because the forbidden length is capped at 10, but the substring
  slicing (`word[l:r+1]`) allocates and hashes up to 10-char strings each step.
- **Space:** `O(Σ|forbidden|)` for the set.

This set-of-suffixes method is fine here precisely because `Lmax` is tiny. When
patterns are long or unbounded, the per-step `O(Lmax)` factor and repeated
hashing become the bottleneck — that is where Aho–Corasick wins with a true
`O(n)` scan.

## Optimal Approach (Aho–Corasick Automaton)

Build the automaton over `forbidden`, then run a **sliding window** over `word`.
The invariant: `left` is the smallest index such that `word[left..r]` contains no
forbidden substring.

**Why it is correct.** Scan `word` with the automaton, maintaining node `cur`.
After consuming `word[r]`, the automaton's dictionary-suffix links tell us the
set of forbidden strings ending at index `r`. Let `mlen` be the length of the
**shortest** forbidden string ending at `r` (precompute per node the minimum
forbidden length reachable via dict-links). If such a forbidden string exists, it
occupies `[r - mlen + 1, r]`; to keep the window valid we must move `left` to at
least `r - mlen + 2` (just past that occurrence's start). Using the *shortest*
match ending at `r` is optimal: a longer forbidden match ending at `r` starts
even earlier, so excluding the shortest already excludes it, and moving `left`
any less would leave the shortest forbidden substring inside the window. After
updating `left`, the window `[left, r]` is guaranteed valid and we take
`ans = max(ans, r - left + 1)`.

Why "shortest" and not "longest": we want the *largest* valid window, i.e. the
*smallest* forced `left`. A forbidden match ending at `r` with length `mlen`
forces `left >= r - mlen + 2`. Among all forbidden matches ending at `r`, the one
with the smallest `mlen` gives the *largest* lower bound on `left` (because
`r - mlen + 2` grows as `mlen` shrinks), which is exactly the binding
constraint. So we must move `left` past the **shortest** forbidden occurrence
ending at `r`.

**Step by step.**

1. Build the trie over `forbidden`; store each terminal node's word length.
2. BFS for failure links, goto transitions, and per node
   `min_forb_len[node] = min(own length if terminal, min_forb_len[fail[node]])`
   (use `+inf` when none).
3. Scan `word` with `cur` and `left = 0`. At each `r`: advance `cur`; if
   `min_forb_len[cur]` is finite, set `left = max(left, r - min_forb_len[cur] + 2)`;
   update `ans = max(ans, r - left + 1)`.

```python
from collections import deque

class Solution:
    def longestValidSubstring(self, word, forbidden):
        INF = float("inf")
        nxt = [{}]; fail = [0]; wlen = [0]        # wlen: forbidden length ending here (0 = none)
        for w in forbidden:
            cur = 0
            for ch in w:
                if ch not in nxt[cur]:
                    nxt.append({}); fail.append(0); wlen.append(0)
                    nxt[cur][ch] = len(nxt) - 1
                cur = nxt[cur][ch]
            wlen[cur] = len(w)

        min_forb = [INF] * len(nxt)
        q = deque()
        for ch, v in nxt[0].items():
            fail[v] = 0; q.append(v)
        while q:
            u = q.popleft()
            base = wlen[u] if wlen[u] else INF
            min_forb[u] = min(base, min_forb[fail[u]])
            for ch, v in nxt[u].items():
                f = fail[u]
                while f and ch not in nxt[f]:
                    f = fail[f]
                fail[v] = nxt[f].get(ch, 0) if (f or ch in nxt[0]) else 0
                if fail[v] == v:
                    fail[v] = 0
                q.append(v)

        ans = 0
        cur = 0
        left = 0
        for r, ch in enumerate(word):
            while cur and ch not in nxt[cur]:
                cur = fail[cur]
            cur = nxt[cur].get(ch, 0)
            m = min_forb[cur]
            if m != INF:
                left = max(left, r - m + 2)
            ans = max(ans, r - left + 1)
        return ans
```

- **Build:** `O(S · σ)`, `S = Σ|forbidden[i]|`.
- **Scan:** `O(n)` amortized (`left` only increases; failure hops amortize to
  `O(1)` per char).
- **Overall:** `O(S · σ + n)` time, `O(S · σ)` space.

## Key Insights & Edge Cases

- **Track the shortest, not the longest, forbidden match ending at `r`.** This is
  the subtle correctness point: the shortest match imposes the tightest (largest)
  lower bound on `left`.
- **`left = max(left, …)`** — never move `left` backward; the window's left edge
  is monotonically non-decreasing, which is what keeps the scan linear.
- **Whole word forbidden** (Example 3, `"aaa"`/`["aaa"]`): at `r=2` the shortest
  (only) match has length 3, so `left = max(0, 2-3+2)=1`, giving window `[1,2]`
  length 2 — correct.
- **Empty valid substring** always allowed, so the answer never goes below 0
  (with `ans` initialized to 0 and windows of length `>= 1` only enlarging it).
- **Root failure self-loop guard** is needed as usual.
- **Why not the length-capped set trick?** It is legitimately optimal here since
  `Lmax <= 10`; the automaton is the technique that generalizes to unbounded
  pattern lengths and to reporting *which* patterns match, and is the reason this
  problem is filed under Aho–Corasick.
