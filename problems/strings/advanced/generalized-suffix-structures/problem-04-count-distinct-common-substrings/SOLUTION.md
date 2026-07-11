# Count Distinct Common Substrings — Solution

## Brute Force

Build the substring set of the first string with a hash set, then for each
subsequent string build its substring set and intersect. With total length `L`
there are `O(L^2)` substrings each up to `O(L)` long, so this is `O(L^2)` hashing
work per string (with rolling hashes) and `O(L^2)` space — fine for tiny inputs,
impossible at `L = 10^6`.

- **Time:** `O(k * L^2)` (rolling hashes) / worse with literal substrings.
- **Space:** `O(L^2)`.

## Optimal Approach (Generalized Suffix Structure)

### Idea

This is the counting cousin of Problem 3. Build **one** generalized suffix
automaton over all `k` strings and tag each state with a `k`-bit ownership mask
(propagated up the suffix-link tree). A state whose mask is all-ones represents
substrings common to every string — and it represents exactly
`len[v] - len[link[v]]` **distinct** such substrings. Summing that quantity over
all all-ones states counts every distinct common substring exactly once.

### Why it is correct

Two facts do all the work:

1. **Ownership.** After OR-ing each string's bit into the states it occupies and
   propagating up suffix links, `mask[v]` is precisely the set of strings whose
   substrings pass through state `v`. Because every substring in `v` shares the
   same `endpos`, "`mask[v]` is all-ones" means *every* substring represented by
   `v` occurs in all `k` strings.
2. **Distinct partition.** State `v` represents the substrings of lengths in
   `(len[link[v]], len[v]]`, i.e. exactly `len[v] - len[link[v]]` distinct
   strings, and these ranges partition all distinct substrings of the union with
   no overlap. Restricting the sum to all-ones states therefore counts each
   distinct *common* substring exactly once.

The only subtlety: could a substring counted at an all-ones state have some of
its members not common while others are? No — all substrings in one state share
one `endpos`, hence share ownership. The mask is a property of the whole state.

### Steps

1. Build the GSA, inserting each string with `last` reset to root; OR the current
   string's bit into every state returned by `extend`.
2. Propagate masks up the suffix links (states in decreasing `len`).
3. Sum `len[v] - len[link[v]]` over all non-root states with `mask[v]` all-ones.

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

def count_common_substrings(strings):
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
    return sum(g.length[v] - g.length[g.link[v]]
               for v in range(1, S) if mask[v] == full)
```

### Complexity

- **Build:** `O(L)` for a fixed alphabet (`L = sum of lengths`).
- **Mask propagation:** `O(L)` (counting sort by length) or `O(L log L)`.
- **Counting pass:** `O(L)`.
- **Space:** `O(L)`.

## Key Insights & Edge Cases

- This differs from Problem 3 only in the final aggregation: **sum**
  `len[v] - len[link[v]]` instead of **max** `len[v]` over all-ones states.
- Two identical strings return the count of distinct substrings of that string.
- No common character -> no all-ones state -> answer `0`.
- The formula `len[v] - len[link[v]]` is safe for non-root states; never take it
  at the root (skip `v = 0`).
- Restricting to a specific subset (e.g. "common to strings `A` and `C` only")
  is a one-line change: test `mask[v] & required == required` and adjust the
  target mask.
- To count substrings common to **at least `k`** strings instead of all of them,
  count set bits per state (see Problem 5) rather than testing for all-ones.
