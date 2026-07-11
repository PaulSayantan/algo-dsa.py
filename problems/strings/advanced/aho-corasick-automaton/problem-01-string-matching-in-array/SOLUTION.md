# Solution — String Matching in an Array

## Brute Force

For every ordered pair `(i, j)` with `i != j`, test whether `words[i]` is a
substring of `words[j]` using Python's `in` operator (which internally runs a
linear substring search). Collect each `words[i]` that succeeds for at least one
`j`.

```python
def stringMatching(self, words):
    res = []
    for i, a in enumerate(words):
        if any(i != j and a in b for j, b in enumerate(words)):
            res.append(a)
    return res
```

- **Time:** `O(n^2 · L)` where `n = len(words)` and `L` is the max word length
  (each `in` is `O(L)` best case, `O(L^2)` worst with naive matching but CPython
  uses a fast two-way search, so treat it as `O(L)` amortized). With
  `n <= 100`, `L <= 30`, this is trivially fast and passes.
- **Space:** `O(1)` beyond the output.

This is the pragmatic answer for the given constraints and is a great oracle to
check the automaton against.

## Optimal Approach (Aho–Corasick Automaton)

To make the matching cost independent of the number of patterns, build **one**
automaton over all words and stream each word through it.

**Why it is correct.** The automaton, when fed a text `T`, reports the end
position of every pattern occurrence in `T`. If we set `T = words[j]` and the
automaton contains all words as patterns, then any pattern `words[i]` reported
inside `words[j]` is by definition a contiguous substring of `words[j]`. We only
need to exclude the case `i == j` (a word matching itself), which we do by
checking `len(words[i]) < len(words[j])` **or** `i != j`. Because all words are
distinct, a strictly-shorter match is automatically a different word; an
equal-length match can only be the word itself, so we ignore equal-length hits.

**Step by step.**

1. Insert every `words[i]` into a trie; store the pattern's index at its
   terminal node (and its length).
2. BFS from the root to compute a **failure link** for each node — the node for
   the longest proper suffix of the current string that is also a prefix of some
   pattern — and precompute a **goto/transition** table so each step is `O(1)`.
3. Compute **dictionary suffix links** so that at any node we can enumerate all
   patterns ending there (needed because e.g. matching `superhero` should report
   both `hero` and, if present, `ero`-type suffixes that are themselves words).
4. For each `words[j]`, walk the automaton character by character; at every node
   follow the dictionary-link chain and mark every pattern index found — as long
   as that pattern is shorter than `words[j]` (so a word never reports itself).
5. Output the words whose index got marked.

```python
from collections import deque

class Aho:
    def __init__(self, patterns):
        self.next = [{}]          # trie transitions
        self.fail = [0]
        self.out = [[]]           # pattern indices ending exactly here
        self.dict_link = [0]      # link to nearest ancestor-suffix that is terminal
        for idx, p in enumerate(patterns):
            self._add(p, idx)
        self._build()

    def _add(self, p, idx):
        cur = 0
        for ch in p:
            if ch not in self.next[cur]:
                self.next.append({}); self.fail.append(0)
                self.out.append([]); self.dict_link.append(0)
                self.next[cur][ch] = len(self.next) - 1
            cur = self.next[cur][ch]
        self.out[cur].append(idx)

    def _build(self):
        q = deque()
        for ch, nxt in self.next[0].items():
            self.fail[nxt] = 0
            q.append(nxt)
        while q:
            u = q.popleft()
            # dict_link: nearest terminal via failure chain
            f = self.fail[u]
            self.dict_link[u] = f if self.out[f] else self.dict_link[f]
            for ch, v in self.next[u].items():
                f = self.fail[u]
                while f and ch not in self.next[f]:
                    f = self.fail[f]
                self.fail[v] = self.next[f].get(ch, 0) if f or ch in self.next[0] else 0
                q.append(v)

    def matches_in(self, text):
        found = set()
        cur = 0
        for ch in text:
            while cur and ch not in self.next[cur]:
                cur = self.fail[cur]
            cur = self.next[cur].get(ch, 0)
            node = cur
            while node:
                for idx in self.out[node]:
                    found.add(idx)
                node = self.dict_link[node]
        return found

class Solution:
    def stringMatching(self, words):
        aho = Aho(words)
        marked = set()
        for j, w in enumerate(words):
            for i in aho.matches_in(w):
                if i != j:          # never let a word match itself
                    marked.add(i)
        return [words[i] for i in sorted(marked)]
```

Because all words are distinct, `matches_in(w)` can only report index `j`
itself as an equal-length hit, so the single `i != j` guard is sufficient.

- **Build:** `O(S)` for the trie and `O(S · σ)` for the links, `S = Σ|words[i]|`.
- **Matching:** `O(Σ|words[j]| + z) = O(S + z)` total, where `z` is the number of
  reported (pattern, position) pairs.
- **Space:** `O(S · σ)` for the automaton.

## Key Insights & Edge Cases

- **Self-match exclusion is the only trap.** Because words are distinct, a match
  strictly shorter than the host word is always a different word. Guard equal
  lengths carefully: two distinct equal-length words can still be substrings only
  if identical, which cannot happen here — so an equal-length hit inside a word
  is necessarily the word itself and must be skipped.
- **Overlapping / nested patterns** (`hero` inside `superhero`, `as` inside
  `mass`) are handled naturally by the dictionary-suffix-link chain; do not stop
  at the first match at a node.
- **Empty answer** (Example 3) must return `[]`, not `None`.
- For the given constraints the brute force is genuinely optimal in practice;
  the automaton shines when `n` and `L` grow large or when the word set is reused
  across many texts.
