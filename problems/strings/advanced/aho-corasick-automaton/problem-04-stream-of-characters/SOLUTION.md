# Solution — Stream of Characters

## Brute Force

Keep a growing list of all characters seen. On each `query`, append the new
letter, then test every word to see whether it equals the last `len(word)`
characters of the stream.

```python
class StreamChecker:
    def __init__(self, words):
        self.words = words
        self.stream = []
        self.maxlen = max(map(len, words))

    def query(self, letter):
        self.stream.append(letter)
        tail = self.stream[-self.maxlen:]
        s = "".join(tail)
        return any(s.endswith(w) for w in self.words)
```

- **Time:** `O(W · L)` per query (`W` words, comparing up to `L` chars each), so
  `O(Q · W · L)` overall. With `Q = 4·10^4`, `W = 2000`, `L = 200` this is
  `~1.6·10^10` operations — too slow.
- **Space:** `O(Q)` for the stream (or `O(L)` if you keep only the tail).

A common optimization builds a **trie of reversed words** and walks the reversed
stream tail on each query — correct, but each query is still `O(L)` in the worst
case. Aho–Corasick makes each query `O(1)` amortized.

## Optimal Approach (Aho–Corasick Automaton)

Build the automaton over the words **in their natural (forward) orientation** and
keep one persistent `cur` node representing the longest dictionary-prefix that is
a suffix of the stream so far.

**Why it is correct.** This is the streaming form of Aho–Corasick text scanning:
treating the entire stream as the "text," after consuming character `t` the node
`cur` is, by the automaton's invariant, the node for the **longest suffix of the
stream that is a prefix of some word.** A word `w` is a suffix of the stream iff
`w` ends at the current position — i.e. iff the terminal node for `w` lies on
`cur`'s dictionary-suffix-link chain. Precompute `suffix_word[node]` = "is this
node terminal, or does its dict-link chain reach a terminal node," so a query is
a single transition plus a boolean lookup.

**Step by step.**

1. Build the trie over `words`; mark terminal nodes.
2. BFS to compute failure links and `O(1)` goto transitions.
3. During BFS set `suffix_word[node] = is_terminal[node] or
   suffix_word[fail[node]]` (fail node is shallower, already finalized).
4. Keep `self.cur = 0`. On `query(ch)`: advance `cur` via goto/failure to the
   next node and return `suffix_word[cur]`.

```python
from collections import deque

class StreamChecker:
    def __init__(self, words):
        nxt = [{}]; fail = [0]; term = [False]
        for w in words:
            cur = 0
            for ch in w:
                if ch not in nxt[cur]:
                    nxt.append({}); fail.append(0); term.append(False)
                    nxt[cur][ch] = len(nxt) - 1
                cur = nxt[cur][ch]
            term[cur] = True

        suffix_word = [False] * len(nxt)
        q = deque()
        for ch, v in nxt[0].items():
            fail[v] = 0; q.append(v)
        while q:
            u = q.popleft()
            suffix_word[u] = term[u] or suffix_word[fail[u]]
            for ch, v in nxt[u].items():
                f = fail[u]
                while f and ch not in nxt[f]:
                    f = fail[f]
                fail[v] = nxt[f].get(ch, 0) if (f or ch in nxt[0]) else 0
                if fail[v] == v:
                    fail[v] = 0
                q.append(v)

        self.nxt, self.fail, self.suffix_word = nxt, fail, suffix_word
        self.cur = 0

    def query(self, letter):
        cur, nxt, fail = self.cur, self.nxt, self.fail
        while cur and letter not in nxt[cur]:
            cur = fail[cur]
        cur = nxt[cur].get(letter, 0)
        self.cur = cur
        return self.suffix_word[cur]
```

- **Build (`__init__`):** `O(S · σ)` time and space, `S = Σ|words[i]|`.
- **`query`:** `O(1)` amortized (KMP potential argument bounds total failure hops
  by the number of queries), `O(1)` extra space.
- **Total over `Q` queries:** `O(S · σ + Q)`.

## Key Insights & Edge Cases

- **Forward automaton, persistent node.** The key realization is that "is any
  word a *suffix* of the stream" over an *append-only* stream is exactly the
  Aho–Corasick "does any pattern end here" query — no need to reverse words if
  you keep a single advancing node. (The reversed-trie approach also works but is
  `O(L)` per query.)
- **Precompute the suffix flag.** Walking dict-links on every query would make a
  pathological set of nested words (`a`, `aa`, `aaa`, …) cost `O(L)` per query;
  folding it into `suffix_word` during BFS keeps queries `O(1)`.
- **Single-character words** and words that are prefixes/suffixes of one another
  are handled by the failure/dictionary-link machinery; verify with Example 2
  where `"ab"` and `"ba"` interleave.
- **Root failure self-loop guard** (`fail[v] == v → 0`) is essential for
  correctness on depth-1 nodes.
- **State persists across queries** — do not reset `self.cur`; that persistence
  is what makes the stream online.
