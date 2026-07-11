# Solution — Count Keyword Occurrences

## Brute Force

Deduplicate the keywords, then for each distinct keyword run a substring search
over `text` counting overlapping occurrences (advance by one after each hit, not
by the pattern length).

```python
def count_keyword_occurrences(keywords, text):
    total = 0
    for kw in set(keywords):
        start = 0
        while True:
            i = text.find(kw, start)
            if i == -1:
                break
            total += 1
            start = i + 1          # +1, not +len(kw), to allow overlaps
    return total
```

- **Time:** `O(K · n)` where `K` is the number of distinct keywords and
  `n = len(text)`. With `K` up to `10^4` and `n` up to `10^6` this is `~10^10`
  character comparisons — far too slow.
- **Space:** `O(K · L)` to hold the keyword set.

## Optimal Approach (Aho–Corasick Automaton)

Build a single automaton over the distinct keywords and scan the text once.

**Why it is correct.** Aho–Corasick guarantees that after consuming
`text[0..i]`, the current node represents the **longest suffix of the consumed
text that is a prefix of some keyword.** Every keyword that ends at position `i`
corresponds to a terminal node reachable from the current node by following
**dictionary-suffix links** (the chain of proper suffixes that are themselves
complete keywords). Summing, over all positions, the number of keywords that end
there yields exactly the number of `(keyword, start index)` occurrence pairs —
including overlaps, since each ending position is examined independently.

**Making it linear.** Naively walking the dictionary-link chain at every
position costs `O(z)` where `z` is the number of matches, which can be
`Θ(n · maxlen)` (e.g. `"aa","aaa","aaaa",…"` over `"aaaa…"`). To count in pure
`O(n)`, precompute for every node a **`suffix_count`** = (1 if the node is
terminal else 0) + `suffix_count[dict_link[node]]`. This is computed during the
BFS (parents before children in failure-depth order), so at each text position
we just add `suffix_count[cur]` — amortized `O(1)` per character.

**Step by step.**

1. `set(keywords)` to deduplicate; insert each into the trie, marking terminal
   nodes with a count (use a boolean; duplicates already removed).
2. BFS to compute failure links and the `O(1)` goto transitions.
3. During the BFS also compute `suffix_count[node] = is_terminal[node] +
   suffix_count[fail[node]]` (fail-node is always shallower, already processed).
4. Scan `text`: maintain current node `cur`; for each char follow goto/fail to
   the next node and add `suffix_count[cur]` to the answer.

```python
from collections import deque

def count_keyword_occurrences(keywords, text):
    keywords = set(keywords)
    nxt = [{}]
    fail = [0]
    term = [0]           # 1 if a keyword ends exactly at this node
    for kw in keywords:
        cur = 0
        for ch in kw:
            if ch not in nxt[cur]:
                nxt.append({}); fail.append(0); term.append(0)
                nxt[cur][ch] = len(nxt) - 1
            cur = nxt[cur][ch]
        term[cur] = 1

    suffix_count = [0] * len(nxt)
    q = deque()
    for ch, v in nxt[0].items():
        fail[v] = 0
        q.append(v)
    while q:
        u = q.popleft()
        suffix_count[u] = term[u] + suffix_count[fail[u]]
        for ch, v in nxt[u].items():
            f = fail[u]
            while f and ch not in nxt[f]:
                f = fail[f]
            fail[v] = nxt[f].get(ch, 0) if (f or ch in nxt[0]) else 0
            if fail[v] == v:
                fail[v] = 0
            q.append(v)

    ans = cur = 0
    for ch in text:
        while cur and ch not in nxt[cur]:
            cur = fail[cur]
        cur = nxt[cur].get(ch, 0)
        ans += suffix_count[cur]
    return ans
```

- **Build:** `O(S · σ)` time, `O(S · σ)` space, `S = Σ|distinct keyword|`,
  `σ = 26`.
- **Scan:** `O(n)` time (the `while cur` failure hops are amortized `O(1)` per
  character by the standard KMP potential argument), `O(1)` extra space.

## Key Insights & Edge Cases

- **Overlaps count**: because we credit *every* ending position, `"aa"` in
  `"aaa"` is counted 2 times automatically — no `+len(kw)` skipping.
- **Nested keywords**: `"he"` ending inside `"she"` at the same position is what
  `suffix_count` captures via the dictionary links; do not stop at the first
  terminal node.
- **Duplicate keywords**: deduplicate up front so the same keyword is not counted
  twice per position. (If the problem instead wanted multiplicity, store a count
  per terminal node.)
- **Root self-loop bug**: guard the failure computation so a depth-1 node's
  failure link points to the root (0), never to itself — otherwise the scan can
  loop forever.
- **No matches** returns `0`; a single-character text and single-character
  keywords are handled by the same code path.
