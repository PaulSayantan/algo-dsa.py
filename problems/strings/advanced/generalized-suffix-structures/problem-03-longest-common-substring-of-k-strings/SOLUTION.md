# Longest Common Substring of K Strings — Solution

## Brute Force

Take the shortest string (length `s`); enumerate all `O(s^2)` of its substrings
and, for each, test membership in the other `k - 1` strings. A membership test is
`O(len)` with a substring search, so the total is roughly
`O(s^2 * (k * L_max))` — astronomically slow for `s` around `10^5`. Even the
"binary search on the answer length + hash-set intersection per length" idea is
`O(L log L)` expected but relies on hashing and risks collisions.

- **Time:** `O(s^2 * k * L_max)` naive; `O(L log L)` expected with rolling hashes
  + binary search.
- **Space:** `O(L)` for the hash sets.

## Optimal Approach (Generalized Suffix Structure)

### Idea

Build **one** generalized suffix automaton over all `k` strings and tag each
state with a `k`-bit mask telling which strings occur at that state. Any state
whose mask is "all ones" (`(1 << k) - 1`) represents substrings common to every
string; the longest such substring has length `len[v]`, so the answer is the
maximum `len[v]` over all-ones states.

### Why it is correct

Recall the two structural facts of a suffix automaton:

1. A state `v` represents all substrings of one `endpos` class, i.e. the suffixes
   of its longest member with lengths in `(len[link[v]], len[v]]`.
2. `endpos(v)` is the union of `endpos` of `v`'s children in the suffix-link
   tree, plus any positions where `v` itself is the longest suffix.

If we OR string-`i`'s bit into a state each time inserting string `i` makes that
state the current longest suffix (a *primary occurrence*), and then propagate
those bits up the suffix links, `mask[v]` becomes exactly the set of strings that
contain the substrings of state `v`. When `mask[v]` has all `k` bits, **every**
substring in `v` (in particular its longest, length `len[v]`) occurs in all `k`
strings, so it is a valid common substring. Taking the max `len[v]` over such
states gives the longest common substring of all `k` strings.

### Steps

1. Build the GSA, inserting each of the `k` strings after resetting `last = root`.
   After appending a character while inserting string `i`, set the returned
   state's primary bit `marks[state] |= (1 << i)`.
2. Compute `mask[v]` for all states by processing states in **decreasing `len`**
   (children before parents) and OR-ing `mask[v]` into `mask[link[v]]`.
3. Answer = `max(len[v] for v with mask[v] == (1 << k) - 1)`, or `0`.

### Reference implementation

```python
from collections import defaultdict

class GSA:
    def __init__(self):
        self.nxt = [dict()]; self.link = [-1]; self.length = [0]
    def _new(self, length, link, trans=None):
        self.nxt.append(dict(trans) if trans else dict())
        self.link.append(link); self.length.append(length)
        return len(self.nxt) - 1
    def extend(self, c, last):
        if c in self.nxt[last]:
            q = self.nxt[last][c]
            if self.length[last] + 1 == self.length[q]:
                return q
            clone = self._new(self.length[last] + 1, self.link[q], self.nxt[q])
            self.link[q] = clone; p = last
            while p != -1 and self.nxt[p].get(c) == q:
                self.nxt[p][c] = clone; p = self.link[p]
            return clone
        cur = self._new(self.length[last] + 1, -1); p = last
        while p != -1 and c not in self.nxt[p]:
            self.nxt[p][c] = cur; p = self.link[p]
        if p == -1:
            self.link[cur] = 0
        else:
            q = self.nxt[p][c]
            if self.length[p] + 1 == self.length[q]:
                self.link[cur] = q
            else:
                clone = self._new(self.length[p] + 1, self.link[q], self.nxt[q])
                self.link[q] = clone; self.link[cur] = clone
                while p != -1 and self.nxt[p].get(c) == q:
                    self.nxt[p][c] = clone; p = self.link[p]
        return cur

def longest_common_substring_k(strings):
    g = GSA()
    marks = defaultdict(int)
    for i, w in enumerate(strings):
        last = 0
        for ch in w:
            last = g.extend(ch, last)
            marks[last] |= (1 << i)
    S = len(g.link)
    mask = [marks.get(v, 0) for v in range(S)]
    for v in sorted(range(S), key=lambda v: -g.length[v]):
        p = g.link[v]
        if p != -1:
            mask[p] |= mask[v]
    full = (1 << len(strings)) - 1
    return max((g.length[v] for v in range(S) if mask[v] == full), default=0)
```

### Complexity

- **Build:** `O(L)` (`L = sum of lengths`) for a fixed alphabet.
- **Mask propagation:** `O(L)` with counting sort by length, or `O(L log L)` with
  a comparison sort; then one linear pass. The `k`-bit mask fits in a machine
  word for `k <= 64`, so each OR is `O(1)`.
- **Answer scan:** `O(L)`.
- **Space:** `O(L)`.

## Key Insights & Edge Cases

- **`k`-bit masks are `O(1)`** for `k` up to the machine word size (`k <= 10`
  here comfortably). For large `k` you would instead maintain, per state, a count
  of *distinct* strings seen — but plain OR over bits double-counts nothing and
  is simplest for small `k`.
- Set the primary bit only on the state **returned by `extend`** (the longest
  suffix ending at the current index). This is where the propagation invariant
  begins.
- Sorting states by **decreasing length** guarantees the suffix-link child is
  processed before its parent, so a single OR pass suffices.
- No shared character across all strings -> no all-ones state -> answer `0`.
- Duplicate input strings just set the same bit again; harmless.
- Contrast with two-string LCS, where you can instead build the SAM of one string
  and stream the other through it. That trick does not extend to `k > 2`; the
  generalized-SAM + mask approach is the idiomatic multi-string solution.
