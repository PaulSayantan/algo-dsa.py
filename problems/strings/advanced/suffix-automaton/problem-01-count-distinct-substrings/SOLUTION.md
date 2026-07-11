# Count Distinct Substrings — Solution

## Brute Force

Enumerate every substring and insert it into a hash set, then return the set
size. There are `O(n^2)` substrings and each has length up to `n`, so hashing
them all costs `O(n^3)` time (or `O(n^2)` if you use rolling hashes, at the risk
of collisions) and `O(n^2)` space. This is fine for `n` up to a few thousand but
blows up at `n = 10^5`.

A cleaner `O(n^2 log n)` alternative uses a suffix array + LCP array: the number
of distinct substrings equals `n*(n+1)/2 - sum(LCP[i])`. That is the standard
suffix-array trick, but a Suffix Automaton gives an even simpler linear pass.

- **Time:** `O(n^3)` naive / `O(n^2)` with rolling hashes.
- **Space:** `O(n^2)`.

## Optimal Approach (Suffix Automaton)

### Why it works

In a Suffix Automaton every distinct substring corresponds to exactly one path
from the initial state, and every state `v` groups together all substrings that
end at the same set of positions (`endpos`). Within one state, the substrings
are exactly the suffixes of its longest member whose length lies in the interval
`(len[link[v]], len[v]]`. Therefore state `v` is responsible for precisely

```
len[v] - len[link[v]]
```

distinct substrings, and these ranges partition the whole set of distinct
substrings with no overlaps and no gaps. Summing over all states (excluding the
initial state, whose `len = 0`) counts each distinct substring exactly once.

### Steps

1. Build the SAM of `s` by extending it one character at a time (`sa_extend`).
2. Iterate over all states `v != initial`.
3. Accumulate `len[v] - len[link[v]]`.

### Reference implementation

```python
class SuffixAutomaton:
    def __init__(self):
        self.next = [dict()]     # transitions per state
        self.link = [-1]         # suffix link (-1 for the root)
        self.length = [0]        # length of longest substring in the state
        self.last = 0            # state for the whole current prefix

    def extend(self, c):
        cur = len(self.next)
        self.next.append(dict())
        self.link.append(-1)
        self.length.append(self.length[self.last] + 1)
        p = self.last
        while p != -1 and c not in self.next[p]:
            self.next[p][c] = cur
            p = self.link[p]
        if p == -1:
            self.link[cur] = 0
        else:
            q = self.next[p][c]
            if self.length[p] + 1 == self.length[q]:
                self.link[cur] = q
            else:
                clone = len(self.next)
                self.next.append(dict(self.next[q]))
                self.link.append(self.link[q])
                self.length.append(self.length[p] + 1)
                while p != -1 and self.next[p].get(c) == q:
                    self.next[p][c] = clone
                    p = self.link[p]
                self.link[q] = clone
                self.link[cur] = clone
        self.last = cur


def count_distinct_substrings(s: str) -> int:
    sam = SuffixAutomaton()
    for ch in s:
        sam.extend(ch)
    return sum(sam.length[v] - sam.length[sam.link[v]]
               for v in range(1, len(sam.length)))
```

### Complexity

- **Build:** `O(n)` states/transitions; with a dict `next` the total work is
  `O(n log |Sigma|)` (effectively `O(n)` for a fixed alphabet).
- **Counting pass:** `O(number of states) = O(n)`.
- **Space:** `O(n * |Sigma|)` worst case for transitions.

## Key Insights & Edge Cases

- The initial state has `len = 0` and `link = -1`; skip it (start the sum at
  state `1`). Never dereference `link[root]`.
- The formula `len[v] - len[link[v]]` is always non-negative because a state's
  suffix link always points to a strictly shorter substring class.
- Single character string (`"a"`) -> exactly `1` distinct substring.
- All-identical string `"aaaa"` -> `n` distinct substrings (`"a"`, `"aa"`, ...).
- The same summation, but adding the length contribution instead of the count,
  gives the *total length* of all distinct substrings — see Problem 2.
- If you want a `O(n)`-transition SAM, replace the dict with fixed-size arrays
  of size `|Sigma|`; the logic is identical.
